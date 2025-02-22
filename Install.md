# Installation Instructions

Follow the following steps to install and run the software:

## Clone the repository
First, clone this repository to your local machine using git:

git clone https://github.com/diannamega/Skills-based-career-navigator/
cd Skills-based-career-navigator

## Set up a virtual environment (Recommended)
To ensure all dependencies are installed in an isolated environment, it's recommended to use a virtual environment. You can set one up by following these steps:

On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

On Windows:
python -m venv venv
.\venv\Scripts\activate

## Install dependencies
Once your virtual environment is activated, you can install the necessary dependencies using pip. This project requires the following dependencies:

pandas==2.2.3
networkx==3.3
prettytable==3.14.0

To install these dependencies, run the following command:
pip install -r requirements.txt

## Additional Setup
Please check the repository documentation for the datasets that need to be downloaded.

## Running the code
Once you have installed the necessary dependencies, you can run the code as follows:

python skills.py
