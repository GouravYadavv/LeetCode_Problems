class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a=sorted(nums)
        if nums==a or nums==a[::-1]:
            return True
        return False