class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()         # uses O(n) space
        visit = {}
        for i in range(len(nums)):
            visit[nums[i]] = visit.get(nums[i], 0) + 1
        for i in range(len(nums)):
            visit[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums)):
                visit[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                curSum = -(nums[i] + nums[j])
                if visit.get(curSum, 0) > 0:
                    res.append([nums[i], nums[j], curSum])
            
            for j in range(i + 1, len(nums)):
                visit[nums[j]] = visit.get(nums[j], 0) + 1
        return res
                

                

