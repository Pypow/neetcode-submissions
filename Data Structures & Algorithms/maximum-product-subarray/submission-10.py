class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP, minP = 1, 1
        res = max(nums)
        for n in nums:
            if n == 0:
                maxP, minP = 1, 1
                continue
            tmp = maxP
            maxP = max(maxP * n, minP * n, n)
            minP = min(tmp * n, minP * n, n)
            res = max(res, maxP)
        return res