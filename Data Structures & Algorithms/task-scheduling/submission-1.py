import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown = deque()  # (count, available_time)

        while max_heap or cooldown:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1  # +1 since counts stored negative
                if cnt != 0:
                    cooldown.append((cnt, time + n))

            if cooldown and cooldown[0][1] == time:
                cnt, _ = cooldown.popleft()
                heapq.heappush(max_heap, cnt)

        return time