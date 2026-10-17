class Solution:
    def numDecodings(self, s: str) -> int:
        # memoized
        dp = {len(s): 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            c = 0
            # single digit
            c += dfs(i + 1)
            # double digit
            if ((i + 1) < len(s)) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                c += dfs(i + 2)
            dp[i] = c
            return c
        return dfs(0)


            
