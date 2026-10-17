class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two pass on nums: once for prefix, next for postfix products
        # prefix = product of [i - 1] * i = ith prefix  [left to right]
        # postfix = product of [i + 1] * i = ith prefix [right to left]

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        res = [1] * len(nums)

        pre = 1
        post = 1
        for i in range(len(nums)):
            pre *= nums[i]
            prefix[i] = pre
        
        for i in range(len(nums) - 1, -1, -1):
            post *= nums[i]
            postfix[i] = post
        
        for i in range(len(nums)):
            prev = prefix[i - 1] if (i - 1) >= 0 else 1
            nxt = postfix[i + 1] if (i + 1) < len(postfix) else 1
            res[i] = prev * nxt
        return res
