class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = {}     # i: a

        def dfs(i, a):
            if a == target:
                return True
            if a > target or i >= len(nums):
                return False
            if (i, a) in dp:
                return dp[(i, a)]

            skip = dfs(i + 1, a)
            take = dfs(i + 1, a + nums[i])
            dp[(i, a)] = skip or take
            return dp[(i, a)]
        return dfs(0, 0)
            