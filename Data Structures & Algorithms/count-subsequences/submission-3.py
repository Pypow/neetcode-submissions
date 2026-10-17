class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        res = 0
        def dfs(i, j):
            nonlocal res
            if not s and not t:
                return 1
            if not s:
                return 0
            if not t:
                return 1
            if (i, j) in dp:
                return dp[(i, j)]
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            tmp = 0
            if s[i] == t[j]:
                tmp += dfs(i+1, j+1)
                tmp += dfs(i+1, j)
            else:
                tmp += dfs(i+1, j)
            dp[(i, j)] = tmp
            res = max(res, tmp)
            return tmp
        dfs(0, 0)
        return res
            