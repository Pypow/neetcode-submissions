class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Think of this as a sliding window problem, NOT DFS/ RECURSION
        res = nums[0]   # IMP: I/P contains -ve eles
        total = 0
        for n in nums:
            if total < 0:
                total = 0
            total += n
            res = max(res, total)
        return res