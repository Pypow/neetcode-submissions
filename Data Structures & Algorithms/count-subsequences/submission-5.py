class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}     # (i, j): no of subsequences

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            matched = 0
            if s[i] == t[j]:
                matched = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                matched = dfs(i + 1, j)
            dp[(i, j)] = matched
            return matched
        return dfs(0, 0)