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
        expected_tour = (0, 2, 1, 4, 3)
        expected_cost = 19
        tour, cost = compute_tsp(distances)
        self.assertEqual(tour, expected_tour)
        self.assertEqual(cost, expected_cost)

if __name__ == '__main__':
    unittest.main()
