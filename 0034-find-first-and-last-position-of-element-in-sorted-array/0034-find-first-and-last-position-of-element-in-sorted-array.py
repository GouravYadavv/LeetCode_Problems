class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = nums.index(target) if target in nums else -1
        b = a
        if a == -1:
            return [-1, -1]
        for i in range(a + 1, len(nums)):
            if nums[i] == target:
                b += 1
            else:
                break
        return [a, b]