class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums==sorted(nums) or nums==sorted(nums)[::-1]:
            return True
        return False