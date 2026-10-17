class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # IMP: * is where we have choice, skip it or consider it
        dp = {}     # (i, j): True/False
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):                                             # IMP
                return False
            if (i, j) in dp:
                return dp[(i, j)]
            matches = (i < len(s)) and (s[i] == p[j] or p[j] == ".")      # IMP

            if (j + 1) < len(p) and p[j + 1] == "*":
                dp[(i, j)] = (matches and dfs(i + 1, j)) or dfs(i, j + 2)  # consider or skip
                return dp[(i, j)]

            if matches:
                return dfs(i + 1, j + 1)                        # IMP
            return False
        return dfs(0, 0)
            