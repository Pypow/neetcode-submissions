class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quick Select Implementation
        l, r = 0, len(nums) - 1
        k = len(nums) - k
        while l <= r:    
            piviot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= piviot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            if k == p:
                return nums[p]
            elif k < p:
                r = p - 1
            else:
                l = p + 1
    
                


