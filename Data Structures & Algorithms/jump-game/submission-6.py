class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 2
        goal = len(nums) - 1
        while i >= 0:
            dist = goal - i
            if nums[i] >= dist:
                goal = i
            i -= 1
        return goal == 0
