
import unittest
from src.triangle_generator import generate_pascals_triangle
from src.pattern_analyzer import analyze_row_sums

class TestPatternAnalysis(unittest.TestCase):
    def setUp(self):
        self.triangle = generate_pascals_triangle(5)
    
    def test_row_sums(self):
        # Redirect print to capture output
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            analyze_row_sums(self.triangle)
        
        output = f.getvalue()
        self.assertIn("Row 1: 1 = 2^0 (1)", output)
        self.assertIn("Row 5: 16 = 2^4 (16)", output)

if __name__ == '__main__':
    unittest.main()