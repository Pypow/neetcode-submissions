class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob1(nums):
            r1, r2 = 0, 0
            for i in range(len(nums)):
                tmp = max(r1 + nums[i], r2)
                r1 = r2
                r2 = tmp
            return r2
        return max(rob1(nums[1:]), rob1(nums[:len(nums)-1]))