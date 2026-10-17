class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return 100000
            
            res = 100000
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                res = min(res, 1 + dfs(j))
            dp[i] = res
            return res
        return dfs(0)