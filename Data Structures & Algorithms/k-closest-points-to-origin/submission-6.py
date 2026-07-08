
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        points=[(math.sqrt(place[0]**2 +place[1]**2),[place[0],place[1]]) for place in points ]
        m_heap=points
        heapq.heapify(m_heap)
        for i in range(k):
            res.append(heapq.heappop(m_heap)[1])

        return res    



        
        