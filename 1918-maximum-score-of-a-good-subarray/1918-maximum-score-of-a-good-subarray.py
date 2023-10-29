class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        l=r=k

        curr_min=nums[k]
        res=nums[k]

        while l>0 or r<len(nums)-1:
            left=nums[l-1] if l>0 else 0
            right=nums[r+1] if r<len(nums)-1 else 0

            if left>right:
                l-=1
                curr_min=min(curr_min,left)
            else:
                r+=1
                curr_min=min(curr_min,right)
            
            res=max(res,curr_min*(r-l+1))
        
        return res
            
