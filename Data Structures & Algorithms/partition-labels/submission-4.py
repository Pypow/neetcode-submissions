class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        hmap = {}   # c: last idx
        for i, c in enumerate(s):
            hmap[c] = i
        
        count = 1
        end = 0
        for i in range(len(s)):
            end = max(end, hmap[s[i]])
            if i == end:
                res.append(count)
                count = 0
            count += 1
        return res