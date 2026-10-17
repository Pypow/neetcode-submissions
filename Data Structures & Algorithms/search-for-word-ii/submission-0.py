class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build Trie
        root = TrieNode()
        for word in words:
            root.addWord(word)

        res, visit = set(), set()
        rows, cols = len(board), len(board[0])


        # recursive Search
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or 
                c == cols or r == rows or
                (r, c) in visit or 
                board[r][c] not in node.children):
                return

            
            visit.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]

            if node.endOfWord:
                node.endOfWord = False
                res.add(word)
            
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visit.remove((r, c))
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)
            











