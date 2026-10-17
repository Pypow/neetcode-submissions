class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # hmap to store values
        # minHeap to find starting pos of each group
        if len(hand) % groupSize:
            return False

        hmap = {}   # n: freq
        minHeap = []
        for n in hand:
            if n not in hmap:
                hmap[n] = 0
            hmap[n] += 1
        for n in hmap:
            heapq.heappush(minHeap, n)
        
        while minHeap:
            start = minHeap[0]
            if hmap[start] <= 0:
                heapq.heappop(minHeap)
                continue
            # find each group
            for i in range(groupSize):
                num = start + i
                if (num not in hmap) or (hmap[num] <= 0):
                    if num in hmap:
                        del hmap[num]
                    return False
                hmap[num] -= 1
        return True

        return True

        
