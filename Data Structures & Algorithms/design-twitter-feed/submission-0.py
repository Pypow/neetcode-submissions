class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = {}     # userId: set of followeeId
        self.tweetMap = {}      # userId: list of [time, tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []    # [time, tweetId, followeeId, index]

        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, [time, tweetId, followeeId, index-1])
        
        while maxHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, [time, tweetId, followeeId, index-1])
        return res       

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)        
