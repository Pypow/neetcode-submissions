class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in smap:
                smap[s[i]] = 0
            smap[s[i]] += 1
            if t[i] not in tmap:
                tmap[t[i]] = 0
            tmap[t[i]] += 1
        return smap == tmap