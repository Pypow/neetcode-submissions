class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        for i in range(len(nums) + 1):
            total -= i
        return abs(total)