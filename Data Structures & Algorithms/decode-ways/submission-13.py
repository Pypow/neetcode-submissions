class Solution:
    def numDecodings(self, s: str) -> int:
        # T: O(2^n) -> brute force without dp, without memoization
        def dfs(i):
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            # single digit
            res = dfs(i + 1)

            # double digit
            if (i + 1) < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i + 2)
            return res
        return dfs(0)
            