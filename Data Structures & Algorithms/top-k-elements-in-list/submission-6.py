class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}   # n: freq
        bucket = [[] for _ in range(len(nums) + 1)]   # freqTH idx -> list of ele with freq
        res = []

        for n in nums:
            hmap[n] = 1 + hmap.get(n, 0)

        for n, f in hmap.items():
            bucket[f].append(n)
        
        for i in range(len(bucket) -1, -1, -1):
            for j in range(len(bucket[i]) -1, -1, -1):
                res.append(bucket[i][j])
                if len(res) == k:
                    return res
        
        