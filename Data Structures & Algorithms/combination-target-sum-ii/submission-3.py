class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(sub.copy())
                return
            if i >= len(candidates):
                return
            if total > target:
                return
            sub.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            sub.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)
        dfs(0, 0)
        return res
                