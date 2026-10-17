class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        countF = [0] * 26
        res = 0

        for r in range(len(s)):
            countF[ord(s[r]) - ord("A")] += 1
            while (r-l+1) - max(countF) > k:
                countF[ord(s[l]) - ord("A")] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


