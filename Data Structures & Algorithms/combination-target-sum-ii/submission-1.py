class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(subset, curSum, i):
            if curSum == target:
                res.append(subset.copy())
                return
            
            if curSum > target or i >= len(candidates):
                return
            
            # include nums[i] and duplicates
            subset.append(candidates[i])
            backtrack(subset, curSum + candidates[i], i+1)
            subset.pop()

            # exclude nums[i] and remove duplicates
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(subset, curSum, i+1)

        backtrack([], 0, 0)
        return res