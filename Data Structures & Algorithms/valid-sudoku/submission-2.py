class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        
        # row-wise
        for r in range(rows):
            visited = set()
            for c in range(cols):
                if board[r][c] != ".":
                    if board[r][c] in visited:
                        return False
                    visited.add(board[r][c])

        # col-wise
        for c in range(cols):
            visited = set()
            for r in range(rows):
                if board[r][c] != ".":
                    if board[r][c] in visited:
                        return False
                    visited.add(board[r][c])
        
        # 3x3 Matrix
        for rw in range(0, rows, 3):
            for cl in range(0, cols, 3):
                startRow, startCol = rw, cl
                endRow, endCol = startRow + 2, startCol + 2

                visited = set()
                for r in range(startRow, endRow + 1):
                    for c in range(startCol, endCol + 1):
                        if board[r][c] != ".":
                            if board[r][c] in visited:
                                return False
                            visited.add(board[r][c])
        return True
                
                

