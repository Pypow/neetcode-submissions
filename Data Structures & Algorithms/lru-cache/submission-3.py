class ListNode:
    def __init__(self,key= 0, val=0, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.prev = prev



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = ListNode()
        self.right = ListNode()
        self.left.nxt = self.right
        self.right.prev = self.left
        self.hmap = {}

    def get(self, key: int) -> int:
        if key in self.hmap:
            self.remove(self.hmap[key])
            self.insert(self.hmap[key])
            return self.hmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.remove(self.hmap[key])
        self.hmap[key] = ListNode(key=key, val=value)
        self.insert(self.hmap[key])

        if len(self.hmap) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.hmap[lru.key]

    # insert at right, remove from left
    def remove(self, node):
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        node.nxt = nxt
        node.prev = prev
        nxt.prev = prev.nxt = node
 
        
        

        