class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}     # (i, j): no of op
        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j       # IMP (if any one reaches end, return remain chars from other word)
            if j == len(word2):
                return len(word1) - i       # IMP
            if (i, j) in dp:
                return dp[(i, j)]
            error = 0
            if word1[i] == word2[j]:
                error += dfs(i + 1, j + 1)
            else:               #insert                 delete          replace
                error += 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1))
            dp[(i, j)] = error
            return error
        return dfs(0, 0)