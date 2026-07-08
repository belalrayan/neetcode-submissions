class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-val for val in stones]
        heap=stones
        heapq.heapify(heap)
        while len(heap)>1:
            val1, val2 = heapq.heappop(heap), heapq.heappop(heap)
            if val1 -val2 ==0:
                continue
            else:
                heapq.heappush(heap,val1-val2)    
        return -heap[0] if heap else 0        

        