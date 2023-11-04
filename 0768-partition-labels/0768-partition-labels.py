from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        L=[]
        hash={}
        for i in range(len(s)):
            hash[s[i]]=i
        i=0
        while i<len(s):
            end=hash[s[i]]
            j=i
            while j!=end:
                end=max(end,hash[s[j]])
                j+=1
            L.append(j-i+1)
            i=j+1
        return L