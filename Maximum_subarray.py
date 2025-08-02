# Filename: maximum_subarray.py

def max_subarray(nums):
    """
    Finds the contiguous subarray with the largest sum using Kadane's Algorithm.

    Parameters:
    nums (List[int]): The input list of integers.

    Returns:
    int: The maximum subarray sum.
    """
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        # If current_sum + nums[i] is worse than just nums[i], start fresh
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

# ------------------------
# Example usage
# ------------------------
if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray(nums)
    print(f"Input: nums = {nums}")
    print(f"Maximum subarray sum = {result}")  # Output: 6
