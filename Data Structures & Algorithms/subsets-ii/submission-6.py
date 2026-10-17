class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        sub = []

        def dfs(i):
            if i >= len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i + 1)

            prev = sub.pop()
            while i < len(nums) and prev == nums[i]:
                i += 1
            dfs(i)

        dfs(0)
        return res