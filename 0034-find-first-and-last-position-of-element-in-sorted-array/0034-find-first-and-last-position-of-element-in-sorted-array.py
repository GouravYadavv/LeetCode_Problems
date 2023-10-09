class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)
        start, end = -1, -1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                start = mid
                right = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                end = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return [start, end]