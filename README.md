# Python_for_DataScience

<p align="center">
  <img src="./assets/python_logo.png" width="200"/>&nbsp; &nbsp; &nbsp;<img src="./assets/python_logo.png" width="200"/>&nbsp; &nbsp; &nbsp;<img src="./assets/python_logo.png" width="200"/>
</p>

## :page_facing_up: # Python for Economic and Social Data Science  :page_facing_up:

![coverage](https://img.shields.io/badge/Teaching-yellow)
[![Generic badge](https://img.shields.io/badge/Python-blue.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/GNU3.0-purple.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Maintained-brightgreen.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/BuildPassing-orange.svg)](https://shields.io/)
---

### Introduction
Welcome to the 'Python for Economic and Social Data Science' class! This GitHub repository contains everything that we'll need for about ~20 hours of lectures. This course begins by assuming absolutely no knowledge of what Python is or can do, and hopefully ends with us being able to read data from the web, load it into data frame, visualise, and model it. The background of the class will determine how quickly we go. Please star this repository on GitHub if you are taking the class!

### Prearrival

There are lots of `subdirectories' and files within this repository here which we will need. The first is the [prearrival.md](./prearrival.md) file. That contains everything you need to know to get the two main tools which will be using installed. In particular, we're going to need two things installed, and they should both work for Windows, Linux, and Mac all the same!

* **Python**: A powerful, versatile language used for data analysis, visualization, and machine learning, with extensive libraries like pandas, NumPy, and scikit-learn

* **Git**: Git is a distributed version control system that tracks changes in code, enabling collaborative development and efficient project management.

If you are using a Chromebook, you might want to investigate [Google Collab](https://colab.research.google.com).

### Files

The five main subdirectories which we will need are:

1. [Lectures](./Lectures), which holds the five main tutorials that we'll work through together.
2. [Homeworks](./Homeworks), which holds three questions for each lecture.
3. [Solutions](./Solutions), which will be updated and populated day by day after you have solved the homeworks.
4. [Data](./Data), which is the place where we store data which we create and download.
5. [Figures](./Figures), which is where we still store our figures when we get to the matplotlib component of the class.

Homeworks are not optional, but should be *quite* easy if you've attended the lecture. My preferred system is to randomly select (via Python!) three people at the start of each following class to present their solutions to the group, with feedback. I'll roughly divide the questions up into three chunks at the start of the second, third, fourth and fifth class.

This is useful because *communicating* data science is every bit as important as doing it! You should consider writing your solutions in a Jupyter Notebook, the same tool that we are using to `live code' the lecture series. We will use ```homework_randomiser.py``` to achieve this: One of the goals of this course is actually to get us to a point where everybody understands what this is doing. I am never sharing the ```student_list.csv``` or ```selected_names.csv``` for confidentiality. **Note**: Do not forget to remove any randomly drawn students from the ```selected_names.csv``` file.

### Structure

The material is designed to last for about twenty hours, split across five 'lectures'.

* **Lecture One**: Basic object types and an introduction to collections (tenatively Day One, 13:00-1700)
* **Lecture Two**: Iterating over a collection, Boolean logic, advanced loops, user input and error handling (tenatively Day Two, 13:00-17:00)
* **Lecture Three**: Pseudocode, functions, file I/O, programming outside of Python, Numpy (tenatively Day Three, 13:00-17:00)
* **Lecture Four**: Random numbers, webscraping, Pandas (tenatively Day Four, 13:00-16:00)
* **Lecture Five**: Matplotlib, statsmodels, RobustiPy, NLTK, scikit-learn (tenatively Day Five, 13:00-17:00)

The classes should take between three to four hours. The first part of each of the second through fifth days will be a review of the homeworks. The class on Day Four needs to end one hour earlier. One 'lecture' doesn't necessarily correspond to one day: if we finish one lecture earlier on a specific day, we can move the next lecture. If we finish all five days of content early, we can spend the remaining time working on and discussing your own specific projects which you want to use Python for. At the end of each section of the notebooks, we will take a break from the lecture and you can play around in the notebooks following the set example question (which will then be live coded afterwards when the lectures resume). 

### Additional Material.

The internet is full of a multitude of excellent resources related to how to teach Python, especially for datascience. I learnt from [this](http://do1.dr-chuck.com/py4inf/EN-us/book.pdf) wonderful book called `Python for Informatics' by Charles Severance. There is also an *excellent* Coursera course which accompanies this, which can be found [here](https://www.coursera.org/learn/python) (also taught by Charles Severance). A colleague of mine (Bernie Hogan) wrote an excellent book called '[From Social Science to Data Science](https://uk.sagepub.com/en-gb/eur/from-social-science-to-data-science/book270152)' for those of you who are coming from a more social science background. Finally, for those who are interested in a _slightly_ more technical introduction, see Jake VanderPlas's excellent '[Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)' which we learn on heavily in *parts* of Lectures 3-5.