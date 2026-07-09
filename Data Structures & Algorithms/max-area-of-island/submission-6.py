class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows,cols= len(grid), len(grid[0])
        visited=set()
        max_area=0

        def bfs(r,c):
            q=collections.deque()
            size=1
            q.append((r,c))
            visited.add((r,c))
            directions=[[-1,0],[1,0],[0,1],[0,-1]]

            while q:
                r,c=q.popleft()
                for dr, dc in directions:
                    nr,nc= r+dr,c+dc
                    if(nr in range (rows) and nc in range (cols)
                     and grid[nr][nc]==1 and (nr,nc) not in visited):
                     q.append((nr,nc))
                     visited.add((nr,nc))
                     size+=1
            return size         

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    max_area=max(bfs(r,c),max_area)

        return max_area




        