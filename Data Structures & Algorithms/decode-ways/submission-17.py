class Solution:
    def numDecodings(self, s: str) -> int:
        # you need to use complete string in different ways
        """     
        1 digit
        - (1-9)     -> it shoud not be 0
        2 digits
        - first digit-> 1, second digit (1-9)
        - first digigt-> 2, second digit (0-6)
        """
        dp = {len(s): 1}     # i: no of ways
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            # 1 digit
            ways = dfs(i + 1)
            # 2 digits
            if ((i + 1) < len(s)) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                ways += dfs(i + 2)
            dp[i] = ways
            return ways
        return dfs(0)




