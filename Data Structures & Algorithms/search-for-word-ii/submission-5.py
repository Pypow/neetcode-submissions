class Node:
    def __init__(self):
        self.children = {}
        self.eow = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build prefix tree
        self.root = Node()
        for word in words:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = Node()
                cur = cur.children[c]
            cur.eow = True


        # search word in prefix tree
        rows, cols = len(board), len(board[0])
        res = set()
        visit = set()

        # imp: this is backtracking DFS
        def dfs(r, c, node, word):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visit or
                board[r][c] not in node.children
            ):
                return 

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.eow:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, self.root, "")
        return list(res)

            
