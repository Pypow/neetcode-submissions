class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapH = {}
        for i, c in enumerate(s):
            mapH[c] = i

        res = []
        size, end = 0, 0
        for i in range(len(s)):
            if mapH[s[i]] > end:
                end = mapH[s[i]]
            size += 1
            if i == end:
                res.append(size)
                size = 0
        return res
