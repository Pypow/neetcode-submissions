class MedianFinder:

    def __init__(self):
        self.small = []     # maxheap
        self.large = []     # minheap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # order: ele in small always less than ele in large
        if (self.small and self.large and -self.small[0] > self.large[0]):
            ele = heapq.heappop(self.small)
            heapq.heappush(self.large, -ele)
        
        # rebalance: len(small) - len(large) not > 1
        if len(self.small) > len(self.large) + 1:
            ele = heapq.heappop(self.small)
            heapq.heappush(self.large, -ele)
        if len(self.large) > len(self.small) + 1:
            ele = heapq.heappop(self.large)
            heapq.heappush(self.small, -ele)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return ((-self.small[0]) + self.large[0]) / 2

        
        