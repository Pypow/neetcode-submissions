class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:  # edge case
            return nums[0]  
        def dfs(i, arr, dp):
            if i >= len(arr):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(arr[i] + dfs(i + 2, arr, dp), dfs(i + 1, arr, dp))
            return dp[i]
        return max(dfs(0, nums[:len(nums)-1], {}), dfs(0, nums[1:], {}))
        # each call will have idx, sub array, hmap

        