class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority=len(nums)//2 # This is the majority as per the question.
        for i in set(nums):
            if nums.count(i)>majority:
                return i