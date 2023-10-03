class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first=nums[:n]
        second=nums[n:]
        L=[]
        for i in range(n):
            L.append(first[i])
            L.append(second[i])
        return L