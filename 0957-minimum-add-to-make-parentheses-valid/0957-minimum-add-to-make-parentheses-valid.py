class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        flag=True
        while flag:
            if "()" in s:
                s=s[:s.find("()")]+s[s.find("()")+2:]
                flag=True
            else:
                flag=False
        return len(s)