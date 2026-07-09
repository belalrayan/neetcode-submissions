class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
             return 0

        rows, cols= len(grid), len(grid[0])
        visited=set()
        islands=0
        self.directions=[[1,0],[0,1],[-1,0],[0,-1]]

        def bfs(r,c):
            q=collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                r,c=q.popleft()
                for dr,dc in self.directions:
                    nr,nc =r+dr,c+dc
                    if(( nr in range(rows) and nc in range(cols))
                    and grid[nr][nc] =='1' and (nr,nc) not in visited):
                        q.append((nr,nc))
                        visited.add((nr,nc))

                


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands            


        