class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        L = []
        counter = 1
        if len(nums)==0:
            return 0
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                counter += 1
                continue
            elif nums[i+1]==nums[i]:
                continue
            L.append(counter)
            counter = 1
        L.append(counter)
        return max(L)