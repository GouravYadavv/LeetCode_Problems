class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        res=[]
        compare=len(nums)/3
        for i in dict:
            if dict[i]>compare:
                res.append(i)
        return res