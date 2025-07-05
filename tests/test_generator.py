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

    def test_large_triangle(self):
        triangle = generate_pascals_triangle(10)
        self.assertEqual(len(triangle), 10)
        self.assertEqual(triangle[-1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1])

    def test_row_symmetry(self):
        triangle = generate_pascals_triangle(7)
        for row in triangle:
            self.assertEqual(row, row[::-1])  # Each row should be symmetric

if __name__ == '__main__':
    unittest.main()