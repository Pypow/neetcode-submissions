class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if not prices:
            return 0
        l, r = 0, 1
        while r < len(prices):
            currProfit = prices[r] - prices[l]
            profit = max(profit, currProfit) 
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1
        return profit

