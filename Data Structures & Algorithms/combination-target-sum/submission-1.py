class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(curSum, subset, i): 
            if curSum == target:
                res.append(subset.copy())
                return
            if curSum > target or i >= len(nums):
                return 
            
            # continue including nums[i]
            subset.append(nums[i])
            backtrack(curSum + nums[i], subset, i)
            subset.pop()

            # exclude nums[i] and explore other elemets
            backtrack(curSum, subset, i+1)
        
        backtrack(0, [], 0)
        return res