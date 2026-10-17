class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # DP with Memo :  T: O(n * max(nums[i]))   |    S: O(n)

        dp = {} # i: T/F
        def dfs(i):
            if i >= len(nums)-1:
                return True
            if i in dp:
                return dp[i]
            dp[i] = False
            for j in range(1, nums[i] + 1):
                if dfs(i + j):
                    dp[i] = True
                    return True
            return False
        return dfs(0)
                