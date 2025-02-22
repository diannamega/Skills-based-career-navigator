# Skills-Based Career Navigator
# Team Members

Ken Nelson & Dianna Mega

# Project Description

The problem we're tackling is the disconnect between individuals and the evolving job market. This disconnect leads to several issues:

- **For Students:** High schoolers often lack the resources to make informed decisions about college majors or career paths, leading to potential wasted time and money on unsuitable education.
- **For Career Changers:** Individuals seeking new careers struggle to identify roles that align with their existing skills, hindering efficient job searching and career transitions.
- **For Educational Institutions:** Trade schools and universities may find it challenging to keep their curriculum aligned with the skills demanded by emerging industries, potentially leaving graduates ill-prepared for the workforce.

This project aims to bridge this gap by creating a tool that:
- Empowers individuals to make data-driven decisions about their education and career paths.
- Facilitates efficient career transitions by matching existing skills to in-demand jobs.
- Enables educational institutions to adapt their curriculum to meet future workforce needs.

By addressing these issues, we aim to promote better alignment between individual skills and labor market demands, leading to more fulfilling careers and a more efficient workforce.

# Basic Functionality Features

- **Interactive Skill Matching:** Interactive Skill Matching allows users to input their skills and interests, then matches them with relevant occupations and educational paths. This dynamic tool helps users explore career options and identify potential skill gaps they may need to address.
- **Occupation Exploration:** Occupation Exploration provides detailed insights into various occupations, including required skills, projected growth, and potential salary ranges. This feature enables users to research potential career paths and make informed decisions.
- **Personalized Skills Development Roadmap:** Personalized Skills Development Roadmap creates a tailored plan for users to acquire the necessary skills for their target occupation, including recommendations for courses, certifications, and other learning resources. This feature helps users bridge their skill gaps and enhance their employability.

# Nice to Have Functionality Features

- **Educational Pathway Guidance:** Educational Pathway Guidance makes recommendations on potential educational paths, including college majors and vocational programs, based on a user's chosen career interests and skillset. This helps users identify programs that will best prepare them for their desired field.
- **Regional Workforce Analysis:** Regional Workforce Analysis allows users to explore skill demands and occupation trends within specific geographic areas. This feature helps individuals and institutions understand local labor market dynamics and make informed decisions based on regional needs.
- **Policy Recommendation Generation:** Policy Recommendation Generation analyzes skills gaps and future workforce needs to suggest policy recommendations, such as developing targeted education programs or workforce development initiatives.

# Skills Exploration Tools

This is a starter repository for projects in the CAS502 class in the School of Complex Adaptive Systems at Arizona State University. If you choose to use the code in this repository for your project, please clone it into your own account and work with your clone.

## What the code does

This Python script analyzes soft skills data to recommend potential careers. It loads data from CSV files, creates a network of occupations based on shared codes, allows users to input their soft skills, and then ranks occupations based on how well their required skills match the user's. Finally, it presents the top recommended careers in a neatly formatted table, displaying the occupation, associated code, and the average of the relevant "Skills Covered" percentages.

## Set up

To set up the project, clone the repository. You need the following packages installed:
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/2.5/index.html)
- [networkx](https://networkx.org/)
- [matplotlib](https://matplotlib.org/)

See [Installation Guide](Install.md) for more information.

## How to run the code

To execute the tool, simply 
Open a command prompt (Windows) or Terminal (Linux/Mac)
run `python skills.py`. It will run for a few moments and then ask you for a skill code. You can find the codes for each skill in the file `skills-list.csv` (e.g. `2.A.1.a` for "Reading Comprehension"). Once entered, the program will present you with a list of 10 skills are that are most often used in combination with the entered skill and the top five professions in which a skill is important for.

## User Documentation

Follow the how to run the code section above. Then you, the user, will be prompted to enter one or more soft skills. The available soft skills are available as part of the prompt.

```
Enter your soft skills (comma-separated, e.g., learningstrategy, social, timemanagement, instructing, coordination, pursuasion, criticalthinking, negotiating, service, listening, monitoring, problemsolving, learning, decisionmaking):
```

Enter one or more soft skills (input), such as:
```
instructing, listening, problemsolving
```

The script will analyze your selected soft skills and provide you a list of recommended occupations to pursue (output).
```
ecommended Careers:
+---------------------------------------------------------------+------+---------------------+
|                           Occupation                          | Code | Avg. Skills Covered |
+---------------------------------------------------------------+------+---------------------+
|               Chemistry Teachers, Postsecondary               | None |         0.00        |
|                     Mechatronics Engineers                    | None |         0.00        |
|                         Sales Managers                        | None |         0.00        |
|                  Forensic Science Technicians                 | None |         0.00        |
| Administrative Law Judges, Adjudicators, and Hearing Officers | None |         0.00        |
|                Obstetricians and Gynecologists                | None |         0.00        |
|                  Biofuels Production Managers                 | None |         0.00        |
|                      Mechanical Drafters                      | None |         0.00        |
|                       Robotics Engineers                      | None |         0.00        |
|            Library Science Teachers, Postsecondary            | None |         0.00        |
+---------------------------------------------------------------+------+---------------------+
```



## Repository content

The following files are part of this repository:

- `skills.py`  
The code for this program.
- `skills-list.csv`  
CSV file with a list of skills and their codes.
- `data`
-- coordination.csv

## Assignment 4: Dependency Management Write-Up
As I (Ken Nelson) have stated in the past, I cannot stand python as a language. The tools are horrible, pip being a prime example. That said
we used to pip to assist in creating the requirements.txt file, although we are not certain that it accurately reflected the projects
dependencies. We had to manually enter a number of dependencies that the pip freeze command missed. We also added a dependencies.txt file
to list all the dependency versions, although we feel that is inadequate as well. In reading some online forums, pip freeze is not seen
as a good solution to use (read: https://medium.com/@tomagee/pip-freeze-requirements-txt-considered-harmful-f0bce66cf895).


## License Selection
We are applying the MIT license for a collaborative, open-source environment. This will make the project freely available to anyone to use, modify, or distribute the code. This encourages contributions and ensures the software can be used in both personal and commercial projects without restrictions.
