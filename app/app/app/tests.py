from django.test import TestCase
from .calc import add, sub, divide


class CalcTest(TestCase):

    def test_add_numbers(self):
        """Test the function to add two numbers"""
        self.assertEqual(add(2, 3), 5)

    def test_sub_numbers(self):
        """Test to subtract two numbers"""
        self.assertEqual(sub(5, 3), 2)

    def test_divide_numbers(self):
        self.assertEqual(divide(4, 2), 2)
