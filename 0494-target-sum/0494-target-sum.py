class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        Sum=sum(nums)
        n=len(nums)
        x=Sum+target

        if x%2!=0:
            return 0
        else:
            x=x//2

        dp={}

        def Solve(n,sm):
            if n==0:
                if sm==0:
                    return 1
                else:
                    return 0
            elif (n,sm) in dp:
                return dp[(n,sm)]
            else:
                item=nums[n-1]
                if item<=sm:
                    c1=Solve(n-1,sm-item)
                    c2=Solve(n-1,sm)

                    c=c1+c2
                else:
                    c=Solve(n-1,sm)
                
                dp[(n,sm)]=c
                return c
        return Solve(n,x)