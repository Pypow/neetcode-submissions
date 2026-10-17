class TrieNode:
    def __init__(self):
        self.children = {}      # hmap of TrieNodes
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root 
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.eow = True

    def search(self, word: str) -> bool:
        node = self.root
        def dfs(node, i):
            # if i == len(word):                    # WRONG: DON"T ADD THIS
            #     return node.eow
            for j in range(i, len(word)):
                c = word[j]                         # IMP: use i and j properly
                if c == ".":
                    for child in node.children.values(): #IMP: .values()
                        if dfs(child, j + 1):       # IMP: try every child
                            return True
                    return False                    # IMP: False if outside for loop
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.eow
        return dfs(node, 0)





