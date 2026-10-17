class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hmap = {}
        self.left, self.right = Node(0, 0), Node(0, 0)  # dummy nodes for head and tail
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.hmap:
            self.remove(self.hmap[key])
            self.insert(self.hmap[key])
            return self.hmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.remove(self.hmap[key])
        self.hmap[key] = Node(key, value)
        self.insert(self.hmap[key])

        if len(self.hmap) > self.cap:
            lru = self.right.prev
            self.remove(lru)
            del self.hmap[lru.key]
            

    def insert(self, node):     # insert from left
        prev, nxt = self.left, self.left.next
        node.next = nxt
        node.prev = prev
        prev.next = node
        nxt.prev = node
    
    def remove(self, node):     # remove from right
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

