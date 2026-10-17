class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}     # (t1, t2): max len of subsequence
        
        def dfs(t1, t2):
            if t1 >= len(text1) or t2 >= len(text2):
                return 0
            if (t1, t2) in dp:
                return dp[(t1, t2)]
            resLen = 0
            if text1[t1] == text2[t2]:
                resLen += 1 + dfs(t1 + 1, t2 + 1)       # found matching chars
            else:
                resLen += max(dfs(t1 + 1, t2), dfs(t1, t2 + 1)) # explore in either of strs
            dp[(t1, t2)] = resLen
            return resLen
        return dfs(0, 0)
            
