class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # len(piles) <= h -> if we eat max no of banana from each pile, we still need len(piles) hours to finish all bananas
        # range to search -> k = [1 to max(piles)]
        # T: O(N * log(M))    -> N = len(piles) and M = max(piles)
        res = max(piles)          # initial k
        l, r = 1, max(piles)      # range of k
        while l <= r:
            m = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / m)       # IMP
            if time <= h:                      # IMP
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res