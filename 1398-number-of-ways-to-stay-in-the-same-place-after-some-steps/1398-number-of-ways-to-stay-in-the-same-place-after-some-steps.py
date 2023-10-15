class Solution:
    MOD = 1000000007

    def numWays(self, steps: int, arrLen: int) -> int:
        return self.countWays(steps, 0, arrLen)
    dp={}
    def countWays(self, steps, position, arrLen):
        if position < 0 or position >= arrLen:
            return 0

        if steps == 0:
            return 1 if position == 0 else 0
        elif (steps, position,arrLen) in self.dp:
            return self.dp[(steps, position,arrLen)]

        ways = self.countWays(steps - 1, position, arrLen)
        ways = (ways + self.countWays(steps - 1, position - 1, arrLen)) % self.MOD
        ways = (ways + self.countWays(steps - 1, position + 1, arrLen)) % self.MOD
        self.dp[(steps, position,arrLen)] = ways
        

        return ways

