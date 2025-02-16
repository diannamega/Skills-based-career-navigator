import unittest
import pandas as pd
import networkx as nx
from skills import create_career_network  # Import the function

class TestCreateCareerNetwork(unittest.TestCase):

    def test_create_career_network_simple(self):
        # Create mock data
        mock_data = {
            "skill1": pd.DataFrame({"Occupation": ["Dancers"], "Code": ["27-2031.00"], "Skills Covered": [1]}),
            "skill2": pd.DataFrame({"Occupation": ["Stonemasons"], "Code": ["47-2022.00"], "Skills Covered": [1]}),
            "skill3": pd.DataFrame({"Occupation": ["Athletes and Sports Competitors"], "Code": ["27-2021.00"], "Skills Covered": [100]})
        }

        # Call the function
        G = create_career_network(mock_data)

        # Assert the return value
        self.assertIsInstance(G, nx.Graph)
        self.assertEqual(G.number_of_nodes(), 3)

    def test_create_career_network_no_shared_codes(self):
        # Mock data where occupations do not share codes
        mock_data = {
            "skill1": pd.DataFrame({"Occupation": ["Dancers"], "Code": ["27-2031.00"], "Skills Covered": [100]}),
            "skill2": pd.DataFrame({"Occupation": ["Stonemasons"], "Code": ["47-2022.00"], "Skills Covered": [100]}),
            "skill3": pd.DataFrame({"Occupation": ["Athletes and Sports Competitors"], "Code": ["27-2021.00"], "Skills Covered": [100]}),
            "skill4": pd.DataFrame({"Occupation": ["Carpenters"], "Code": ["47-2031.00"], "Skills Covered": [100]}),
            "skill5": pd.DataFrame({"Occupation": ["Helpers--Roofers"], "Code": ["47-3016.00"], "Skills Covered": [100]}),
            "skill6": pd.DataFrame({"Occupation": ["Highway Maintenance Workers"], "Code": ["47-4051.00"], "Skills Covered": [100]}),
            "skill7": pd.DataFrame({"Occupation": ["Manufactured Building and Mobile Home Installers"], "Code": ["49-9095.00"], "Skills Covered": [100]}),
            "skill8": pd.DataFrame({"Occupation": ["Millwrights"], "Code": ["49-9044.00"], "Skills Covered": [100]}),
            "skill9": pd.DataFrame({"Occupation": ["Roof Bolters, Mining"], "Code": ["47-5043.00"], "Skills Covered": [100]}),
            "skill10": pd.DataFrame({"Occupation": ["Roofers"], "Code": ["47-2181.00"], "Skills Covered": [100]})
        }

        # Call the function
        G = create_career_network(mock_data)

        print(G)
        # Assert the return value
        self.assertIsInstance(G, nx.Graph)
        self.assertEqual(G.number_of_nodes(), 10)
        # self.assertEqual(G.number_of_edges(), 0)  # No shared codes, so no edges

        # Check skills attribute for each occupation
        self.assertEqual(set(G.nodes["Dancers"]['skills']), {"skill1"})
        self.assertEqual(set(G.nodes["Stonemasons"]['skills']), {"skill2"})
        self.assertEqual(set(G.nodes["Athletes and Sports Competitors"]['skills']), {"skill3"})
        self.assertEqual(set(G.nodes["Carpenters"]['skills']), {"skill4"})
        self.assertEqual(set(G.nodes["Helpers--Roofers"]['skills']), {"skill5"})
        self.assertEqual(set(G.nodes["Highway Maintenance Workers"]['skills']), {"skill6"})
        self.assertEqual(set(G.nodes["Manufactured Building and Mobile Home Installers"]['skills']), {"skill7"})
        self.assertEqual(set(G.nodes["Millwrights"]['skills']), {"skill8"})
        self.assertEqual(set(G.nodes["Roof Bolters, Mining"]['skills']), {"skill9"})
        self.assertEqual(set(G.nodes["Roofers"]['skills']), {"skill10"})


    def test_create_career_network_empty_data(self):
        # Test with empty input data
        mock_data = {}

        # Call the function
        G = create_career_network(mock_data)

        # Assert the return value
        self.assertIsInstance(G, nx.Graph)
        self.assertEqual(G.number_of_nodes(), 0)
        self.assertEqual(G.number_of_edges(), 0)

if __name__ == '__main__':
    unittest.main()