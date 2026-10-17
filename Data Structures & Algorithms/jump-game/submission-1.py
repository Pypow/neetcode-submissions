class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[len(nums)-1] = True
        for i in range(len(nums)-1, -1, -1):
            # dp[i] = dp[dp[i]]
            j = 0
            while j <= nums[i] and (i + j) < len(dp):
                if dp[i+j]:
                    dp[i] = True
                j += 1
        return dp[0]
