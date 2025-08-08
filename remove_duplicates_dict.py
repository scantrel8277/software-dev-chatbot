def remove_duplicates(nums):
    # Using dict.fromkeys to maintain order and remove duplicates
    return list(dict.fromkeys(nums))

#  Example usage
numbers = [1, 2, 3, 2, 1, 4, 5, 3, 6, 5]
unique_numbers = remove_duplicates(numbers)
print("Unique numbers:", unique_numbers)
