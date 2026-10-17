class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s): True} # i: True/False -> from ith idx can we break the s
        def dfs(i):
            if i in dp:
                return dp[i]

            for word in wordDict:
                if ((i + len(word) - 1) < len(s)) and (s[i: i + len(word)] == word): #imp
                    if dfs(i + len(word)):  # if true, we found one matching word
                        dp[i] = True
                        return True
            dp[i] = False                   # we did not find any matching word
            return False
        return dfs(0)
                
            

