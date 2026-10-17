class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for c in tasks:
            count[c] = 1 + count.get(c, 0)
        
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = collections.deque()
        time = 0
        while maxHeap or q:
            time += 1
            if len(maxHeap):
                task = 1 + heapq.heappop(maxHeap)       # decrementing 1, indicates remaining time
                if task:
                    q.append([task, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0]) 
        return time  
            
            



