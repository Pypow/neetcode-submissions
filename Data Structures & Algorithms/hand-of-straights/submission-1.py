class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hmap = {}
        for n in hand:
            hmap[n] = 1 + hmap.get(n, 0)
        minHeap = list(hmap.keys())
        heapq.heapify(minHeap)

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