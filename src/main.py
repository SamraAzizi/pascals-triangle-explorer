from triangle_generator import generate_pascals_triangle
from pattern_analyzer import analyze_patterns
from visualization import display_triangle, display_colored_triangle

def main():
    print("Pascal's Triangle Explorer")
    print("=========================\n")
    
    try:
        rows = int(input("Enter number of rows (1-20): "))
        if rows < 1 or rows > 20:
            raise ValueError
    except ValueError:
        print("Invalid input. Using default 10 rows.")
        rows = 10