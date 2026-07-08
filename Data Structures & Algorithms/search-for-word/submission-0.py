class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, i):
            # אם הגענו לאינדקס ששווה לאורך המילה, מצאנו את כולה
            if i == len(word):
                return True
            
            # בדיקת חריגה מגבולות הלוח או חוסר התאמה באות הנוכחית
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                board[r][c] != word[i]):
                return False
            
            # סימון התא הנוכחי כדי שלא נחזור אליו באותו מסלול (Backtracking)
            temp = board[r][c]
            board[r][c] = '#'
            
            # חיפוש בארבעת הכיוונים האפשריים
            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))
            
            # ניקוי והחזרת המצב לקדמותו
            board[r][c] = temp
            
            return found

        # מעבר על כל התאים בלוח כנקודות התחלה אפשריות
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
                    
        return False