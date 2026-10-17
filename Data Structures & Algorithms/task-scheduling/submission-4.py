class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap = {}
        time = 0
        q = collections.deque()
        # get freq
        for t in tasks:
            if t not in hmap:
                hmap[t] = 0
            hmap[t] += 1
        
        maxHeap = [-cnt for cnt in hmap.values()]
        heapq.heapify(maxHeap)

        while maxHeap or q:
            time += 1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n])
            if q and q[0][1] == time:       # imp
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

