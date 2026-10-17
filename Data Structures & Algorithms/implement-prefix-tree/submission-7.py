class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}  # hmap of TrieNodes
        self.eow = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode("None")

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.eow = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.eow

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
        