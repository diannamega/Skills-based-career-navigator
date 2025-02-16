import unittest
import pandas as pd
import os
from unittest.mock import patch, mock_open
from skills import load_and_preprocess_data  # Import the function

class TestLoadAndPreprocessData(unittest.TestCase):

    @patch("os.listdir")
    @patch("pandas.read_csv")
    def test_load_and_preprocess_data_success(self, mock_read_csv, mock_listdir):
        # Mock the listdir to return filenames
        mock_listdir.return_value = ["test_skill.csv"]

        # Mock the pandas read_csv function
        mock_read_csv.return_value = pd.DataFrame({"Skills Covered": ["50%"], "Occupation": ["Test Occupation"], "Code": ["123"]})

        # Call the function
        data, soft_skills_list = load_and_preprocess_data("dummy_dir")

        # Assert that the functions were called
        mock_read_csv.assert_called_once()
        mock_listdir.assert_called_once_with("dummy_dir")

        # Assert the return values
        self.assertEqual(soft_skills_list, ["test_skill"])
        self.assertIsInstance(data["test_skill"], pd.DataFrame)
        self.assertEqual(data["test_skill"]["Skills Covered"].iloc[0], 0.5)

    @patch("os.listdir")
    def test_load_and_preprocess_data_filenotfound(self, mock_listdir):
        # Mock the listdir to raise a FileNotFoundError
        mock_listdir.side_effect = FileNotFoundError("Directory not found")

        # Call the function
        data, soft_skills_list = load_and_preprocess_data("dummy_dir")

        # Assert that the functions were called
        # mock_read_csv.assert_not_called()
        mock_listdir.assert_called_once_with("dummy_dir")

        # Assert the return values
        self.assertIsNone(data)
        self.assertIsNone(soft_skills_list)

    @patch("os.listdir")
    @patch("pandas.read_csv")
    def test_load_and_preprocess_data_invalid_csv(self, mock_read_csv, mock_listdir):
        # Mock listdir
        mock_listdir.return_value = ["bad_file.csv"]

        # Make read_csv raise an Exception
        mock_read_csv.side_effect = Exception("Failed to parse CSV")

        # Call the function
        data, soft_skills_list = load_and_preprocess_data("dummy_dir")

        # Check results
        self.assertIsNone(data)
        self.assertIsNone(soft_skills_list)

if __name__ == '__main__':
    unittest.main()