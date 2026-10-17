class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hmap + heap -> T: O(  n  + k * log n)
        #                     hmap    heap 
        # OPTMIZED: bucket sort
        # 1. count numbers using hmap
        # 2. bucket sort: idx -> count, each idx is a list

        hmap = {}   # num: count
        arr = [[] for i in range(len(nums) + 1)]   # IMP: DONT USE [[]] * len(nums) + 1
        res = []

        for n in nums:
            if n not in hmap:
                hmap[n] = 0
            hmap[n] += 1
        
        for key, val in hmap.items():
            arr[val].append(key)
        
        for i in range(len(nums), -1, -1):
            j = 0
            while j < len(arr[i]):
                res.append(arr[i][j])
                j += 1
                if len(res) == k:
                    return res
