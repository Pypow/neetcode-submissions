class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = 1
        minP = 1
        res = max(nums)     # imp
        for n in nums:
            if n == 0:
                maxP = 1
                minP = 1
            tmpMaxP = maxP
            maxP = max(minP * n, maxP * n, n)   
            minP = min(minP * n, tmpMaxP * n, n)
            res = max(res, maxP)    # imp
        return res                  # not maxP
