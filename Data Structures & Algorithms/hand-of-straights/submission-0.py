from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        
        while minHeap:
            start = minHeap[0]
            for card in range(start, start + groupSize):
                if count[card] == 0:
                    return False
                count[card] -= 1
                if count[card] == 0:
                    if card != minHeap[0]:
                        return False  # shouldn't happen if logic is right, sanity check
                    heapq.heappop(minHeap)
        
        return True