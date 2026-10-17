class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # IMP: i1 + i2 = i3
        # Use all chars in order
        # take char from s1 or s2 that matches s3 at any given point, either one should match
        dp = {}     # (i1, i2): True/ False
        if len(s1) + len(s2) != len(s3):
            return False
        def dfs(i1, i2):
            if (i1 + i2) == len(s3):
                return True
            if (i1, i2) in dp:
                return dp[(i1, i2)]
            res = False
            if (i1 < len(s1)) and s1[i1] == s3[i1 + i2]:
                res = res or dfs(i1 + 1, i2)
            if (i2 < len(s2)) and s2[i2] == s3[i1 + i2]:
                res = res or dfs(i1, i2 + 1)
            dp[(i1, i2)] = res
            return res
        return dfs(0, 0)
