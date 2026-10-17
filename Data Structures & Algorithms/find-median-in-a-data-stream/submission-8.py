class MedianFinder:

    def __init__(self):
        self.left = []      # maxHeap
        self.right = []     # minHeap

    def addNum(self, num: int) -> None:
        # balance left
        heapq.heappush(self.left, -num)
        if len(self.left) > len(self.right) + 1:
            ele = heapq.heappop(self.left)
            heapq.heappush(self.right, -ele)

        # IMP: Every ele in left <= every ele in right
        if (self.left and self.right) and (-self.left[0] > self.right[0]):
            ele = heapq.heappop(self.left)
            heapq.heappush(self.right, -ele)
        
        # balance right
        if len(self.right) > len(self.left) + 1:
            ele = heapq.heappop(self.right)
            heapq.heappush(self.left, -ele)       

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            if len(self.left) > len(self.right):
                return -self.left[0]
            else:
                return self.right[0]
        