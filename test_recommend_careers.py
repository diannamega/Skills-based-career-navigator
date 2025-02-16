import unittest
from skills import recommend_careers  # Import the function

class TestRecommendCareers(unittest.TestCase):

    def test_recommend_careers_simple(self):
        print("Testing recommend_careers: test_recommend_careers_simple")
        ranked_careers = [("Occ1", (0.8, "123")), ("Occ2", (0.7, "456")), ("Occ3", (0.6, "789"))]
        top_careers = recommend_careers(ranked_careers, num_recommendations=2)
        self.assertEqual(top_careers, [("Occ1", 0.8, "123"), ("Occ2", 0.7, "456")])
        
    def test_recommend_careers_fewer_than_requested(self):
        print("Testing recommend_careers: test_recommend_careers_fewer_than_requested")
        ranked_careers = [("Occ1", (0.8, "123"))]
        top_careers = recommend_careers(ranked_careers, num_recommendations=3)
        self.assertEqual(top_careers, [("Occ1", 0.8, "123")])

    def test_recommend_careers_empty_list(self):
        print("Testing recommend_careers: test_recommend_careers_empty_list")
        ranked_careers = []
        top_careers = recommend_careers(ranked_careers, num_recommendations=5)
        self.assertEqual(top_careers, [])
        
if __name__ == '__main__':
    unittest.main()