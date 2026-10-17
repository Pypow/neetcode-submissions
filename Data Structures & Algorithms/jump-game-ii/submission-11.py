class Solution:
    def jump(self, nums: List[int]) -> int:
        # Memoized solution:  T: O(n)     |    S: O(1)
        # Logic: what's the min jumps needed from i to reach end n
        n = len(nums)
        dp = [float("inf")] * n
        dp[n - 1] = 0
        for i in range(n - 2, -1, -1):  # IMP: n-2 as n-1 is the goal
            for j in range(1, nums[i] + 1):
                if i + j < n:           # IMP: i + j < n   not  >
                    dp[i] = min(dp[i], 1 + dp[i + j])
        return dp[0]

