class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        q = collections.deque()   # cooldown tasks: (task, cooldown)
        freq = {}

        for t in tasks:
            if t not in freq:
                freq[t] = 0
            freq[t] += 1
        
        maxHeap = [-f for f in freq.values()]
        heapq.heapify(maxHeap)

        while maxHeap or q:
            res += 1
            if maxHeap:
                task = 1 + heapq.heappop(maxHeap)
                if task:
                    q.append((task, n + res))
            if q and q[0][1] == res:
                task, _ = q.popleft()
                heapq.heappush(maxHeap, task)
        return res




