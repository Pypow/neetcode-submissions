class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        def dfs(i, j, k):
            if k >= len(word):
                return True
            if (
                i < 0 or i >= len(board) or 
                j < 0 or j >= len(board[0]) or
                (i, j) in visit or
                board[i][j] != word[k]
            ):
                return False

            visit.add((i, j))
            k += 1
            # explore neighbours
            res = (
            dfs (i + 1, j, k) or
            dfs (i - 1, j, k) or
            dfs (i, j + 1, k) or
            dfs (i, j - 1, k) 
            )
            visit.remove((i, j))
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False



