from unittest import TestCase
from src.factorial import iterative_factorial, recursive_factorial


class TestFactorial(TestCase):
    def test_simple_ite_factorial(self):
        self.assertEqual(iterative_factorial(5), 120)
        self.assertEqual(iterative_factorial(7), 5040)
        self.assertEqual(iterative_factorial(14), 87178291200)

    def test_simple_rec_factorial(self):
        self.assertEqual(recursive_factorial(5), 120)
        self.assertEqual(recursive_factorial(7), 5040)
        self.assertEqual(recursive_factorial(14), 87178291200)

    def test_edge_cases_ite_factorial(self):
        self.assertEqual(iterative_factorial(0), 1)
        with self.assertRaises(ValueError):
            iterative_factorial(-1)
        with self.assertRaises(ValueError):
            iterative_factorial(-5)
        with self.assertRaises(TypeError):
            iterative_factorial(5.5)
        with self.assertRaises(TypeError):
            iterative_factorial("test")
        with self.assertRaises(TypeError):
            iterative_factorial(None)

    def test_edge_cases_rec_factorial(self):
        self.assertEqual(recursive_factorial(0), 1)
        with self.assertRaises(ValueError):
            recursive_factorial(-1)
        with self.assertRaises(ValueError):
            recursive_factorial(-5)
        with self.assertRaises(TypeError):
            recursive_factorial(5.5)
        with self.assertRaises(TypeError):
            recursive_factorial("test")
        with self.assertRaises(TypeError):
            recursive_factorial(None)
