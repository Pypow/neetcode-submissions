class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 0
            freq[s[r]] += 1
            window = r - l + 1
            maxf = max(maxf, freq[s[r]])
            if (window - maxf) <= k:
                res = max(res, window)
            else:
                freq[s[l]] -= 1
                l += 1
        return res
            
            
