class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        freq = [[] for i in range(len(nums)+ 1)]

        for n in nums:
            if n not in hmap:
                hmap[n] = 0
            hmap[n] += 1
        
        res = []
        for key, val in hmap.items():
            freq[val].append(key)

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

            