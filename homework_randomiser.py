# Note: if a student who is selected isn't present,
# set a lower num_to_select to draw more on same day

import random
import csv
import os

# Function to read previously selected names from a file
def read_selected_names(filename):
    selected_names = set()
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                selected_names.add(row[0])  # assuming names are in the first column
    return selected_names

# Function to select 3 unique names that haven't been selected before
def select_names(names_list, selected_set, num_to_select):
    available_names = [name for name in names_list if name not in selected_set]
    selected_names = random.sample(available_names, num_to_select)
    return selected_names

# Function to update the file with newly selected names
def update_selected_names(filename, selected_names):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        for name in selected_names:
            writer.writerow([name])

# Main function to run the selection process
def main():
    names_file = './assets/student_list.csv'
    selected_file = './assets/selected_names.csv'
    num_to_select = 2

    # Read names from CSV file
    with open(names_file, 'r') as file:
        reader = csv.reader(file)
        names_list = [row[0] for row in reader]

    # Read previously selected names
    selected_names = read_selected_names(selected_file)

    # Select new names
    selected = select_names(names_list, selected_names, num_to_select)

    # Update the list of selected names
    update_selected_names(selected_file, selected)

    # Print the selected names
    print("Selected names for today:")
    for name in selected:
        print(name)

if __name__ == "__main__":
    main()