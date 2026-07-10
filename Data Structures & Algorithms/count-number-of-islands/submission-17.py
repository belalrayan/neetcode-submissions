class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n,m= len(grid),len(grid[0])
        visited=set()
        islands=0
        directions=[[-1,0],[1,0],[0,1],[0,-1]]


        for r in range (n):
            for c in range (m):
                if grid[r][c]=='1' and (r,c) not in visited:
                    islands+=1
                    visited.add((r,c))
                    q=collections.deque()
                    q.append((r,c))
                    while q:
                        cr,cc =q.popleft()
                        for dr,dc in directions:
                            nr,nc=cr+dr,cc+dc
                            if 0<=nr< n and 0<=nc<m and grid[nr][nc] == '1' and (nr, nc) not in visited:
                                q.append((nr,nc))
                                visited.add((nr,nc))
        return islands                        


        