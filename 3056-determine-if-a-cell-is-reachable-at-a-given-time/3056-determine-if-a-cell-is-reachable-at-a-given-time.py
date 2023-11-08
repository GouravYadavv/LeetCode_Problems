class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        Min=min(abs(fx-sx),abs(fy-sy))+abs(abs(fx-sx)-abs(fy-sy))

        if sx==fx and sy==fy and t==1:
            return False
        
        else:
            return t>=Min