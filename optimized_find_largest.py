def find_largest(arr):
    """Find the largest number in a list."""
    if not arr:
        raise ValueError("Input list cannot be empty.")  # Error handling for empty list
    largest = arr[0]  # Initialize largest with the first element
    for num in arr:
        if num > largest:
            largest = num  # Update largest if current number is greater
    return largest
