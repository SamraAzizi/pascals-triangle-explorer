# Color codes for terminal output
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'reset': '\033[0m'
}

def display_triangle(triangle):
    """
    Print Pascal's Triangle with proper formatting
    """
    max_width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        print(' '.join(map(str, row)).center(max_width))

def display_colored_triangle(triangle):
    """
    Print Pascal's Triangle with even/odd numbers colored differently
    """
    max_width = len(' '.join(['X' for _ in triangle[-1]]))  # Account for color codes
    
    for row in triangle:
        colored_row = []
        for num in row:
            if num % 2 == 0:
                colored_num = f"{COLORS['blue']}{num}{COLORS['reset']}"
            else: