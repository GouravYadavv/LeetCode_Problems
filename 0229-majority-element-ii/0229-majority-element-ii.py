from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict=Counter(nums)
        res=[]
        compare=len(nums)/3
        for i in dict:
            if dict[i]>compare:
                res.append(i)
        return res