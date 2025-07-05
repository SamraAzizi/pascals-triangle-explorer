import unittest
from src.triangle_generator import generate_pascals_triangle

class TestTriangleGenerator(unittest.TestCase):
    def test_triangle_generation_basic(self):
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
        self.assertEqual(generate_pascals_triangle(5), expected)

    def test_single_row(self):
        self.assertEqual(generate_pascals_triangle(1), [[1]])

    def test_empty_triangle(self):
        self.assertEqual(generate_pascals_triangle(0), [])
