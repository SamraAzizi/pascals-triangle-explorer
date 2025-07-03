

def generate_pascals_triangle(rows):
    """
    Generate Pascal's Triangle up to specified number of rows
    Returns a 2D list representing the triangle
    """
    triangle = []
    for n in range(rows):
        row = [1]  # First element is always 1
        if n > 0:
            for k in range(1, n):
                # Each element is the sum of the two above it
                row.append(triangle[n-1][k-1] + triangle[n-1][k])
            row.append(1)  # Last element is always 1
        triangle.append(row)
    return triangle