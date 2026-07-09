
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        dist = {}
        heap = [(0, k)]  # (distance, node)

        while heap:
            d, node = heapq.heappop(heap)
            if node in dist:
                continue  # already finalized with shorter distance
            dist[node] = d

            for nei, w in adj[node]:
                if nei not in dist:
                    heapq.heappush(heap, (d + w, nei))

        return max(dist.values()) if len(dist) == n else -1