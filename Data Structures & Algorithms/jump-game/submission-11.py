class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Just DFS -> n!
        # DFS + Memo -> n^2
        # Greedy -> n
        dp = {} # i: T/ F
        def dfs(i):
            if i >= len(nums) - 1:
                return True
            if i in dp:
                return dp[i]
            for j in range(1, nums[i] + 1):
                if dfs(i + j):
                    dp[i + j] = True
                    return True
                dp[i + j] = False
            return False
        return dfs(0)
                