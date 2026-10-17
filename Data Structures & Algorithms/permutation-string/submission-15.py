class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        need = {}   # s1 hmap
        have = {}   # s2 hmap

        for i in range(len(s1)):
            need[s1[i]] = 1 + need.get(s1[i], 0)
            have[s2[i]] = 1 + have.get(s2[i], 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if have == need:
                return True
            have[s2[r]] = 1 + have.get(s2[r], 0)
            have[s2[l]] -= 1
            if have[s2[l]] == 0:
                del have[s2[l]]
            l += 1
        return have == need

