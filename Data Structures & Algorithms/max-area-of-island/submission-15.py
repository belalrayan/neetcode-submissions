class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n, m=len(grid),len(grid[0])
        visited=set()
        max_area=0
        directions=[[-1,0],[1,0],[0,1],[0,-1]]
        for r in range(n):
            for  c in range(m):
                if grid[r][c]==1 and ((r,c)) not in visited:
                    curr_area=0
                    visited.add((r,c))
                    q=collections.deque()
                    q.append((r,c))
                    while q:
                        rn,cn=q.popleft()
                        curr_area+=1
                        for dr,dc in directions:
                            hr,hc=rn+dr,cn+dc   
                            if 0<=hr<n and 0<=hc<m and grid[hr][hc]==1 and ((hr,hc)) not in visited:
                                    q.append((hr,hc))
                                    visited.add((hr,hc))
                            max_area=max(max_area,curr_area)

        return max_area                        
        