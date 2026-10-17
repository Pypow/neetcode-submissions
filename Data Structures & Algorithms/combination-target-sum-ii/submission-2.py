class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return
            # include ith ele
            subset.append(candidates[i])
            dfs(i+1, total + candidates[i])

            # exclude ith ele
            prev = subset.pop()
            while i < len(candidates) and candidates[i] == prev:
                i += 1
            if i < len(candidates):
                dfs(i, total)
        dfs(0, 0)
        return res