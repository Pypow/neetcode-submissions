# trie construction
class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class TrieOperation:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.eow = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()        # available list of words
        visit = set()
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, node, word):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                (r, c) in visit or
                board[r][c] not in node.children):
                return
            visit.add((r, c))                       # IMP: this order is IMP
            node = node.children[board[r][c]]
            word.append(board[r][c])
            
            if node.eow:
                res.add("".join(word))
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            word.pop()                              # IMP: Backtrack to explore other paths
            visit.remove((r, c))
        
        # trie construction
        trie = TrieOperation()
        for w in words:
            trie.addWord(w)
        root = trie.root

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, [])
        return list(res)
        
