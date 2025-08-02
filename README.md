# 📘 15 Days DSA Challenge – Python Solutions

This repository contains clean and efficient Python implementations for popular data structure and algorithm problems. These are suitable for interview preparation and daily problem-solving practice.

---

## ✅ Day 1: Two Sum (Unsorted Array)

**Problem Statement**:  
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

**Approach**: Hashmap (Dictionary)  
- Iterate over the array.
- For each number, check if the complement (`target - num`) is already in the hashmap.
- If found, return the indices.
- Else, store the number with its index in the hashmap.

**File**: [`two_sum_unsorted.py`](./two_sum_unsorted.py)

**Time Complexity**: `O(n)`  
**Space Complexity**: `O(n)`

---

## ✅ Day 2: Maximum Subarray (Kadane's Algorithm)

**Problem Statement**:  
Find the contiguous subarray (containing at least one number) which has the largest sum.

**Approach**: Kadane’s Algorithm  
- Use a single pass to keep track of the maximum sum so far and the current subarray sum.
- Reset current sum if it becomes negative.

**File**: [`maximum_subarray.py`](./maximum_subarray.py)

**Time Complexity**: `O(n)`  
**Space Complexity**: `O(1)`

---

## ✅ Day 3: Remove Duplicates from Sorted Array

**Problem Statement**:  
Given a sorted array `nums`, remove the duplicates in-place such that each element appears only once and return the new length.

**Approach**: Two Pointers  
- One pointer for reading (`i`), and one for writing unique elements (`insert_pos`).
- Overwrite duplicates in-place.

**File**: [`remove_duplicates_sorted_array.py`](./remove_duplicates_sorted_array.py)

**Time Complexity**: `O(n)`  
**Space Complexity**: `O(1)` (in-place)

---

## 🚀 How to Run

```bash
python filename.py
