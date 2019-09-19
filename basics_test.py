import unittest
import get_column_stats as gcs
import numpy as np


class TestStdDev(unittest.TestCase):
    def test_stdev_const(self):
        self.assertEqual(gcs.calc_stdev([1, 1, 1, 1, 1, 1]), 0)

    def test_stdev_random(self):
        exp_std = np.random.uniform(0, 100)
        dist = np.random.normal(loc=0, scale=exp_std, size=200000).tolist()
        self.assertAlmostEqual(gcs.calc_stdev(dist), exp_std, places=0)

    def test_stdev_empty_error(self):
        self.assertRaises(TypeError, gcs.calc_stdev)

    def test_stdev_null_list_error(self):
        self.assertRaises(IndexError, gcs.calc_stdev, [])

    def test_stdev_incorect_type(self):
        self.assertRaises(TypeError, gcs.calc_stdev, 'string')
        self.assertRaises(TypeError, gcs.calc_stdev, 1)
        self.assertRaises(TypeError, gcs.calc_stdev, 1.00+4j)

    def test_stdev_str_list_error(self):
        self.assertRaises(TypeError, gcs.calc_stdev, ['string', 'string'])
        self.assertRaises(TypeError, gcs.calc_stdev, [1, 1, 1, 1, 'string'])


class TestMean(unittest.TestCase):
    def test_mean_const(self):
        self.assertEqual(gcs.calc_mean([1, 1, 1, 1, 1, 1, 1]), 1)
        self.assertEqual(gcs.calc_mean(list(range(1000))), 499.5)

    def test_mean_random(self):
        exp_mean = np.random.uniform(0, 100)
        dist = np.random.normal(loc=exp_mean, scale=1, size=10000).tolist()
        self.assertAlmostEqual(gcs.calc_mean(dist), exp_mean, places=1)

    def test_mean_empty_error(self):
        self.assertRaises(TypeError, gcs.calc_mean)

    def test_mean_null_list_error(self):
        self.assertRaises(TypeError, gcs.calc_mean, 'string')
        self.assertRaises(TypeError, gcs.calc_mean, 1)
        self.assertRaises(TypeError, gcs.calc_mean, 1.00+4j)

    def test_mean_str_list_error(self):
        self.assertRaises(TypeError, gcs.calc_mean, ['string', 'string'])
