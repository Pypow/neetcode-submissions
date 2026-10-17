class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Map = {}
        s2Map = {}
        l, r = 0, len(s1)-1
        for i in range(len(s1)):
            s1Map[s1[i]] = 1 + s1Map.get(s1[i], 0)
            s2Map[s2[i]] = 1 + s2Map.get(s2[i], 0)
        # for i in range(l, r+1):
        #     s2Map[s2[i]] = 1 + s2Map.get(s2[i], 0)
        while r < len(s2)-1: 
            if s2Map == s1Map:
                return True
            if s2Map.get(s2[l], 0):
                if s2Map[s2[l]] == 1:
                    s2Map.pop(s2[l])
                else:
                    s2Map[s2[l]] -= 1
            l += 1
            r += 1
            if r < len(s2):
                s2Map[s2[r]] = 1 + s2Map.get(s2[r], 0)
        return s2Map == s1Map 
