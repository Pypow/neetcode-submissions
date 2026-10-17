class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}   # freq of c
        resLen = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in hmap:
                hmap[s[r]] = 0
            hmap[s[r]] += 1
            while (r - l + 1) - max(hmap.values()) > k:
                hmap[s[l]] -= 1
                if hmap[s[l]] == 0:
                    del hmap[s[l]]
                l += 1
            resLen = max(resLen, (r - l + 1))

        return resLen
