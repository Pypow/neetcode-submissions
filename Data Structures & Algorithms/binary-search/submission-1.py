class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        mid = None

        while l <= r:
            mid = l + ((r - l) // 2)    # (l + r) // 2 can lead to overflow in other lang
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid 
        return -1       
