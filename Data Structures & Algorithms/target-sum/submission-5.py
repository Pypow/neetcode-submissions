class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}     # (i, amt): no of ways

        def dfs(i, amt):
            if i == len(nums):
                if amt == target:
                    return 1
                return 0
            if (i, amt) in dp:
                return dp[(i, amt)]
            ways = dfs(i + 1, amt + nums[i]) + dfs(i + 1, amt - nums[i])
            dp[(i, amt)] = ways
            return ways
        return dfs(0, 0)