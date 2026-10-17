class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = [False] * len(nums)
        res[-1] = True
        i = len(nums) - 2
        goal = len(nums) - 1
        while i >= 0:
            dist = goal - i
            if nums[i] >= dist:
                res[i] = True
                goal = i
            i -= 1
        return res[0]
