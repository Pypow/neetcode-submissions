class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap = {}   # counter
        count = 0
        for t in tasks:
            if t not in hmap:
                hmap[t] = 0
            hmap[t] += 1
        
        maxHeap = [-val for val in hmap.values()]
        heapq.heapify(maxHeap)

        q = collections.deque()     # stores cooldown tasks
        while maxHeap or q:
            count += 1
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1
                if task:
                    q.append([task, count + n])
            if q and q[0][1] == count:
                heapq.heappush(maxHeap, q.popleft()[0])
        return count

