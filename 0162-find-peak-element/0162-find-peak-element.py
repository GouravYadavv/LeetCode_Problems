class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)<4:
            return nums.index(max(nums))
        nums.insert(0,0)
        nums.append(0)
        for i in range(1,len(nums)-1):
            if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                return i-1