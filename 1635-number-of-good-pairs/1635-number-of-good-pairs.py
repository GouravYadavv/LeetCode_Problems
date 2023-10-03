class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result={}
        res=0

        for num in nums:
            if num in result:
                res+=result[num]
                result[num]+=1
            else:
                result[num]=1
        
        return res