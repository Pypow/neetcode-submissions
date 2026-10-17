class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s): True}

        def dfs(i):
            if i in dp:
                return dp[i]
            for word in wordDict:
                w = len(word)
                res = False
                if i + w <= len(s) and s[i: i+w] == word:
                    if dfs(i+w):
                        res = True
                        break
            dp[i] = res
            return res

        return dfs(0)
