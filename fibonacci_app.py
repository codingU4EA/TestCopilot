import streamlit as st

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

# Streamlit app
st.title("Fibonacci Sequence - Recursive Implementation")
st.write("This app displays the result of the first example from fibonacci-python-guide.md")

# Display the result of fibonacci_recursive(10) as shown in the first example
st.subheader("Example Usage:")
st.code("fibonacci_recursive(10)")

result = fibonacci_recursive(10)
st.subheader("Result:")
st.success(f"fibonacci_recursive(10) = {result}")

# Display additional information
st.info("This uses the recursive implementation from the first example in the fibonacci-python-guide.md file.")