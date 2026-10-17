class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        end = 0
        for i, c in enumerate(s):
            last[c] = i
        count = 0
        res = []
        for i in range(len(s)):
            if last[s[i]] > end:
                end = last[s[i]]
            count += 1
            if i == end:
                res.append(count)
                count = 0
        return res