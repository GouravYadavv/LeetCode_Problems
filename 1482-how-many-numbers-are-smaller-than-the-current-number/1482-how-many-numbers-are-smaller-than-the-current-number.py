class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = sorted(nums)
        b = {}
        for i in range(len(a)):
            if a[i] not in b:
                b[a[i]] = i
        return [b[i] for i in nums]