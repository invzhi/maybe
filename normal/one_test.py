import unittest

from normal.one import statistics, msn


class TestStatistics(unittest.TestCase):

    def test_statistics1(self):
        samples = [99.3, 98.7, 100.5, 101.2, 98.3, 99.7, 99.5, 102.1, 100.5]
        mean, std, n = msn(samples)
        v, p = statistics(mu=100, sigma=1.2, mean=mean, std=std, n=n)
        self.assertAlmostEqual(v, -0.0556, places=4)
        self.assertAlmostEqual(p, 0.9557, places=4)

    def test_statistics2(self):
        samples = [100.36, 100.31, 99.99, 100.11, 100.64, 100.85, 99.42, 99.91, 99.35, 100.10]
        mean, std, n = msn(samples)
        v, p = statistics(mu=100, sigma=0.5, mean=mean, std=std, n=n)
        self.assertAlmostEqual(v, 0.6578, places=4)
        self.assertEqual(p, 0.51069637568085)
        v, p = statistics(mu=100, sigma=None, mean=mean, std=std, n=n)
        self.assertEqual(v, 0.7283527538257837)
        self.assertEqual(p, 0.4849162263796869)

    def test_statistics3(self):
        v, p = statistics(mu=70, sigma=None, mean=66.5, std=15, n=36)
        self.assertEqual(v, -1.4)
        self.assertAlmostEqual(p, 0.1703, places=4)

    def test_statistics4(self):
        samples = [1.32, 1.55, 1.36, 1.40, 1.44]
        mean, std, n = msn(samples)
        v, p = statistics(mu=None, sigma=0.048, mean=mean, std=std, n=n)
        self.assertEqual(v, 10.805555555555552)
        self.assertEqual(p, 0.02883844593410758)
