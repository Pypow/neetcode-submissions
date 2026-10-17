class Twitter:

    def __init__(self):
        self.post = {}  # userId: [count, tweetId]
        self.followers = {} # followerId: SET {followeeId}
        self.count = 0      # IMP: use this to track 

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.post:
            self.post[userId] = []
        self.post[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []    # recent posts from all followers
        followList = self.followers[userId] if userId in self.followers else set()
        followList = set(followList.copy())
        followList.add(userId)
        res = []        # list of tweetId
        for fid in followList:
            if fid in self.post and self.post[fid]:
                count, tweetId = self.post[fid][-1]     # get latest tweet
                nextIdx = len(self.post[fid]) - 2
                heapq.heappush(maxHeap, (count, tweetId, fid, nextIdx))
        
        while maxHeap:
            count, tweetId, fid, nextIdx = heapq.heappop(maxHeap)
            res.append(tweetId)
            if len(res) >= 10:
                return res
            if nextIdx >= 0:
                count, tweetId = self.post[fid][nextIdx]
                heapq.heappush(maxHeap, (count, tweetId, fid, nextIdx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            return
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
