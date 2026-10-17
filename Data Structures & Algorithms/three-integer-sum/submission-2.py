class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # T: O(N logN)  S: O(1)
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1
            while l < r:
                currSum = a + nums[l] + nums[r]
                if currSum > 0:
                    r-=1
                elif currSum < 0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
        
