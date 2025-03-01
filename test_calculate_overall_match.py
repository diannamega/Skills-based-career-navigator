import unittest
from skills import calculate_overall_match  # Import the function

class TestCalculateOverallMatch(unittest.TestCase):
    def test_calculate_overall_match_simple(self):
        # Create a simple graph
        G = nx.Graph()
        G.add_node("Occ1", skills=["skill1", "skill2"])
        G.add_node("Occ2", skills=["skill2", "skill3"])
        G.add_node("Occ3", skills=["skill1"])

        # Mock data
        mock_data = {
            "skill1": pd.DataFrame({"Occupation": ["Occ1"], "Code": ["1"], "Skills Covered": [0.5]}),
            "skill2": pd.DataFrame({"Occupation": ["Occ2"], "Code": ["2"], "Skills Covered": [0.7]}),
            "skill3": pd.DataFrame({"Occupation": ["Occ3"], "Code": ["3"], "Skills Covered": [0.9]})
        }

        # User skills
        user_skills = ["skill1", "skill2"]

        # Call the function
        ranked_careers = calculate_overall_match(G, user_skills, mock_data)

        # Assert the return value
        self.assertIsInstance(ranked_careers, list)

        # Assert the number of recommendations
        #self.assertEqual(len(ranked_careers), 3)
        self.assertEqual(len(ranked_careers), 3)
        # Basic assert check, but it's not entirely accurate.
        # The values can differ from your expected order.

    def test_calculate_overall_match_no_skills(self):
        # Create a simple graph
        G = nx.Graph()
        G.add_node("Occ1", skills=[])
        G.add_node("Occ2", skills=[])

        # Mock data
        mock_data = {}

        # User skills
        user_skills = []

        # Call the function
        ranked_careers = calculate_overall_match(G, user_skills, mock_data)

        # Assert the return value
        self.assertIsInstance(ranked_careers, list)
        self.assertEqual(len(ranked_careers), 2) # All occupations, but 0 scores

    def test_calculate_overall_match_no_matching_skills(self):
        # Create a simple graph
        G = nx.Graph()
        G.add_node("Occ1", skills=["skill1"])
        G.add_node("Occ2", skills=["skill2"])

        # Mock data
        mock_data = {
            "skill3": pd.DataFrame({"Occupation": ["Occ1"], "Code": ["1"], "Skills Covered": [0.5]}),
            "skill4": pd.DataFrame({"Occupation": ["Occ2"], "Code": ["2"], "Skills Covered": [0.7]})
        }
        # User skills
        user_skills = ["skill5", "skill6"]

        # Call the function
        ranked_careers = calculate_overall_match(G, user_skills, mock_data)

        # Assert the return value
        self.assertIsInstance(ranked_careers, list)
        self.assertEqual(len(ranked_careers), 2) #All occupations, but 0 scores

if __name__ == '__main__':
    import networkx as nx #This is a MUST, it has to import networkx
    unittest.main()