import pandas as pd
import networkx as nx
import os
from prettytable import PrettyTable

def load_and_preprocess_data(data_dir):
    #   Loads and preprocesses the CSV files from the specified directory.
    data = {}
    soft_skills_list = []
    try:
        for filename in os.listdir(data_dir):
            if filename.endswith(".csv"):
                skill_name = filename[:-4]  # Remove ".csv" to get skill name
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

    return data, soft_skills_list

def create_career_network(data):
    # Creates a career network graph, linking Occupations based on shared skills.    
    G = nx.Graph()

    # 1. Add nodes for each unique occupation (using Occupation as the node identifier)
    all_occupations = set()
    for skill_df in data.values():
        for occupation in skill_df['Occupation'].unique():
            all_occupations.add(occupation)

    for occupation in all_occupations:
        G.add_node(occupation)  # Add the occupation if it is new

    # 2. Add edges between Occupations sharing a Code
    for skill, skill_df in data.items():
      #For each CSV file
        for index, row in skill_df.iterrows():
            #For each row in a single CSV File
            occupation = row['Occupation']
            code = row['Code']

            # Find other occupations with the same code
            for other_skill, other_skill_df in data.items():
                for other_index, other_row in other_skill_df.iterrows():
                    if row is not other_row:
                        other_occupation = other_row['Occupation']
                        other_code = other_row['Code']
                        #Connect the ones that share a code and has an edge!
                        if (code == other_code) and (occupation in G.nodes() and other_occupation in G.nodes()):
                            if not G.has_edge(occupation, other_occupation):
                                G.add_edge(occupation, other_occupation)

    # 3. Populate the 'skills' attribute for each occupation (AFTER creating edges)
    for skill, skill_df in data.items():
        for occupation in skill_df['Occupation'].unique():
            if occupation in G.nodes():
                G.nodes[occupation]['skills'] = []

    #Now update it!
    for skill, skill_df in data.items():
        for occupation in skill_df['Occupation'].unique():
            if occupation in G.nodes():
                G.nodes[occupation]['skills'].append(skill)
    return G

def calculate_overall_match(G, user_skills, data):
    #   Calculate overall match scores based on the created network and Skills Covered.
    occupation_scores = {} # {occupation: (weighted score, code)}
    for occupation in G.nodes():
        # 1. Collect Skills Covered values across ALL specified skills
        skill_values = []
        code_value = None  # Store code

        for skill in user_skills:
            if skill in data:
                skill_df = data[skill] #Get the skill data frame
                if occupation in skill_df['Occupation'].values:
                    skill_row = skill_df[skill_df['Occupation'] == occupation].iloc[0] #Get row
                    skills_covered = skill_row['Skills Covered'] #Skills Covered.
                    skill_values.append(skills_covered)
                    code = skill_row['Code']
                    if code_value is None: #Setting the code to something
                      code_value = code
                else:
                    skill_values.append(0)  # Assign zero if skill not found

        # 2. Calculate the average
        average_weighted_score = sum(skill_values) / len(skill_values) if skill_values else 0
        occupation_scores[occupation] = (average_weighted_score, code_value)

    #Sorting by Weighted Score:
    ranked_careers = sorted(occupation_scores.items(), key=lambda item: item[1][0], reverse=True)

    return ranked_careers

def recommend_careers(ranked_careers, num_recommendations=10):
    #   Recommends the top N careers based on the overall match scores.
    if not ranked_careers:
        print("No careers to recommend. Check input data.")
        return []

    top_careers = []
    for career, (score, code)  in ranked_careers[:num_recommendations]: #CHANGED: Now parsing score and code

        top_careers.append((career, score, code))
    return top_careers


def main():
    #   Main function to drive the career recommendation process.
    data_dir = "data/softskills"  # Specify the directory
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

main()