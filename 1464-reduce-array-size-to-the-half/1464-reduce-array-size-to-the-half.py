from typing import List
from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        a=Counter(arr)

        n=len(arr)

        target=n//2

        count=0

        for i in sorted(a.values(),reverse=True):
            n-=i
            count+=1
            if n<=target:
                break
        return count