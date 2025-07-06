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
        ]
        
        with StringIO() as buf, redirect_stdout(buf):
            analyze_row_sums(self.triangle)
            output = buf.getvalue()
            
        for expected in expected_output:
            self.assertIn(expected, output)

    def test_fibonacci_sequence(self):
        expected_fib = [1, 1, 2, 3, 5]
        
        with StringIO() as buf, redirect_stdout(buf):
            analyze_fibonacci(self.triangle, self.max_fib_rows)
            output = buf.getvalue()
            
        self.assertIn("Fibonacci numbers from shallow diagonals:", output)
        for num in expected_fib:
            self.assertIn(str(num), output)

    def test_sierpinski_pattern_output(self):
        expected_phrases = [
            "Sierpinski Triangle Pattern",
            "coloring odd numbers",
            "Sierpinski fractal"
        ]
        
        with StringIO() as buf, redirect_stdout(buf):
            analyze_sierpinski_pattern(self.triangle)
            output = buf.getvalue()
            
        for phrase in expected_phrases:
            self.assertIn(phrase, output)

if __name__ == '__main__':
    unittest.main()