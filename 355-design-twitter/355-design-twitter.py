class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = collections.defaultdict(list)
        self.followerMap = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followerMap[userId].add(userId)
        for followeeID in self.followerMap[userId]:
            if followeeID in self.tweetMap:
                index = len(self.tweetMap[followeeID]) - 1
                count, tweetID = self.tweetMap[followeeID][index]
                minHeap.append([count, tweetID, followeeID, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetID, followeeID, index = heapq.heappop(minHeap)
            res.append(tweetID)
            if index >= 0:
                count, tweetID = self.tweetMap[followeeID][index]
                heapq.heappush(minHeap, [count, tweetID, followeeID, index - 1])
                
        return res
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)