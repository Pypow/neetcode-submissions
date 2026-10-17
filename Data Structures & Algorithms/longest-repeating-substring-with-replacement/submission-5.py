class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hmap = {}   # freq of each char in current window
        res = 0
        for r in range(len(s)):
            hmap[s[r]] = 1 + hmap.get(s[r], 0)
            while (r - l + 1) - max(hmap.values()) > k:
                if hmap[s[l]]:
                    hmap[s[l]] -= 1
                else:
                    del hmap[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
            
                