import unittest

from answer import compute_tsp

class TestTSP(unittest.TestCase):

    def test_compute_tsp(self):
        # Test case with 5x5 distance matrix
        distances = [
            [0, 3, 4, 2, 7],
            [3, 0, 4, 6, 3],
            [4, 4, 0, 5, 8],
            [2, 6, 5, 0, 6],
            [7, 3, 8, 6, 0]
        ]
        expected_tour = [0, 3, 2, 1, 4]
        expected_cost = 21
        tour, cost = compute_tsp(distances)
        self.assertEqual(tour, expected_tour)
        self.assertEqual(cost, expected_cost)

    def test_compute_tsp_all_zero(self):
        # Test case with 5x5 distance matrix with all zeros
        distances = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_tour = [0, 1, 2, 3, 4]
        expected_cost = 0
        tour, cost = compute_tsp(distances)
        self.assertEqual(tour, expected_tour)
        self.assertEqual(cost, expected_cost)
        
    def test_compute_tsp_symmetric(self):
        # Test case with 5x5 symmetric distance matrix
        distances = [
            [0, 2, 3, 4, 5],
            [2, 0, 6, 7, 8],
            [3, 6, 0, 9, 10],
            [4, 7, 9, 0, 11],
            [5, 8, 10, 11, 0]
        ]
        expected_tour = [0, 1, 2, 3, 4]
        expected_cost = 33
        tour, cost = compute_tsp(distances)
        self.assertEqual(tour, expected_tour)
        self.assertEqual(cost, expected_cost)
    
if __name__ == '__main__':
    unittest.main()
