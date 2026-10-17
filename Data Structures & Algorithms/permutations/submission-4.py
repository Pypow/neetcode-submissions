class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        prem = []

        def dfs():
            if len(prem) == len(nums):
                res.append(prem.copy())
                return
            for n in nums:
                if n not in prem:
                    prem.append(n)
                    dfs()
                    prem.pop()
        dfs()
        return res