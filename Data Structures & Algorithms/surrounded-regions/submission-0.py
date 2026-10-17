class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def captureDFS(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            captureDFS(r+1, c)
            captureDFS(r-1, c)
            captureDFS(r, c+1)
            captureDFS(r, c-1)

        # phase 1: DFS - capture unsurrounded region
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows-1] or c in [0, cols-1]):
                    captureDFS(r, c)
        
        # phase 2: capture surrounded region (O -> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # phase 3: uncapture unsurrounded region (T -> O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"