class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for i in range(len(nums) + 1)] 

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        for n, c in freq.items():
            count[c].append(n)
        
        ans = []
        for i in range(len(count)-1, 0, -1):
            for j in count[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

                    