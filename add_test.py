import unittest
from add import addition


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        d = addition(3, 8)
        d = str(d)
        print("Hello")
        self.assertEqual(d, '11')


if __name__ == '__main__':
    unittest.main()
