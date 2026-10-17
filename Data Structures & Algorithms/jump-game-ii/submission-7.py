class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float('inf')   # return inf, as we can't jump any further
            jmp = float('inf')
            goal = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, goal):
                jmp = min(jmp, 1 + dfs(j))
            dp[i] = jmp
            return jmp
    
        return dfs(0) 