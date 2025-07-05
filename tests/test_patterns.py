import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.triangle_generator import generate_pascals_triangle
from src.pattern_analyzer import analyze_row_sums, analyze_fibonacci, analyze_sierpinski_pattern

class TestPatternAnalysis(unittest.TestCase):
    def setUp(self):
        self.triangle = generate_pascals_triangle(6)
        self.max_fib_rows = 5  # Limit for Fibonacci test

    def test_row_sums_output(self):
        expected_output = [
            "Row 1: 1 = 2^0 (1)",
            "Row 2: 2 = 2^1 (2)",
            "Row 6: 32 = 2^5 (32)"