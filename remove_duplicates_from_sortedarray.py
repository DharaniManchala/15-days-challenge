# Filename: remove_duplicates_sorted_array.py

def remove_duplicates(nums):
    """
    Removes duplicates from a sorted array in-place.

    Parameters:
    nums (List[int]): A sorted list of integers.

    Returns:
    int: The length of the array after removing duplicates.
    The input list `nums` is modified in-place to contain the unique elements in the first `k` positions.
    """
    if not nums:
        return 0

    # Pointer for the place to insert next unique element
    insert_pos = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[insert_pos] = nums[i]
            insert_pos += 1

    return insert_pos

# ------------------------
# Example usage
# ------------------------
if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    print(f"Unique count = {k}")
    print(f"Modified array (first {k} elements): {nums[:k]}")
