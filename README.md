# Pascal's Triangle Explorer

![Pascal's Triangle Example](examples/colored_output.png)  
*Visualizing mathematical patterns in Pascal's Triangle*

## 📖 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Examples](#-examples)
- [Testing](#-testing)
- [Mathematical Patterns](#-mathematical-patterns)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features
- **Interactive CLI** - Enter any number of rows (1-20)
- **Multiple Displays**:
  - Basic triangle output
  - Color-coded even/odd visualization
- **Pattern Detection**:
  - Row sums (powers of 2)
  - Fibonacci sequence in diagonals
  - Sierpinski triangle fractal pattern
- **Tested & Reliable** - Full unit test coverage

## 💻 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pascals-triangle-explorer.git
   cd pascals-triangle-explorer

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

## Usage
Run the interactive explorer:
```bash
python src/main.py
```

Sample Output:
```bash
Enter number of rows (1-20): 5

1. Basic Pascal's Triangle:
    1    
   1 1   
  1 2 1  
 1 3 3 1 
1 4 6 4 1

2. Colored Triangle:
[Yellow odd numbers, Blue even numbers]

3. Pattern Analysis:
Row sums: 1, 2, 4, 8, 16 (powers of 2)
Fibonacci sequence: 1, 1, 2, 3, 5
```

## Examples
see pre-generated outputs in `/exmaples`:
- `basic_output.txt`: Standart Triangle
- `colored_output.txt`: Color-formated version
- `fibonacci_highlight.txt`: Diagonal pattern

## Testing
Run the complete test suite:
```bash
python -m unittest discover tests
```

Expected Output:
```bash
...........
----------------------------------------------------------------------
Ran 11 tests in 0.002s

OK
```

## 🔢 Mathematical Patterns

### Key Discoveries

| Pattern       | Example               | Mathematical Basis       |
|---------------|-----------------------|--------------------------|
| Powers of 2   | Row sums: 1, 2, 4, 8... | ∑C(n,k) = 2ⁿ             |
| Fibonacci     | 1, 1, 2, 3, 5...      | Diagonal sums            |
| Sierpinski    | Fractal pattern       | Odd/even parity          |

![Pattern Visualization](https://docs/patterns.png)