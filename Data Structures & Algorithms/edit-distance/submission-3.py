class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # insert - (i, j + 1)
        # delete - (i + 1, j)
        # replace - (i + 1, j + 1)

        # dp = {}
        # if len(word2) == 0:
        #     return len(word1)
        # if len(word1) == 0:
        #     return len(word2)
        # def dfs(i, j):
        #     if j == len(word2):
        #         return len(word1[i:])
        #     if i == len(word1):
        #         return len(word2[j:])
        #     if (i, j) in dp:
        #         return dp[(i, j)]
        #     if word1[i] == word2[j]:
        #         dp[(i, j)] = dfs(i + 1, j + 1)
        #     else:
        #         dp[(i, j)] = 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1))
        #     return dp[(i, j)]
        # return dfs(0, 0)

        dp = [[float('inf')] * (len(word2) + 1) for i in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]

