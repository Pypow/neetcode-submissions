class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = {}
        for c in s1:
            need[c] = 1 + need.get(c, 0)
        
        l = 0
        have = {}
        for r in range(len(s2)):
            have[s2[r]] = 1 + have.get(s2[r], 0)
            while (r - l + 1) > len(s1):
                if have[s2[l]] > 1:
                    have[s2[l]] -= 1
                else:
                    del have[s2[l]]
                l += 1
            if have == need:
                return True
        return True if have == need else False
            