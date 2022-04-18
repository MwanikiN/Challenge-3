import unittest
from array_size import arr_size

class TestArraySize (unittest.TestCase):
    def test_array_size(self):
        self.assertEquals((4,12), arr_size())

if __name__ == "__main__":
    unittest.main()