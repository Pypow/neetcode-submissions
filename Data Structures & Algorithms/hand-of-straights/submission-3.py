class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        mapH = {}

        if len(hand) % groupSize:
            return False

        for n in hand:
            mapH[n] = 1 + mapH.get(n, 0)
        minHeap = list(mapH.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]
            for i in range(first, first + groupSize):
                if i not in mapH:
                    return False
                mapH[i] -= 1
                if mapH[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
