class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        total = set()   
        total.add(0) 
        target = sum(nums) // 2
        for n in nums:
            tmpSet = set()
            if target in total:
                return True
            for t in total:
                tmpSet.add(t+n)
                tmpSet.add(t)
            total = tmpSet
        return False

        
