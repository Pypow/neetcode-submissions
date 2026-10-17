class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, curr):
            if curr == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or curr > target:
                return
                
            # include ith ele
            subset.append(nums[i])
            dfs(i, curr + nums[i])

            # exclude ith ele
            subset.pop()
            dfs(i+1, curr)
        dfs(0, 0)
        return res



            