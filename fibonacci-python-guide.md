# How to Write a Fibonacci Sequence in Python

## What is the Fibonacci Sequence?

The Fibonacci sequence is a famous mathematical sequence where each number is the sum of the two preceding ones. The sequence typically starts with 0 and 1:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
```

Mathematically, it can be defined as:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

## Implementation Methods

There are several ways to implement the Fibonacci sequence in Python, each with different trade-offs in terms of performance, memory usage, and code readability.

### 1. Recursive Implementation

The most straightforward approach that directly follows the mathematical definition:

```python
def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    
    Time Complexity: O(2^n) - Exponential
    Space Complexity: O(n) - Due to recursion stack
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage
print(fibonacci_recursive(10))  # Output: 55
```

**Pros:**
- Simple and intuitive
- Directly follows the mathematical definition

**Cons:**
- Very inefficient for large numbers due to repeated calculations
- Exponential time complexity
- Can cause stack overflow for large inputs

### 2. Iterative Implementation

A much more efficient approach using a loop:

```python
def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using iteration.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    
    Time Complexity: O(n) - Linear
    Space Complexity: O(1) - Constant
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage
print(fibonacci_iterative(10))  # Output: 55
```

**Pros:**
- Much more efficient than recursive approach
- Linear time complexity
- Constant space complexity

**Cons:**
- Slightly more complex logic than recursive approach

### 3. Memoized Recursive Implementation

Combines the simplicity of recursion with efficiency through caching:

```python
def fibonacci_memoized(n, memo={}):
    """
    Calculate the nth Fibonacci number using memoized recursion.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        memo (dict): Cache for previously calculated values
    
    Returns:
        int: The nth Fibonacci number
    
    Time Complexity: O(n) - Linear
    Space Complexity: O(n) - Due to memoization and recursion stack
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

# Alternative using functools.lru_cache decorator
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    """
    Calculate the nth Fibonacci number using cached recursion.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

# Example usage
print(fibonacci_memoized(10))  # Output: 55
print(fibonacci_cached(10))    # Output: 55
```

**Pros:**
- Combines simplicity of recursion with efficiency
- Linear time complexity after initial calculations

**Cons:**
- Uses more memory to store cached values
- Still has recursion stack limitations for very large numbers

### 4. Generator Implementation

Perfect for generating sequences or when you don't need all values at once:

```python
def fibonacci_generator():
    """
    Generate Fibonacci numbers indefinitely.
    
    Yields:
        int: Next Fibonacci number in sequence
    
    Space Complexity: O(1) - Constant
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fibonacci_sequence(count):
    """
    Generate the first 'count' Fibonacci numbers.
    
    Args:
        count (int): Number of Fibonacci numbers to generate
    
    Returns:
        list: List of the first 'count' Fibonacci numbers
    """
    if count < 0:
        raise ValueError("count must be non-negative")
    
    fib_gen = fibonacci_generator()
    return [next(fib_gen) for _ in range(count)]

# Example usage
fib_gen = fibonacci_generator()
first_10 = [next(fib_gen) for _ in range(10)]
print(first_10)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print(fibonacci_sequence(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

**Pros:**
- Memory efficient for large sequences
- Can generate infinite sequences
- Lazy evaluation

**Cons:**
- More complex for simple use cases

### 5. Matrix Exponentiation (Advanced)

For very large Fibonacci numbers, matrix exponentiation provides O(log n) complexity:

```python
def matrix_multiply(A, B):
    """Multiply two 2x2 matrices."""
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]

def matrix_power(matrix, n):
    """Calculate matrix to the power of n using fast exponentiation."""
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_power = matrix_power(matrix, n // 2)
        return matrix_multiply(half_power, half_power)
    else:
        return matrix_multiply(matrix, matrix_power(matrix, n - 1))

def fibonacci_matrix(n):
    """
    Calculate the nth Fibonacci number using matrix exponentiation.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    
    Time Complexity: O(log n) - Logarithmic
    Space Complexity: O(log n) - Due to recursion in matrix_power
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    
    # Base matrix [[1, 1], [1, 0]]
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(base_matrix, n)
    return result_matrix[0][1]

# Example usage
print(fibonacci_matrix(10))  # Output: 55
```

**Pros:**
- Most efficient for very large numbers
- Logarithmic time complexity

**Cons:**
- Complex implementation
- Overkill for small to medium numbers

## Performance Comparison

Here's a simple script to compare the performance of different implementations:

```python
import time

def benchmark_fibonacci(func, n, name):
    """Benchmark a Fibonacci function."""
    start_time = time.time()
    try:
        result = func(n)
        end_time = time.time()
        print(f"{name}: F({n}) = {result}, Time: {end_time - start_time:.6f} seconds")
    except RecursionError:
        print(f"{name}: RecursionError for F({n})")
    except Exception as e:
        print(f"{name}: Error - {e}")

# Test with n = 35
n = 35
print(f"Calculating F({n}):")
benchmark_fibonacci(fibonacci_iterative, n, "Iterative")
benchmark_fibonacci(fibonacci_memoized, n, "Memoized")
benchmark_fibonacci(fibonacci_matrix, n, "Matrix")
# Note: Recursive will be very slow for n=35, uncomment if you want to test
# benchmark_fibonacci(fibonacci_recursive, n, "Recursive")
```

## Best Practices and Recommendations

1. **For most use cases**: Use the **iterative implementation** - it's simple, efficient, and easy to understand.

2. **For generating sequences**: Use the **generator implementation** - it's memory efficient and allows for lazy evaluation.

3. **For very large numbers**: Consider the **matrix exponentiation** approach for optimal performance.

4. **For learning purposes**: Start with the **recursive implementation** to understand the concept, then move to more efficient versions.

5. **Error handling**: Always validate input parameters and handle edge cases appropriately.

6. **Documentation**: Include clear docstrings explaining the function's purpose, parameters, return values, and complexity.

## Common Use Cases

### Checking if a number is in the Fibonacci sequence

```python
def is_fibonacci(num):
    """Check if a number is in the Fibonacci sequence."""
    if num < 0:
        return False
    
    # Generate Fibonacci numbers until we reach or exceed the target
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    
    return a == num

# Example usage
print(is_fibonacci(21))  # True
print(is_fibonacci(20))  # False
```

### Finding the nth Fibonacci number modulo m

```python
def fibonacci_mod(n, m):
    """Calculate the nth Fibonacci number modulo m."""
    if n <= 1:
        return n % m
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % m
    return b

# Example usage
print(fibonacci_mod(100, 1000))  # Last 3 digits of F(100)
```

## Conclusion

The Fibonacci sequence offers an excellent example for learning different programming techniques in Python. Start with the simple recursive approach to understand the concept, then progress to more efficient implementations based on your specific needs. The iterative approach is usually the best balance of simplicity and efficiency for most practical applications.