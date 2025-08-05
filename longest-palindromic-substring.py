class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            temp1 = expandAroundCenter(i, i)
            # Even length palindrome
            temp2 = expandAroundCenter(i, i + 1)
            
            if len(temp1) > len(longest):
                longest = temp1
            if len(temp2) > len(longest):
                longest = temp2
        
        return longest
s = Solution()
print(s.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(s.longestPalindrome("cbbd"))   # Output: "bb"
