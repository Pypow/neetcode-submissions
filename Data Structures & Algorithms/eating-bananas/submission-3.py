class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        res = float('inf')
        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2
            tmp = 0
            for p in piles:
                tmp += math.ceil(p/m)
            if tmp <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        return res
            
            

