class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        res, resLen = [-1, -1], float("inf")
        needMap = {}
        for c in t:
            needMap[c] = 1 + needMap.get(c, 0)
        need = len(needMap)

        haveMap = {}
        have = 0
        l = 0
        for r in range(len(s)):
            haveMap[s[r]] = 1 + haveMap.get(s[r], 0)
            if s[r] in needMap and haveMap[s[r]] == needMap[s[r]]:
                have += 1
            while have == need:
                count = r - l + 1

                if count < resLen:
                    resLen = count
                    res = [l, r]

                haveMap[s[l]] -= 1
                if s[l] in needMap and haveMap[s[l]] < needMap[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""
                

        