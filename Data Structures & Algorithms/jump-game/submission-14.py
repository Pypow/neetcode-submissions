class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy: T: O(n)   |    S: O(1)
        goal = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0

        
                