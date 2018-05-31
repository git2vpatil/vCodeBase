import unittest
from source_code.source_code import is_prime


class testPrime(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_number_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_number_not_prime(self):
        """Is 6 successfully determined not prime?"""
        self.assertFalse(is_prime(6))

    def test_zero_or_one_not_prime(self):
        """ 0 or 1 not prime"""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1), "1 is not prime number")

    def test_negative_num_not_prime(self):
        """negative number correctly determined not to be prime?"""
        self.assertFalse(is_prime(-5), "-5 should be determined as not prime")


if __name__ == '__main__':
    unittest.main()