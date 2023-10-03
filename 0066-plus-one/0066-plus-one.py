class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=0
        for i in digits:
            a=a*10
            a+=i
        a+=1
        L=[]
        while a!=0:
            L.append(a%10)
            a=a//10
        return reversed(L)