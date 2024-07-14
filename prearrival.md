## Prearrival information

---
You should *attempt* to install these two main tools before you arrive to the first day of class.

### How to Install Git

Git is a distributed version control system widely used for tracking changes in source code during software development. Here's a step-by-step guide to installing Git on various operating systems.

##### Windows

Go to the official [Git website](https://gitforwindows.org/). Download the latest version of the Git installer. Open the downloaded .exe file. Follow the installer steps. It's generally safe to accept the default settings, but here are some key points:
* Select Components: Make sure to select "Git Bash Here" and "Git GUI Here" to add useful context menu shortcuts.
* Choosing the default editor used by Git: You can select your preferred text editor.
* Adjusting the name of the initial branch in new repositories: You can leave this as "master" or set a custom name.
* Adjusting your PATH environment: Choose "Git from the command line and also from 3rd-party software".
* Choosing HTTPS transport backend: Opt for "Use the OpenSSL library".
* Configuring the line ending conversions: Choose "Checkout Windows-style, commit Unix-style line endings".
* Configuring the terminal emulator to use with Git Bash: Use "Use MinTTY (the default terminal of MSYS2)".
* Configuring extra options: Enable the necessary extra options, such as "Enable file system caching".
* **Verifying the Install**: Open Git Bash from the Start menu or context menu.

Type the following command to verify the installation and check the Git version:
```bash
git --version
```

##### macOS

Install Homebrew (if not already installed): 

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

In the Terminal, type the following command:

```bash
brew install git
```

Check the installed Git version:

```bash
git --version
```
##### Linux

Debian/Ubuntu-based systems:

```bash
sudo apt update
sudo apt install git
```

Check the installed Git version:

```bash
git --version
```

After installing Git, it's essential to configure your Git environment.

Set your username:

```bash
git config --global user.name "Your Name"
```

Set your email address:

```bash
git config --global user.email "your.email@example.com"
```
Verify your configuration:

```bash
git config --list
```

You have now installed Git and completed the initial setup. You can start using Git for your version control needs. For further learning, consider checking the official Git documentation: Git Documentation.

### How to Install Python (Anaconda)


* **Download Anaconda**: Visit the [Anaconda website](https://www.anaconda.com/download/).
Choose your operating system: Anaconda supports Windows, macOS, and Linux. Select the version appropriate for your system. Download the installer: Click on the download button for Anaconda Individual Edition.
* **Install Anaconda for Windows**: Run the installer: Once the download completes, locate the installer file (typically named Anaconda3-<version>-Windows-x86_64.exe) and double-click it to launch.  Follow the setup wizard. Click "Next" to begin installation. Read and accept the license agreement. Select the installation location (you can leave it as default).  Choose whether to add Anaconda to your PATH environment variable (recommended).  Complete the installation: Click "Install" to begin the installation process. Once completed, click "Next" and then "Finish" to exit the installer.

* **Install Anaconda for For macOS**: Run the installer: Open the downloaded .pkg file (e.g., Anaconda3-<version>-MacOSX-x86_64.pkg) by double-clicking it. Follow the installation instructions: Click "Continue" and then "Agree" to accept the license agreement. Choose the installation location (typically /Users/your-username/anaconda3/). Click "Install" to begin the installation. Verify the installation: After the installation completes, you can close the installer.

* **Install Anaconda For Linux**: Open a terminal: Navigate to the directory where the downloaded installer script is located. Run the installer script: Change the permissions of the script to make it executable if needed:
```bash
chmod +x Anaconda3-<version>-Linux-x86_64.sh
./Anaconda3-<version>-Linux-x86_64.sh
```

* Follow the installer prompts: You'll be asked to review the license agreement (press Enter to scroll through), and then type "yes" to agree.  Choose the installation location (default is typically /home/your-username/anaconda3). Type "yes" to initialize Anaconda in your ~/.bashrc (or equivalent) to automatically set up Anaconda every time you open a terminal. Activate the installation: After the installation is complete, close and reopen your terminal.

* **Verify Your Installation:** Test in terminal: Open a new terminal and type ```conda list``` to see a list of installed packages.

