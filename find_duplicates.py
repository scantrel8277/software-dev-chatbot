def find_duplicates(input_list):
    """
    Identifies and returns a list of duplicate elements from the given list of integers.

    Parameters:
    input_list (list): A list of integers which may contain duplicates.

    Returns:
    list: A list of duplicate integers found in the input list.
    """
    # Initialize an empty list to store duplicates
    duplicates = []
    # Use a set to track seen elements
    seen = set()

    # Iterate through each number in the input list
    for number in input_list:
        # If the number has been seen before, it's a duplicate
        if number in seen:
            # Only add to duplicates if it's not already added
            if number not in duplicates:
                duplicates.append(number)
        else:
            # Add the number to the seen set
            seen.add(number)

    return duplicates

# Sample input list with duplicates
sample_list = [1, 2, 3, 4, 2, 3, 5, 6, 5, 7]
# Calling the function and printing the result
print(find_duplicates(sample_list))  # Output: [2, 3, 5]
