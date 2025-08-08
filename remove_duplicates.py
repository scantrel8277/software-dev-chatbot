def remove_duplicates(nums):
    seen = set()
    unique_nums = []
    
    for num in nums:
        if num not in seen:
          seen.add(num)
          unique_nums.append(num)
    return unique_nums
