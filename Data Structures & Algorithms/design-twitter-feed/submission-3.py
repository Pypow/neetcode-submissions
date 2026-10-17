class Twitter:

    def __init__(self):
        self.count = 0
        self.followers = defaultdict(set)   # userId: set of (followerIds)
        self.posts = defaultdict(list)      # userId: tuple of (count, tweetIds)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.count, tweetId])
        self.count -= 1             # for maxHeap

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        followers = self.followers[userId]
        followers.add(userId)
        for usr in followers:
            if usr in self.posts:
                index = len(self.posts[usr]) - 1
                count, post = self.posts[usr][index]
                maxHeap.append([count, post, usr, index - 1])
        heapq.heapify(maxHeap)
        while maxHeap and len(res) < 10:
            count, post, usr, index = heapq.heappop(maxHeap)
            res.append(post)
            if index >= 0:
                count, post = self.posts[usr][index]
                heapq.heappush(maxHeap, [count, post, usr, index-1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
