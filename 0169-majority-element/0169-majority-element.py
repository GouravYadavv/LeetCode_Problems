from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority=len(nums)//2 # This is the majority as per the question.
        a=Counter(nums)
        for i,j in a.items():
            if j > majority:
                return  i