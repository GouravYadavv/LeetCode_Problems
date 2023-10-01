class Solution:
    def reverseWords(self, s: str) -> str:
        L=[]
        string=s.split()
        for i in string:
            L.append(i[::-1])
        return " ".join(L)