class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}     # (i, j): min ops to make eq

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= len(word1):
                return len(word2) - j 
            if j >= len(word2):
                return len(word1) - i 
            ops = 0
            if word1[i] == word2[j]:
                ops += dfs(i + 1, j + 1)
            else:
                ops += 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
            dp[(i, j)] = ops
            return ops

        return dfs(0, 0)
                