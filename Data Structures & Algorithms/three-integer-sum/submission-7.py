class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()     # sort to remove duplicates
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:    # eleminate duplicates
                continue
            a = nums[i]
            l = i + 1
            r = len(nums)-1
            while l < r:
                total = a + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:   # eleminate duplicates
                        l += 1

        return res
