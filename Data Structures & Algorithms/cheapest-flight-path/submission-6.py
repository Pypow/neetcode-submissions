class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-ford -> blindly iterate over all edges, k times |  T: O(E * K)
        prices = [float("inf")] * n
        prices[src] = 0     
        for i in range(k + 1):  # run loop k + 1 times, dest is not considered as stop
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):   # path does not exist, yet
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]
                

