# ReadMe.md
## Description
This is a simple script the merges multiple excel files (xlsx files). It takes the column names from one file and ignores the column names for the rest of the files.

## Installation
Clone this directory anywhere onto your machine

### Prerequisites / Dependencies 
This project runs on python 3 and requires the packages: openpyxl, datetime and Pathlib installed.

## Primary setup and usage
The file containing the program and required directories (as well as this ReadMe file) may be placed anywhere on the system. Inside the file the following must be present:
* The python script; **Main.py**
* A python script named **Functions.py**
* The user license; **LICENSE.txt**
* A folder named **Merged**
* A folder named **Unmerged**
* This file- **ReadMe.md**

Notes:
* The folders’ names and the scripts’ names must remain unchanged and in the same capitalisation as above.
* None of the individual files or folders can be relocated. 
* Another files present in the directory may be ignored but not deleted.

### Usage
The unmerged files must be placed in the “Unmerged” directory. The script will only work with .xlsx files. The files must have only column names in the first row. The first row and first column must not have any gaps (this was a side effect of the fact that the program has no limit on the dimensions of the excel files). Finally this program is not tested with merged cells and was not designed to handle them.

The merged excel file will returned to the Merged directory. The file will be called Merged and will have the current date.

To run the script the Main.py python file is all that needs to be run.

## Notes
If you want the program to ignore certain files in the Unmerged directory, edit the first if statement in Functions.py