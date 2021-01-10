import unittest
from Tasks.b1_binary_search import binary_search


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.arr = [-20] + [i for i in range(100)] + [101] + [103]

    def test_existing(self):
        self.assertEqual(6, binary_search(5, self.arr), msg="Invalid index returned!")
        self.assertEqual(55, binary_search(54, self.arr), msg="Invalid index returned!")
        self.assertEqual(1, binary_search(2, [1, 2, 2, 2]), msg="You should return first occurrence from the array.")
        self.assertEqual(0, binary_search(2, [2, 2, 2, 2]), msg="You should return first occurrence from the array.")
        self.assertEqual(1, binary_search(2, [1, 2, 2, 3]), msg="You should return first occurrence from the array.")
        self.assertEqual(0, binary_search(1, [1, 2]), msg="You should return first occurrence from the array.")

    def test_missing(self):
        self.assertIsNone(binary_search(-1, self.arr),
                          msg="Answer should be None because element is not presented in the array")
        self.assertIsNone(binary_search(-10, self.arr),
                          msg="Answer should be None because element is not presented in the array")
        self.assertIsNone(binary_search(100, self.arr),
                          msg="Answer should be None because element is not presented in the array")
        self.assertIsNone(binary_search(102, self.arr),
                          msg="Answer should be None because element is not presented in the array")

    def test_borders(self):
        self.assertEqual(0, binary_search(-20, self.arr),
                         msg="First element is not found - maybe 'mid - 1' is missing?")
        self.assertEqual(102, binary_search(103, self.arr),
                         msg="Last element is not found - maybe 'mid + 1' is missing?")


if __name__ == '__main__':
    unittest.main()
