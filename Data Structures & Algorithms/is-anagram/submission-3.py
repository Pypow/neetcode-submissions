class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap = {}
        for c in s:
            hmap[c] = hmap.get(c, 0) + 1
        for c in t:
            if c not in hmap or hmap[c] <= 0:
                return False
            hmap[c] -= 1
        return True