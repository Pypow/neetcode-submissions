class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}     # i: LIS -> what's the max LIS from ith idx
        def dfs(i, prev):
            if i >= len(nums):
                return 0
            if (i, prev) in dp:
                return dp[(i, prev)]
            
            skip = dfs(i + 1, prev)
            take = 0
            if nums[i] > prev:
                take = 1 + dfs(i + 1, nums[i])
            dp[(i, prev)] = max(skip, take)
            return dp[(i, prev)]
        
        return dfs(0, float('-inf'))        # imp
            