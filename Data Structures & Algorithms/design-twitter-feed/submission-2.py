class Twitter:
    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)     # [count, tweetId]
        self.followMap = defaultdict(set)      # {usrId1, usrId2,..}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followerId in self.followMap[userId]:
            if followerId in self.tweets:
                index = len(self.tweets[followerId]) - 1
                count, tweetId = self.tweets[followerId][index]
                minHeap.append([count, tweetId, followerId, index - 1])     # add last frontier of each followerid to the minHeap
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followerId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[followerId][index]
                heapq.heappush(minHeap, [count, tweetId, followerId, index - 1])
        return res                

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
