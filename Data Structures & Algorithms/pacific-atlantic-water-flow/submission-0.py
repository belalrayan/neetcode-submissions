from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
            
        ROWS, COLS = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(r, c, reachable, prev_height):
            # אם חרגנו מהגבולות, או שכבר ביקרנו בתא, או שהתא הנוכחי נמוך מהקודם (לא ניתן לטפס)
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                (r, c) in reachable or 
                heights[r][c] < prev_height):
                return
                
            # מסמנים את התא כנגיש מהאוקיינוס הנוכחי
            reachable.add((r, c))
            
            # ממשיכים ל-4 הכיוונים
            dfs(r + 1, c, reachable, heights[r][c])
            dfs(r - 1, c, reachable, heights[r][c])
            dfs(r, c + 1, reachable, heights[r][c])
            dfs(r, c - 1, reachable, heights[r][c])
            
        # הרצה עבור השורה העליונה והתחתונה
        for c in range(COLS):
            dfs(0, c, pacific_reachable, heights[0][c]) # שורה עליונה (שקט)
            dfs(ROWS - 1, c, atlantic_reachable, heights[ROWS - 1][c]) # שורה תחתונה (אטלנטי)
            
        # הרצה עבור העמודה השמאלית והימנית
        for r in range(ROWS):
            dfs(r, 0, pacific_reachable, heights[r][0]) # עמודה שמאלית (שקט)
            dfs(r, COLS - 1, atlantic_reachable, heights[r][COLS - 1]) # עמודה ימנית (אטלנטי)
            
        # מחזירים את נקודת החיתוך שבה מגיעים גם לשקט וגם לאטלנטי
        return [list(cell) for cell in pacific_reachable.intersection(atlantic_reachable)]