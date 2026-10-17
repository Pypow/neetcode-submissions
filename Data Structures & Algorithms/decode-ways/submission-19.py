class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        dp[len(s)] = 1           # IMP
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":     # IMP: DONT USE i >= len(s) -> return 0 
                return 0
            # single digit
            dp[i] = dfs(i + 1)   
            # double digit      
            if ((i + 1) < len(s) and 
            (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"))):
                dp[i] += dfs(i + 2)
            return dp[i]
        return dfs(0)


            