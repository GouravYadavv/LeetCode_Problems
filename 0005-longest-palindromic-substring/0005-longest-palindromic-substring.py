class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        max_len = 1
        max_str = s[0]
        
        for i in range(len(s)):
            for j in range(i + max_len, len(s) + 1):
                if j - i > max_len and s[i:j] == s[i:j][::-1]:
                    max_len = j - i
                    max_str = s[i:j]

        return max_str
