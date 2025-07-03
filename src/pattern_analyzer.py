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

def analyze_fibonacci(triangle, rows):
    """Demonstrate Fibonacci sequence in shallow diagonals"""
    print("\nFibonacci Sequence in Diagonals:")
    fib_sequence = []
    max_diagonals = min(rows, 10)  # Limit for display
    
    for diagonal in range(max_diagonals):
        fib_num = 0
        i, j = diagonal, 0
        while i >= 0 and j < len(triangle):
            if i < len(triangle[j]):
                fib_num += triangle[j][i]
            i -= 1
            j += 1
        fib_sequence.append(fib_num)

    print("Fibonacci numbers from shallow diagonals:")
    print(", ".join(map(str, fib_sequence)))
    print("(Each number is the sum of the previous two)")

def analyze_sierpinski_pattern(triangle):
    """Mention the Sierpinski triangle pattern in parity"""
    print("\nSierpinski Triangle Pattern:")
    print("When coloring odd numbers and leaving even numbers blank,")
    print("Pascal's Triangle approximates the Sierpinski fractal.")
    print("(Visible in the colored output above)")