from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        cols, dig1, dig2 = [],[],[]
        def dfs(row):
            
            if row == n:
                res.append(["".join(r) for r in board])
            for col in range(n):
                if col not in cols and row + col not in dig1 and row - col not in dig2:
                    board[row][col] = "Q"
                    cols.append(col)
                    dig1.append(row+col)
                    dig2.append(row-col)
                    dfs(row+1)
                    
                    board[row][col] = "."
                    cols.pop()
                    dig1.pop()
                    dig2.pop()

        dfs(0)
        return res