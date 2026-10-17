class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select algorithm
        k = len(nums) - k   # index of ele if array was sorted

        def quickSelect(l, r):
            piviot = nums[r]
            p = l    
            for i in range(l, r):
                if nums[i] <= piviot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if k > p:
                return quickSelect(p+1, r)
            elif k < p:
                return quickSelect(l, p-1)
            else:
                return nums[p]
        return quickSelect(0, len(nums)-1)




