class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {} # (i, a): no of ways
        def dfs(i, a):
            if i >= len(nums):
                return 1 if a == target else 0 
            cache[(i, a)] =  (
                dfs(i + 1, a + nums[i]) +
                dfs(i + 1, a - nums[i])
                )
            return cache[(i, a)]
        return dfs(0, 0)