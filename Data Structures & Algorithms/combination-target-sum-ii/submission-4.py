class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def dfs(i, cur):
            if cur == target:
                res.append(subset.copy())
                return
            if cur > target or i >= len(candidates):
                return
            
            subset.append(candidates[i])
            dfs(i + 1, cur + candidates[i])

            prev = subset.pop()
            while i < len(candidates) and candidates[i] == prev:
                i += 1
            dfs(i, cur)
        dfs(0, 0)
        return res