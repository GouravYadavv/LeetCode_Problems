class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp={}

        def Solve(n,sm):
            if sm<=0:
                return 0
            elif n<0:
                return float("inf")
            elif (n,sm) in dp:
                return dp[(n,sm)]
            else:
                paint=cost[n]+Solve(n-1,sm-1-time[n])
                skip=Solve(n-1,sm)
                c=min(paint,skip)
                dp[(n,sm)]=c
                return c

        return Solve(len(cost)-1,len(cost))