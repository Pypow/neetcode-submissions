class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        total = nums[l]
        res = nums[l]
        for r in range(1, len(nums)):
            if total < 0:
                total = 0
                l = r + 1
            total += nums[r]
            res = max(res, total)
        return res