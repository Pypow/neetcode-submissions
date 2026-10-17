class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        res = 0
        l = 0
         
        for r in range(len(s)):
            while s[r] in visit:
                visit.remove(s[l])
                l += 1
            visit.add(s[r])
            res = max(res, len(visit))
        return res
