class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i == len(s) and j == len (p):
                return True
            if j == len(p):
                return False

            matches = i < len(s) and ((s[i] == p[j]) or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                dp[(i, j)] = dfs(i, j + 2) or (matches and dfs(i + 1, j))
                return dp[(i, j)]
            
            if matches:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else: 
                dp[(i, j)] = False
            return dp[(i, j)]
        return dfs(0, 0)
            