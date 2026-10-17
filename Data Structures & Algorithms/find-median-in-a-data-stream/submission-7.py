class MedianFinder:

    def __init__(self):
        self.left = []  # maxHeap
        self.right = [] # minHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        if len(self.right) > len(self.left) + 1:
            heapq.heappush(self.left, -heapq.heappop(self.right))
        if self.left and self.right and -self.left[0] > self.right[0]:
            a, b = -heapq.heappop(self.left), heapq.heappop(self.right)
            heapq.heappush(self.right, a)
            heapq.heappush(self.left, -b)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            a, b = -self.left[0], self.right[0]
            return (a + b)/ 2
        