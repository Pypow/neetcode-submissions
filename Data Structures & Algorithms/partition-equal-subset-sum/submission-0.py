class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        
        target = target // 2
        cache = set()
        cache.add(0)
        for i in range(len(nums) - 1, -1, -1):
            tmpCache = set()
            for t in cache:
                if (t + nums[i]) == target:
                    return True
                tmpCache.add(t + nums[i])
                tmpCache.add(t)
            cache = tmpCache
        return False

        