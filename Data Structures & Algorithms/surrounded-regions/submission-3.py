class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Save "O"s that touch the border
        # Wipe out all other "O"s
        # Revive the saved "O"s

        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r, c):
            if(
                r < 0 or r == rows or
                c < 0 or c == cols or
                (r, c) in visit or
                board[r][c] == "X"
            ):
                return
            visit.add((r, c))
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # border travsersal
        for c in range(cols):   #horizontal
            dfs(0, c)
            dfs(rows-1, c)
        for r in range(rows):   #vertical
            dfs(r, 0)
            dfs(r, cols-1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"