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

        with StringIO() as buf, redirect_stdout(buf):
            display_triangle(self.small_triangle)
            output = buf.getvalue().strip()
            
        self.assertEqual(output, expected)

    def test_display_colored_output_contains_numbers(self):
        with StringIO() as buf, redirect_stdout(buf):
            display_colored_triangle(self.small_triangle)
            output = buf.getvalue()
            
        self.assertIn("1", output)
        self.assertIn("2", output)
        self.assertIn(COLORS['blue'], output)  # Even number color
        self.assertIn(COLORS['yellow'], output)  # Odd number color

        def test_display_colored_legend(self):
        expected_legend = [
            f"{COLORS['yellow']}Yellow: Odd numbers",
            f"{COLORS['blue']}Blue: Even numbers"
        ]
        
        with StringIO() as buf, redirect_stdout(buf):
            display_colored_triangle(self.large_triangle)
            output = buf.getvalue()
            
        for legend_item in expected_legend:
            self.assertIn(legend_item, output)

    def test_center_alignment_large_triangle(self):
        with StringIO() as buf, redirect_stdout(buf):