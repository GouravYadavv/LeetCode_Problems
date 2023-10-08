class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == 0:
            return []
        elif len(points)==1:
            return points
        else:
            points.sort(key=lambda x: x[0]**2+x[1]**2)
            return points[:k]