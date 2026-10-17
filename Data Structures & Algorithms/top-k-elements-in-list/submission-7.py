class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}   # n: occurances
        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1
        
        # bucket sort
        arr = [[] for _ in range(len(nums) + 1)]
        for key, val in hmap.items():
            arr[val].append(key)

        res = []
        for i in range(len(arr) - 1, -1, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res

