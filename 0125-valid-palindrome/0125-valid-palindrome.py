class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = []
        for i in s:
            if i.isalpha() or i.isnumeric():
                L.append(i.lower())
        if L == L[::-1]:
            return True
        else:
            return False