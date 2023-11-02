class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r

        while l<=r:
            mid=(l+r)//2
            if self.check(weights,mid,days):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
    
    def check(self,weights,mid,days):
        cnt=1
        cur=0
        for w in weights:
            if cur+w>mid:
                cnt+=1
                cur=w
            else:
                cur+=w
        return cnt<=days