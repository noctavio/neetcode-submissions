class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # defaultdict sets all map values to 0
        self.followMap = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        # return all tweets by userID as a list of integer IDs
        result = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1 # final value in map
                count, twtId = self.tweetMap[followeeId][index]
                minHeap.append([count, twtId, followeeId, index - 1])
            heapq.heapify(minHeap)
        while minHeap and len(result) < 10:
            count, twtId, followeeId, index = heapq.heappop(minHeap)
            result.append(twtId)
            if index >= 0:
                count, twtId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, twtId, followeeId, index - 1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        # append ID to a class member list?
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)