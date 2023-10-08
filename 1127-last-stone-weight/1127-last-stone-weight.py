class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort(reverse=True)
            a=stones.pop(1)
            b=stones.pop(0)
            stones.insert(0,(abs(a-b)))
        return stones[0]