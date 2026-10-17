class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)    # userid: [list of count, tweets]
        self.followerMap = defaultdict(set) # 
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []
        followers = self.followerMap[userId]
        followers.add(userId)
        for followerId in followers:
            if len(self.tweetMap[followerId]):
                index = len(self.tweetMap[followerId]) - 1
                count, tweetId = self.tweetMap[followerId][index]
                maxHeap.append([count, tweetId, index - 1, followerId])
        heapq.heapify(maxHeap)
        k = 10
        while maxHeap and k > 0:
            count, tweetId, index, followerId = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followerId][index]
                heapq.heappush(maxHeap, [count, tweetId, index - 1, followerId])
            k -= 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)     
