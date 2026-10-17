class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[0] * n for i in range(m)]
        for r in range(n):
            board[m-1][r] = 1
        for c in range(m):
            board[c][n-1] = 1
        
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                board[r][c] = board[r + 1][c] + board[r][c + 1]
        return board[0][0]