class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # intuitive SOLUTION: https://www.youtube.com/watch?v=gFm1lEfnzUQ
        res = []
        subset = []

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for n in nums:
                if n not in subset:
                    subset.append(n)
                    dfs()
                    subset.pop()
        dfs()
        return res