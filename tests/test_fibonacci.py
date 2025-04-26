from unittest import TestCase
from src.fibonacci import iterative_fibonacci, recursive_fibonacci


class TestFibonacci(TestCase):
    def test_simple_ite_fibonacci(self):
        self.assertEqual(iterative_fibonacci(1), 0)
        self.assertEqual(iterative_fibonacci(5), 3)
        self.assertEqual(iterative_fibonacci(10), 34)
        self.assertEqual(iterative_fibonacci(10), 34)
        self.assertEqual(iterative_fibonacci(20), 4181)

    def test_simple_rec_fibonacci(self):
        self.assertEqual(recursive_fibonacci(1), 0)
        self.assertEqual(recursive_fibonacci(5), 3)
        self.assertEqual(recursive_fibonacci(10), 34)
        self.assertEqual(recursive_fibonacci(10), 34)
        self.assertEqual(recursive_fibonacci(20), 4181)

    def test_edge_cases_ite_fibonacci(self):
        with self.assertRaises(ValueError):
            iterative_fibonacci(0)
        with self.assertRaises(ValueError):
            iterative_fibonacci(-1)
        with self.assertRaises(ValueError):
            iterative_fibonacci(-5)
        with self.assertRaises(TypeError):
            iterative_fibonacci(5.5)
        with self.assertRaises(TypeError):
            iterative_fibonacci("test")
        with self.assertRaises(TypeError):
            iterative_fibonacci(None)

    def test_edge_cases_rec_fibonacci(self):
        with self.assertRaises(ValueError):
            recursive_fibonacci(0)
        with self.assertRaises(ValueError):
            recursive_fibonacci(-1)
        with self.assertRaises(ValueError):
            recursive_fibonacci(-5)
        with self.assertRaises(TypeError):
            recursive_fibonacci(5.5)
        with self.assertRaises(TypeError):
            recursive_fibonacci("test")
        with self.assertRaises(TypeError):
            recursive_fibonacci(None)
