from collections import defaultdict
from typing import List
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        C=defaultdict(list)


        for i in range(len(routes)):
            for j in routes[i]:
                C[j].append(i)
        print(C)
        Q=[source]
        visited=set()
        ans=0
        while Q:
            newQ=[]
            for i in Q:
                if i==target:
                    return ans
                for j in C[i]:
                    if j not in visited:
                        visited.add(j)
                        for k in routes[j]:
                            newQ.append(k)
            Q=newQ
            ans+=1
        return -1
    