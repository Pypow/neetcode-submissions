class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # insert - (i, j + 1)
        # delete - (i + 1, j)
        # replace - (i + 1, j + 1)
        dp = {}
        if len(word2) == 0:
            return len(word1)
        if len(word1) == 0:
            return len(word2)
        def dfs(i, j):
            if j == len(word2):
                return len(word1[i:])
            if i == len(word1):
                return len(word2[j:])
            if (i, j) in dp:
                return dp[(i, j)]
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1))
            return dp[(i, j)]
        return dfs(0, 0)


