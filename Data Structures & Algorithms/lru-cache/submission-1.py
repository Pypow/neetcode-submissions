class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.next = nxt
        node.prev = prev
        prev.next = node
        nxt.prev = node
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self.remove(node)
            self.insert(node)
            return self.hmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.remove(self.hmap[key])
        self.hmap[key] = Node(key, value)
        self.insert(self.hmap[key])
        
        if len(self.hmap) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hmap[lru.key]
    

