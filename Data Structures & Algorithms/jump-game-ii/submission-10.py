class Solution:
    def jump(self, nums: List[int]) -> int:
        # Memoized solution:  T: O(n * max(nums))     |    S: O(n)
        res = 0
        dp = {}         # i: no of jumps
        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            if i in dp:
                return dp[i]
            dp[i] = len(nums)
            jmp = 0
            for j in range(1, nums[i] + 1):
                jmp = min(dp[i], 1 + dfs(j + i))
                dp[i] = jmp
            return dp[i]
        return dfs(0)  