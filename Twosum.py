# Filename: two_sum.py

def two_sum(nums, target):
    """
    Returns the indices of the two numbers such that they add up to the target.
    
    Parameters:
    nums (List[int]): The input array of integers.
    target (int): The target sum value.

    Returns:
    List[int]: Indices of the two numbers that add up to the target.
    """
    seen = {}  # HashMap to store number as key and its index as value

    for i, num in enumerate(nums):
        complement = target - num

        # Check if complement is already in the hashmap
        if complement in seen:
            return [seen[complement], i]

        # Otherwise, store the current number and its index
        seen[num] = i

    return []  # Return empty if no pair found

# ------------------------
# Example usage
# ------------------------
if __name__ == "__main__":
    nums = [11, 2, 15, 7]
    target = 9
    result = two_sum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")  # Output: [1, 3]
