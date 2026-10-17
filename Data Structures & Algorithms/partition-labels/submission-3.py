class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end = 0
        res = []
        hmap = {}

        for i, c in enumerate(s):
            hmap[c] = i
        
        size = 0

        for i, c in enumerate(s):
            size += 1
            if hmap[c] > end:
                end = hmap[c]
            if i == end:
                res.append(size)
                size = 0
        return res

        
            
