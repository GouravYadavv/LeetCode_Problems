class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        L=[]
        R=[]
        for i in nums:
            if i%2==0:
                L.append(i)
            else:
                R.append(i)
        for i in R:
            L.append(i)
        return L