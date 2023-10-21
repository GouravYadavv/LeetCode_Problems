from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3
        b=Counter(nums)

        L=[]
        for i in b.keys():
            if b.get(i)>n:
                L.append(i)
        return L