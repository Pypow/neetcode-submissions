class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}     # (i, j): True/ False

        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if (i, j) in dp:
                return dp[(i, j)]
            # wildcard or # alphabet
            matches = (i < len(s)) and (s[i] == p[j] or p[j] == ".")
            dp[(i, j)] = False
            
            # start
            if (j + 1) < len(p) and p[j + 1] == "*":
                dp[(i, j)] = (matches and dfs(i + 1, j)) or dfs(i, j + 2)
            
            else:
                if matches:
                    dp[(i, j)] = dfs(i + 1, j + 1);
            return dp[(i, j)]
        return dfs(0, 0)
        