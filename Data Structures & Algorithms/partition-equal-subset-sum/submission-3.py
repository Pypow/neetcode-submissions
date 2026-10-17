class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:   # odd, cant split
            return False
        target = total // 2
        # i -> 0 - len(nums) | remain -> 0 - target
        dp = [[-1] * (target + 1) for j in range(len(nums)+1)]

        def dfs(i, remain):
            if remain == 0:
                return True 
            if dp[i][remain] != -1:
                return dp[i][remain]
            if i >= len(nums) or remain < 0:
                return False
            res = False
            # consider curr ele
            res = res or dfs(i + 1, remain - nums[i])
            # skip curr ele
            res = res or dfs(i + 1, remain)
            dp[i][remain] = res
            return res
        return dfs(0, target)
