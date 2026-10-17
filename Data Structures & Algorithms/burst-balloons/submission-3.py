class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # IMP:
        # what happens if we pop ith sub array last?
        # we are going to add 1s to either side to take care of single ele
        # T: O(n^3) [for each subarray we iterate entire arr]     S: O(n^2)   (no of subarrays)
        nums = [1] + nums + [1]
        dp = {}     # (l, r): max score of subarray from l to r
        def dfs(l, r):
            if l > r:
                return 0    # out of bounds/ no subarray
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]   # curr score
                res =  dfs(l, i-1) + coins + dfs(i + 1, r)    # left sub + cur score + right sub
                dp[(l, r)] = max(dp[(l, r)], res)
            return dp[(l, r)]
        return dfs(1, len(nums)-2)