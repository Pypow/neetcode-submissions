class Node:
    def __init__(self,key=0, val=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {}  # key: node
        self.capacity = capacity
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            oldNode = self.hmap[key]
            self.remove(oldNode)

        self.hmap[key] = Node(key=key, val=value)
        self.insert(self.hmap[key])

        if len(self.hmap) > self.capacity:
            lru = self.right.prev
            self.remove(lru)
            del self.hmap[lru.key]

        
    def insert(self, node):
        # at left
        prev = self.left
        nxt = self.left.next
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def remove(self, node):
        # at right
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
