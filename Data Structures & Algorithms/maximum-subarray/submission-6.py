class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            if total < 0:
                total = 0
            total += n
            res = max(res, total)
        return res
