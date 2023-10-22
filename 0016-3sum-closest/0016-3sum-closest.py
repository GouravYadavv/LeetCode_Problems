from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        ans=nums[0]+nums[1]+nums[2]

        nums.sort()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if abs(target-sum)<abs(target-ans):
                    ans=sum
                if sum<target:
                    l+=1
                elif sum>target:
                    r-=1
                else:
                    return ans

        return ans