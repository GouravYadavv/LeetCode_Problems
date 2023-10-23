class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()

        count=0

        median=nums[len(nums)//2]

        for n in nums:
            if n!=median:
                count+=abs(n-median)
        return count