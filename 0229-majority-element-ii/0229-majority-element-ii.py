from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        result = []
        compare = len(nums) // 3

        for num, count in counts.items():
            if count > compare:
                result.append(num)

        return result
