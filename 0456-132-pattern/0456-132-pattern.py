class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        min_num = [nums[0]]
        for i in range(1, len(nums)):
            min_num.append(min(min_num[-1], nums[i]))
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > min_num[i]:
                while stack and stack[-1] <= min_num[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False