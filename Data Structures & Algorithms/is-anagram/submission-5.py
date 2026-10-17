class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shmap = {}
        thmap = {}
        for c in s:
            if c not in shmap:
                shmap[c] = 0
            shmap[c] += 1
        for c in t:
            if c not in thmap:
                thmap[c] = 0
            thmap[c] += 1
        return shmap==thmap
            