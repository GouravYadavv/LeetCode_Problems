class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        s2=[]
        for i in s:
            if i=="#":
                if s1:
                    s1.pop()
                else:
                    pass

            else:
                s1.append(i)
        for i in t:
            if i=="#":
                if s2:
                    s2.pop()
                else:
                    pass
            else:
                s2.append(i)
        return "".join(s1)=="".join(s2)