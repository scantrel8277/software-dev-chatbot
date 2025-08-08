def remove_duplicates(nums):
    """
    Remove duplicates from a list of numbers.
    
    Parameters:
    nums (list): A list of numbers that may contain duplicates.
    
    Returns:
    list: A list containing unique numbers, preserving the original order.
    """
    seen = set()  # Set to track seen numbers
    unique_nums = []  # List to store unique numbers
    
    for num in nums:
        if num not in seen:
            seen.add(num)  # Add number to seen set
            unique_nums.append(num)  # Append to unique list
    return unique_nums  # Return the list of unique numbers

# Example usage
numbers = [1, 2, 3, 2, 1, 4, 5, 3, 6, 5]
unique_numbers = remove_duplicates(numbers)
print("Unique numbers:", unique_numbers)
