class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r,c):
            nonlocal board
            if r >= 0 and c >= 0 and r < rows and c < cols and board[r][c] == "O":
                board[r][c] = "T"
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
                

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"