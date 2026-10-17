class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            prev = subset.pop()
            while i < len(nums) and prev == nums[i]:
                i += 1
            dfs(i)
        dfs(0)
        return res