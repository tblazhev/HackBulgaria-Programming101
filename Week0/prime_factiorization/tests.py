import unittest
from solution import prime_factorization


class PrimFacTest(unittest.TestCase):
    def test_prime_factorization(self):
        res1 = [(2, 1), (5, 1)]
        res2 = [(2, 1), (7, 1)]
        res3 = [(2, 2), (89, 1)]
        res4 = [(89, 1)]
        res5 = [(2, 3), (5, 3)]

        self.assertEqual(res1, prime_factorization(10))
        self.assertEqual(res2, prime_factorization(14))
        self.assertEqual(res3, prime_factorization(356))
        self.assertEqual(res4, prime_factorization(89))
        self.assertEqual(res5, prime_factorization(1000))


if __name__ == '__main__':
    unittest.main()
