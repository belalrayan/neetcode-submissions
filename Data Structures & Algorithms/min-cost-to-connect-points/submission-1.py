class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        # build all edges
        for i in range(n):
            for j in range(n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        edges.sort()

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if rank[rx] < rank[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1
            return True

        total_cost = 0
        edges_used = 0

        for dist, i, j in edges:
            if union(i, j):
                total_cost += dist
                edges_used += 1
                if edges_used == n - 1:
                    break

        return total_cost