class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 0
            freq[s[r]] += 1
            window = r - l + 1
            c, f = None, 0      # c -> max ocurring char
            for key, v in freq.items():
                if v > f:
                    c = key
                    f = v
            if (window - f) <= k:
                res = max(res, window)
            else:
                freq[s[l]] -= 1
                l += 1
        return res
            
            
