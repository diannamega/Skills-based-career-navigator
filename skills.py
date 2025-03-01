import pandas as pd
import networkx as nx
import os
from prettytable import PrettyTable

def load_and_preprocess_data(data_dir):
    """
        Loads and preprocesses CSV files from a specified directory, extracting skill names
        and cleaning the 'Skills Covered' column to be a numeric representation.
        Args:
            data_dir (str): The path to the directory containing the CSV files.
        Returns:
            tuple: A tuple containing:
                - data (dict): A dictionary where keys are skill names (extracted from filenames)
                            and values are pandas DataFrames representing the CSV data.
                            Returns None if any file loading fails.
                - soft_skills_list (list): A list of skill names (strings) extracted from the CSV filenames.
                                Returns None if any file loading fails.
        [dmega]
    """
    #   Loads and preprocesses the CSV files from the specified directory.
    data = {}
    soft_skills_list = []
    try:
        for filename in os.listdir(data_dir):
            if filename.endswith(".csv"):
                # Remove ".csv" to get skill name
                # The skill name is the filename without the extension
                #[dmega]
                skill_name = filename[:-4]
                filepath = os.path.join(data_dir, filename)
                df = pd.read_csv(filepath)

                # Clean the Skills Covered, and convert it to a numeric
                df['Skills Covered'] = df['Skills Covered'].astype(str).str.replace('%', '', regex=False).astype(float) / 100
                data[skill_name] = df
                soft_skills_list.append(skill_name)
    except FileNotFoundError:
        print(f"Error: Directory not found: {data_dir}")
        return None, None
    except Exception as e:
        print(f"Error loading data from {data_dir}: {e}")
        return None, None

    # Return the data dictionary and the list of soft skills
    # See comment above for the return format
    # [dmega]
    return data, soft_skills_list

def create_career_network(data):
    """
        Creates a career network graph linking occupations based on shared codes.

        The graph represents occupations as nodes, with edges connecting occupations that share a code,
        and stores the associated skills as a node attribute.
        Args:
            data (dict): A dictionary where keys are skill names and values are pandas DataFrames,
                        containing 'Occupation' and 'Code' columns.
        Returns:
            nx.Graph: A networkx graph where:
                - Nodes represent occupations.
                - Edges connect occupations that share a code.
                - Each node has a 'skills' attribute: a list of skills associated with the occupation.
        [dmega]
    """

    # Creates a career network graph, linking Occupations based on shared skills.
    G = nx.Graph()

    # 1. Add nodes for each unique occupation (using Occupation as the node identifier)
    #    This ensures each occupation is represented in the graph, even if it doesn't share a code with others.
    # [dmega]
    all_occupations = set()
    for skill, skill_df in data.items():
        # Use union() for efficiency for speed when creating a large set.
        # Change suggestion from JDamerow.
        all_occupations = all_occupations.union(list(skill_df['Occupation'].unique()))

    for occupation in all_occupations:
        G.add_node(occupation)

    # 2. Add edges between Occupations sharing a Code
    #    This is the core logic for creating the network structure.  It iterates through all
    #    skills and connects occupations that share a code, creating an edge between them.
    # [dmega] Remove the loop in line 105.
    # In the second loop after that (line 113) add an if before line 116 that checks if  G.nodes[occupation]['skills'] is already initialized and if not, set it to empty list.
    # [kdnelso7]
    for skill, skill_df in data.items():
        # Group by Code within the same skill to find occupations sharing a code
        code_groups = skill_df.groupby('Code')['Occupation'].apply(list)
        for code, occupations in code_groups.items():
            # Create edges between all pairs of occupations sharing this code
            for i in range(len(occupations)):
                for j in range(i + 1, len(occupations)):
                    occ1 = occupations[i]
                    occ2 = occupations[j]
                    if occ1 in G.nodes() and occ2 in G.nodes():
                        if not G.has_edge(occ1, occ2):
                            G.add_edge(occ1, occ2)

        # Populate the 'skills' attribute for each occupation (AFTER creating edges)
        #Append each skill to the dataframe.
        for occupation in skill_df['Occupation'].unique():
            if occupation in G.nodes():
              if 'skills' not in G.nodes[occupation]: #Check for the node and create it if it doesn't exist
                G.nodes[occupation]['skills'] = []
              G.nodes[occupation]['skills'].append(skill) # append the skill to create the list

    return G

def calculate_overall_match(G, user_skills, data):
    """
        Calculates overall match scores for each occupation based on user-provided skills and Skills Covered values.

        This function iterates through each occupation in the graph, calculates a weighted score
        based on the user's selected skills and the corresponding Skills Covered values,
        and then ranks the occupations based on these scores.
        Args:
            G (nx.Graph): The career network graph.
            user_skills (list): A list of soft skills provided by the user.
            data (dict): A dictionary where keys are skill names and values are pandas DataFrames,
                        containing 'Occupation', 'Code', and 'Skills Covered' columns.
        Returns:
            list: A list of tuples, where each tuple contains:
                - occupation (str): The name of the occupation.
                - (average_weighted_score, code_value) (tuple):
                    - average_weighted_score (float): The calculated average weighted score for the occupation.
                    - code_value (str): The code associated with the occupation (taken from the first matching skill).
            The list is sorted in descending order based on the average weighted score.
        [kdnelso7]
    """

    # {occupation: (weighted score, code)}
    occupation_scores = {}

    # Collect relevant Skills Covered values, considering only user-specified skills:
    # Iterates through each user-provided skill and, if the occupation is associated with that skill
    # in the loaded data, retrieves the Skills Covered value. If the occupation does not have
    # a Skills Covered value for a given skill, a default value of 0 is used to handle missing data.
    # [kdnelso7]
    for occupation in G.nodes():
        skill_values = []
        code_value = None

        # Iterate through each skill provided by the user to find the Skills Covered value for the current occupation.
        # [kdnelso7]
        for skill in user_skills:
            if skill in data:
                #Get the skill data frame
                skill_df = data[skill]
                if occupation in skill_df['Occupation'].values:
                    skill_row = skill_df[skill_df['Occupation'] == occupation].iloc[0]
                    skills_covered = skill_row['Skills Covered']
                    skill_values.append(skills_covered)
                    code = skill_row['Code']
                    if code_value is None:
                        code_value = code
                else:
                    skill_values.append(0)

        # Calculate the average score for the occupation based on the user-provided skills.
        # If no Skills Covered values are found, the average is set to 0.
        # [kdnelso7]
        average_weighted_score = sum(skill_values) / len(skill_values) if skill_values else 0
        occupation_scores[occupation] = (average_weighted_score, code_value)

    # Sort the occupations based on the average weighted score in descending order.
    ranked_careers = sorted(occupation_scores.items(), key=lambda item: item[1][0], reverse=True)

    return ranked_careers

def recommend_careers(ranked_careers, num_recommendations=10):
    """
        Recommends the top N careers from a ranked list, based on their overall match scores.

        This function takes a list of ranked careers (occupation, score, code) and returns a list
        containing the top N careers, where N is determined by the 'num_recommendations' parameter.
        If the input list is empty, it prints a message and returns an empty list.
        Args:
            ranked_careers (list): A list of tuples, where each tuple contains:
                - career (str): The name of the occupation.
                - (score, code) (tuple):
                    - score (float): The average weighted score for the occupation.
                    - code (str): The code associated with the occupation.
            num_recommendations (int): The number of top careers to recommend (default is 10).
        Returns:
            list: A list of tuples, where each tuple contains:
                - career (str): The name of the occupation.
                - (score, code) (tuple):
                    - score (float): The average weighted score for the occupation.
                    - code (str): The code associated with the occupation.
            The list contains at most 'num_recommendations' elements.
        [kdnelso7]
    """
    if not ranked_careers:
        print("No careers to recommend. Check input data.")
        return []

    top_careers = []
    for career, (score, code)  in ranked_careers[:num_recommendations]: #CHANGED: Now parsing score and code
        top_careers.append((career, score, code))
    return top_careers

def main():
    """
        Drives the career recommendation process by orchestrating data loading, network creation,
        skill matching, and presentation of results.

        This function performs the following steps:
        1. Loads and preprocesses data from CSV files in a specified directory.
        2. Creates a career network graph based on shared codes.
        3. Prompts the user to enter their soft skills.
        4. Validates the user's input against the available skills.
        5. Calculates overall match scores for each occupation based on the user's skills.
        6. Recommends the top careers based on the calculated scores.
        7. Presents the results in a formatted table.
        [kdnelso7]
    """
    data_dir = "data/softskills"
    data, soft_skills_list = load_and_preprocess_data(data_dir)

    if data is None:
        print("Failed to load data. Exiting.")
        return

    G = create_career_network(data)

    print("Number of nodes:", G.number_of_nodes())
    print("Number of edges:", G.number_of_edges())

    # Get user input for skills
    print(f"Enter your soft skills (comma-separated, e.g., {', '.join(soft_skills_list)}):")
    user_skills_input = input()
    user_skills = [skill.strip() for skill in user_skills_input.split(",")]

    # Validate user skills, remove the skill if it isn't a valid one.
    valid_skills = soft_skills_list
    user_skills = [skill for skill in user_skills if skill in valid_skills]

    ranked_careers = calculate_overall_match(G, user_skills, data)

    if not ranked_careers:
        print("No matching careers found.")
        return

    recommended_careers = recommend_careers(ranked_careers)

    # Create a PrettyTable object
    table = PrettyTable()
    table.field_names = ["Occupation", "Code", "Avg. Skills Covered"]

    # Add data rows to the table
    for career, score, code in recommended_careers:
        table.add_row([career, code, f"{score:.2f}"])

    # Print the table
    print("\nRecommended Careers:")
    print(table)

if __name__ == "__main__":
    main()