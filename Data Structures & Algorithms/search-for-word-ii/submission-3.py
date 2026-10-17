class Node:
    def __init__(self):
        self.children = {}
        self.eow = False
        self.word = ""

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.eow = True
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()

        for word in words:
            root.addWord(word)

        res = set()
        visit = set()
        rows, cols = len(board), len(board[0])

        def dfs(r, c, cur):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visit or
                board[r][c] not in cur.children):
                return False

            visit.add((r, c))
            cur = cur.children[board[r][c]]
            if cur.eow:
                res.add(cur.word)

            dfs(r + 1, c, cur)
            dfs(r - 1, c, cur)
            dfs(r, c + 1, cur)
            dfs(r, c - 1, cur)
            visit.remove((r, c))

        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return list(res)
                    



