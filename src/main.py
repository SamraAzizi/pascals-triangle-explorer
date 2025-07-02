"""
Main entry point for Pascal's Triangle Explorer
"""

from triangle_generator import generate_pascals_triangle
from pattern_analyzer import analyze_patterns
from visualization import display_triangle

def main():
    rows = 10  # Default number of rows
    triangle = generate_pascals_triangle(rows)
    
    # Display basic triangle
    display_triangle(triangle)
    
    # Analyze and display patterns
    analyze_patterns(triangle)

if __name__ == "__main__":
    main()