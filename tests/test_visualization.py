import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.triangle_generator import generate_pascals_triangle
from src.visualization import display_triangle, display_colored_triangle, COLORS

class TestVisualization(unittest.TestCase):
    def setUp(self):
        self.small_triangle = generate_pascals_triangle(3)
        self.large_triangle = generate_pascals_triangle(5)

    def test_display_triangle_output(self):
        expected = "  1  \n 1 1 \n1 2 1"