class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)       # userID: list of [count, TweetID]
        self.followers = defaultdict(set)     # userID: set of followerID
        self.count = 0          # global count to track order of tweets


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.followers[userId]
        followers.add(userId)
        res = []    # tweetids
        maxHeap = []
        for fid in followers:
            if len(self.tweets[fid]):
                index = len(self.tweets[fid]) - 1
                count, tweetId = self.tweets[fid][index]
                heapq.heappush(maxHeap, (count, tweetId, index - 1, fid))

        while maxHeap and len(res) < 10:
            count, tweetId, index, fid = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[fid][index]
                heapq.heappush(maxHeap, (count, tweetId, index - 1, fid))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
