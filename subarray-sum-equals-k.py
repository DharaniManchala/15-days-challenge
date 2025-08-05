from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1  # Initialize with sum 0 having one count

        for num in nums:
            current_sum += num
            if (current_sum - k) in prefix_sum:
                count += prefix_sum[current_sum - k]
            prefix_sum[current_sum] += 1

        return count
s = Solution()
print(s.subarraySum([1, 1, 1], 2))  # Output: 2
