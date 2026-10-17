class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(subset, i):
            if i >= len(nums):
                res.append(subset.copy())
                return 

            # include nums[i]
            subset.append(nums[i])
            backtrack(subset, i+1)
            subset.pop()

            # exclue nums[i] and without its duplicates
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            backtrack(subset, i+1)

    
        backtrack([], 0)
        return res
