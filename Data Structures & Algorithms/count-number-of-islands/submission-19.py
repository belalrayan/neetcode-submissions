class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n, m= len(grid),len(grid[0])
        islands=0
        visited=set()
        directions=[[-1,0],[1,0],[0,1],[0,-1]]
        for r in range(n):
            for c in range(m):
                if grid[r][c]=='1' and (r,c) not in visited:
                    islands+=1
                    q=collections.deque()
                    q.append((r,c))
                    while q:
                        dr, dc= q.popleft()
                        for nr, nc in directions:
                            hr, hc= dr+nr, dc+nc
                            if 0<=hr<n and 0<=hc<m and grid[hr][hc]=='1' and (hr,hc) not in visited:
                                visited.add((hr,hc))
                                q.append((hr,hc))
        return islands                        

        