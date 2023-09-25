class Solution:
    def isHappy(self, a: int) -> bool:
        if a==1:
            return True
        elif a==4:
            return False
        else:
            return self.isHappy(sum([int(i)**2 for i in str(a)]))