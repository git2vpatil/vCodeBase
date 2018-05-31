import unittest
import logging
from source_code.source_code import fact, divTen
import sys
import time

class testFactorial(unittest.TestCase):
    """
    Our basic test class
    """
    def setUp(self):
        logging.info("*"*20+ "\n")
        logging.info("running Setup \n")

    def tearDown(self):
        logging.info("running teardown \n")

    def test_fact(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        logging.info("Test 1")
        res = fact(5)
        self.assertEqual(res, 120)

    def test_div_exception(self):
        """
        To test exception raise due to run time error
        """
        logging.info("Test 2")
        self.assertRaises(ZeroDivisionError, divTen, 0)

    @unittest.skip("Skiping this test for demo") 
    def test_skipTest_demo(self):
        """
        Skip test demo
        """
        logging.info("Test 3")
        self.assertEqual(4, 4)

    @unittest.skipIf('win' in sys.platform, "Skip if Windows")
    def test_skip_if_windows(self):
        """
        Ignore this test on windows platform
        """
        logging.info("Test 4")
        self.assertIn('/usr/lib/python2.7', sys.path, "Python not configured")

    @unittest.skipUnless('win' in sys.platform, "Run only on Windows")
    def test_run_only_on_windows(self):
        """
        Run only on windows platform
        """
        logging.info("Test 5")
        self.assertIn('C:\\Python27', sys.path)
 
    @unittest.expectedFailure
    def test_expected_failure(self):
        """
        Run only on windows platform
        """
        logging.info("Test 6")  
        self.assertEqual(3, divTen(5), "Just an example.. please dont try to find logic in its")


    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename =r'C:\Users\jpi1\Documents\DemoLogs\test{}.log'.format(int(time.time())), level = logging.DEBUG, format='%(message)s')
        logging.info("Before class")

    @classmethod
    def tearDownClass(cls):
        logging.info("*"*20+ "\n")
        logging.info("After class")


if __name__ == '__main__':
    unittest.main()