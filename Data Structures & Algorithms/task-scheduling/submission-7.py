class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count of tasks                            [hmap]
        # process tasks that are most frequent      [maxHeap]
        # Know what tasks are ready to be processed [queue]

        hmap = {}   # "A": freq
        q = collections.deque() # (task, cooldown)
        res = 0        

        for t in tasks:
            if t not in hmap:
                hmap[t] = 0
            hmap[t] += 1
        
        maxHeap = [-v for v in hmap.values()] 
        heapq.heapify(maxHeap)

        while maxHeap or q:
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1
                if task:
                    q.append((task, res + n))
            if q and q[0][1] <= res:
                task, cooldown = q.popleft()
                heapq.heappush(maxHeap, task)
            res += 1
        return res
        

