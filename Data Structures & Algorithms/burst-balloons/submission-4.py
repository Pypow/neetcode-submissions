class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}     # (l, r): max coins
        nums = [1] + nums + [1]

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                res = dfs(l, i - 1) + coins + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], res)
            return dp[(l, r)]
        return dfs(1, len(nums)-2)