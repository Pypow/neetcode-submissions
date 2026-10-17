class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        resLen = 0
        
        l = 0
        for r in range(len(s)):
            while s[r] in visit and l <= r:
                visit.remove(s[l])
                l += 1
            if s[r] not in visit:
                visit.add(s[r])
            resLen = max(resLen, (r - l + 1))
        return resLen
            
