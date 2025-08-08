def find_max_min(numbers):
    """
    Find the maximum and minimum elements in a list.

    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    tuple: A tuple containing the maximum and minimum values.
    """
    # Check if the list is empty
    if not numbers:
        raise ValueError("The list cannot be empty.")

    # Initialize max and min with the first element of the list
    max_value = numbers[0]
    min_value = numbers[0]

    # Iterate through the list to find max and min
    for number in numbers:
        if number > max_value:
            max_value = number  # Update max if current number is greater
        if number < min_value:
            min_value = number  # Update min if current number is smaller

    return max_value, min_value  # Return the results as a tuple

# Example usage
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    max_elem, min_elem = find_max_min(sample_list)
    print(f'Maximum: {max_elem}, Minimum: {min_elem}')
