class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            maxL=0
            i=0
            j=1
            while i<len(s):
                while j<len(s) and s[j] not in s[i:j]:
                    j+=1
                maxL=max(maxL,j-i)
                i+=1
            return maxL