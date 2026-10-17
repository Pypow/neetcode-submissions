class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        size = 0
        end = 0
        mapH = {}

        for i, c in enumerate(s):
            mapH[c] = i
        
        for i in range(len(s)):
            if mapH[s[i]] > end:
                end = mapH[s[i]]

            size += 1

            if i == end:
                res.append(size)
                size = 0
        return res
