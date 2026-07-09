from collections import deque

class Solution:
    def orangesRotting(self, grid):
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = 0

        while q:
            r, c, t = q.popleft()
            minutes = max(minutes, t)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, t + 1))

        return minutes if fresh == 0 else -1