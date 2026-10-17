class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we need sets for each col, row and sq
        # col -> only c, row -> only r, sq -> (r, c)
        # so for storing everything in order, we use Hmap of sets 
        sqMap = collections.defaultdict(set)    # Key = (r // 3, c // 3)
        rowMap = collections.defaultdict(set)   # Key = r
        colMap = collections.defaultdict(set)   # Key = c
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rowMap[r] or
                    board[r][c] in colMap[c] or
                    board[r][c] in sqMap[(r // 3, c // 3)]):
                    return False
                rowMap[r].add(board[r][c])
                colMap[c].add(board[r][c])
                sqMap[(r//3, c//3)].add(board[r][c])
        return True



