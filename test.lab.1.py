import unittest
from lab_1 import array_monotonic

class Test(unittest.TestCase):

    def test_increasing(self):  # тест для зростаючого масиву
        self.assertTrue(array_monotonic([1, 2, 3, 4, 5]))

    def test_decreasing(self):  # тест для спадаючого масиву
        self.assertTrue(array_monotonic([5, 4, 3, 2, 1]))

    def test_not_monotonic(self):  # тест для не монотонного масиву
        self.assertFalse(array_monotonic([1, 2, 2, 3, 2, 4]))

if __name__ == '__main__':
    unittest.main()