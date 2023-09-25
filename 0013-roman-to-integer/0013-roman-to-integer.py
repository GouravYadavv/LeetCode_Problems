class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary={'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        a=0
        for i in range(len(s)-1):
            if dictionary[s[i]]<dictionary[s[i+1]]:
                a-=dictionary[s[i]]
            else:
                a+=dictionary[s[i]]
        return a+dictionary[s[-1]]