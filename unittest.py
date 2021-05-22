import math
import unittest


class C4Test(unittest.TestCase):
    def test_sqrt(self):
        num = 25
        self.assertEqual(math.sqrt(25), 5, 'FAILURE')

    def testsquare(self):
        num = 7
        self.assertEqual(100, 10 * 10, 'FAILURE')

    def tesequality(self):
        self.assertEqual(2, 2, 'FAILURE')


if __name__ == '__main__':
    import xmlrunner

    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False)
