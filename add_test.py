import unittest
from add import addition


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        d = addition(3, 8)
        d = str(d)
        self.assertEqual(d, '11')
