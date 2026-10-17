class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we take two vars pre and post and modify res arr in two pass
        # first pass for prefix (left to right) 
        # second pass for postfix (right to left)
        # T: O(n)  |  S: O(1)
        res = [1] * (len(nums))
        pre = 1
        post = 1

        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res