class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        size=0
        n, m= len(grid), len(grid[0])
        visited=set()
        dirs=[[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(n):
            for c in range(m):
                if grid[r][c]=='1' and (r,c) not in visited:
                    size+=1
                    q=collections.deque()
                    q.append((r,c))
                    visited.add((r,c))
                    while q:
                        nr,nc=q.popleft()
                        for hr,hc in dirs:
                            dr,dc=hr+nr,hc+nc
                            if 0<=dr<n and 0<=dc<m and grid[dr][dc]=='1' and (dr,dc) not in visited:
                                q.append((dr,dc))
                                visited.add((dr,dc))
        return size                        



        