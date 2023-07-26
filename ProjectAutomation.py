import os

def ProjAutomation():
    destinationPath = input("Enter the directory path to create the project folder: ").strip()
    projName = input("Enter the project name: ").strip()
    projPath = os.path.join(destinationPath, projName)
    try:
        os.makedirs(projPath)
        print(f"Project folder '{projName}' created successfully.")
    except FileExistsError:
        print(f"Project folder '{projName}' already exists.")
    readmePath = os.path.join(projPath, "README.md")
    with open(readmePath, "w") as readmeFile:
        readmeFile.write(f"# {projName}\n")
        readmeFile.write(f"\nEnter Contents into this ReadMe file for documentation\n")
    print("README.md file created successfully.")

ProjAutomation()
