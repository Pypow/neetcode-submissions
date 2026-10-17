class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # imp: need to call dfs on each element; res = max of all dfs calls
        
        
        dp = [-1] * len(nums)
        
        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            LIS = 1 # count curr ele
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))  # curr + count of rest of the ele
            dp[i] = LIS
            return LIS
        return max([dfs(i) for i in range(len(nums))])