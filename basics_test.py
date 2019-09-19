import unittest
import get_column_stats as gcs
import numpy as np

class TestStdDev(unittest.TestCase):
    def test_mean_const(self):
        self.assertEqual(gcs.calc_stdev([1, 1, 1, 1, 1, 1]), 0)
        
    def test_mean_random(self):
        exp_std = np.random.uniform(0, 100)
        dist = np.random.normal(loc = 0, scale = exp_std, size = 200000).tolist()
        self.assertAlmostEqual(gcs.calc_stdev(dist), exp_std, places=0)

    def test_mean_empty_error(self):
        self.assertRaises(TypeError, gcs.calc_stdev)

    def test_mean_null_list_error(self):
        self.assertRaises(IndexError, gcs.calc_stdev, [])

    def test_mean_str_list_error(self):
        self.assertRaises(TypeError, gcs.calc_stdev, ['string', 'string'])