class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for a in tasks:
            count[a] = 1 + count.get(a, 0)
        
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = collections.deque()
        time = 0

        while maxHeap or q:
            time += 1
            # process the ready task
            if len(maxHeap):
                task = heapq.heappop(maxHeap) + 1       # decrement by 1
                if task:
                    q.append([task, n+time])
            # move task from waiting to be processed 
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                     
        return time            


