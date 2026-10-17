class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shmap = {}   # sliding window hmap
        thmap = {}   
        res = ""
        resLen = float("inf")
        for c in t:
            if c not in thmap:
                thmap[c] = 0
            thmap[c] += 1

        have = 0
        need = len(thmap)
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c not in shmap:
                shmap[c] = 0
            shmap[c] += 1
            if c in thmap and shmap[c] == thmap[c]:    # imp: ==
                have += 1
            while have == need and l <= r:  # imp: keep it l <= r
                window = (r - l + 1)
                if window < resLen:
                    resLen = window
                    res = s[l: r + 1]
                # shrink the window
                shmap[s[l]] -= 1
                if s[l] in thmap and shmap[s[l]] + 1 == thmap[s[l]]:    # previously equal
                    have -= 1
                if shmap[s[l]] == 0:
                    del shmap[s[l]]
                l += 1
        return res


