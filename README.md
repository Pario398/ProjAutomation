# Project Automation

This is a "Project Automation" script in Python designed to create a folder for the project and a README.md file.

## Usage

1. Get a copy of the `ProjectAutomation.py`
2. Open a terminal or command prompt.
3. Navigate to the directory where the Python script is located.
4. Run the script using the command: `python FileOrganizer.py`

## Code Explanation

The script consists of the following sections:

### Importing Required Modules

```python
import os
```

In this section, we import the following Python module:

* `os`: This module provides a way to interact with the operating system, enabling file and directory-related operations.

## ProjAutomation

The **ProjAutomation function** allows the user to create a new project folder and a corresponding README.md file. Here's how it works:
1. The user is prompted to enter the destinationPath, which is the directory path where the project folder will be created.
2. Next, the user is prompted to enter the projName, which is the name of the project.
The os.path.join function combines the destinationPath and projName to form the complete path for the project folder.
3. The script creates the project folder using os.makedirs(projPath). If the folder already exists, it catches the FileExistsError and notifies the user that the project folder already exists.
4. The script then creates a new README.md file inside the project folder. It writes the project name as the title and adds a placeholder message to instruct the user to enter contents into the README file for documentation.

## Example
```bash
python ProjAutomation.py
Enter the directory path to create the project folder: /Users/users/Desktop/Projects
Enter the project name: NewProject
Project folder 'NewProject' created successfully.
README.md file created successfully.
```

