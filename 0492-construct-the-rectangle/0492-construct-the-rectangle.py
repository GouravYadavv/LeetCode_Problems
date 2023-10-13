class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        length=1
        width=area
        L=[]
        while length<=width:
            if length*width==area:
                L.append([width,length])
            length+=1
            width=area//length
        return L[-1]