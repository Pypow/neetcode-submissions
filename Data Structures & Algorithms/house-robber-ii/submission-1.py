class Solution:
    def rob(self, nums: List[int]) -> int:        
        def helper(numsSub):
            rob1, rob2 = 0, 0
            for n in numsSub:
                tmp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2
            
        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))