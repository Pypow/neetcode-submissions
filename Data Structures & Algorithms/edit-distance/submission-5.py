class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp - memoized
        dp = {} # (i, j): 
        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in dp:
                return dp[(i, j)]
            res = 0
            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            else:
                res = 1 + min(
                    dfs(i, j+1),    # insert
                    dfs(i+1, j),    # delete
                    dfs(i+1, j+1)   # replace
                )
            dp[(i, j)] = res
            return res
        return dfs(0, 0)