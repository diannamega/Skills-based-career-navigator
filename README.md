# Skills Exploration Tools

This is a starter repository for projects in the CAS502 class in the School of Complex Adaptive Systems at Arizona State University. If you choose to use the code in this repository for your project, please clone it into your own account and work with your clone.

## Set up

To set up the project, clone the repository. You need the following packages installed:
- pandas
- openpyxl
- networkx
- matplotlib

## How to run the code

To execute the tool, simply run `python skills.py`. It will run for a few moments and then ask you for a skill code. You can find the codes for each skill in the file `skills-list.csv` (e.g. `2.A.1.a` for "Reading Comprehension"). Once entered, the program will present you with a list of 10 skills are that are most often used in combination with the entered skill and the top five professions in which a skill is important for.

## Repository content

The following files are part of this repository:

- `skills.py`  
The code for this program.
- `skills-list.csv`  
CSV file with a list of skills and their codes.
- `data`  
This folder contains a number of data files. The files have been downloaded from [O*NET Resource Center](https://www.onetcenter.org/database.html), version 29.1 ([license](https://creativecommons.org/licenses/by/4.0/)). The file currently used in the code is `Skills.xlsx`. Additionally, there are two files in this folder:
  - `Occupation Data.xlsx`: Descriptions for each occupation.
  - `TechnologySkills.xlsx`: A list of technological skills for each occupation.

## Notes

This repository is intentially left pretty barebone, so you can use it for all the assignments in CAS502.