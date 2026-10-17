class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # imp: sorting not required as all eles are DISTINCT
        res = []
        subset = []
        
        def dfs(i, cur):
            if cur == target:
                res.append(subset.copy())
                return
            if cur > target or i >= len(nums):
                return 
            
            subset.append(nums[i])
            dfs(i, cur + nums[i])

            subset.pop()
            dfs(i + 1, cur)
        dfs(0, 0)
        return res