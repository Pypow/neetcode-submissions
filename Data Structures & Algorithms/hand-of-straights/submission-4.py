class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hmap = {}
        minHeap = []
        for h in hand:
            if h not in hmap:
                hmap[h] = 0
            hmap[h] += 1
        
        for n in hmap.keys():
            heapq.heappush(minHeap, n)

        while minHeap:
            first = minHeap[0]

            for i in range(first, first + groupSize):
                if i not in hmap:
                    return False
                hmap[i] -= 1
                if hmap[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
            
        