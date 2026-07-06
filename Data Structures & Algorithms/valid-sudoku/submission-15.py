class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for k in range(0,3):
            for h in range(0,3):
                seen=set()
                for i in range(0,3):
                    for j in range(0,3):
                        if board[i+3*h][j+3*k]==".":
                            continue
                        if board[i+3*h][j+3*k] in seen:    
                            return False
                        seen.add(board[i+3*h][j+3*k])
    
        for j in range(0,9):
            seen=set()
            for i in range(0,9):
                if board[i][j]==".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])    


        
        for j in range(0,9):
            seen=set()
            for i in range(0,9):
                if board[j][i]==".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])    

        return True    

        

