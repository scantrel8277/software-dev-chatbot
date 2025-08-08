def eliminate_duplicates_and_sort(countries):
    """
    This function takes a list of country names, removes any duplicates,
    and returns a sorted list of unique country names.
    
    Parameters:
    countries (list): A list of country names (strings).
    
    Returns:
    list: A sorted list of unique country names.
    """
    # Use a set to eliminate duplicates, then convert back to a list
    unique_countries = list(set(countries))
    
    # Sort the list alphabetically
    unique_countries.sort()
    
    return unique_countries

# Example input list containing duplicates
example_countries = [
    'Canada', 'Brazil', 'Germany', 'Canada', 'France',
    'Germany', 'Australia', 'Brazil', 'Japan', 'France'
]

# Call the function and print the result
sorted_unique_countries = eliminate_duplicates_and_sort(example_countries)
print(sorted_unique_countries)
