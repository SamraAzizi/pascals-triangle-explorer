def analyze_patterns(triangle, rows):
    """
    Analyze various patterns in Pascal's Triangle
    """
    analyze_row_sums(triangle)
    analyze_fibonacci(triangle, rows)
    analyze_sierpinski_pattern(triangle)

def analyze_row_sums(triangle):
    """Show that row sums are powers of 2"""
    print("\nRow Sums (Powers of 2):")
    for i, row in enumerate(triangle):
        row_sum = sum(row)
        power = i
        print(f"Row {i+1}: {row_sum} = 2^{power} ({2**power})")