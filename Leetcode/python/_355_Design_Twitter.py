import heapq
import time
from typing import List


class User:
    def __init__(self, userId):
        self.userId = userId
        self.tweets = []
        self.followers = set()
        self.following = set()

    def __repr__(self):
        return f"User {{\n userId: {self.userId},\n tweets: {self.tweets},\n followers: {self.followers},\n following: {self.following}\n }}"

# Dicts, Heaps and Sorting - Time = O(n) - Space = O(n)
# the heap has a fixed size of 10 so it cuts down our time and space greatly
class Twitter:

    def __init__(self):
        self.users = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User(userId)

        self.users[userId].tweets.append((time.time(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []

        user = self.users[userId]

        maxHeap = []
        for i in range(len(user.tweets) - 1, -1, -1):
            if len(maxHeap) < 10:
                heapq.heappush(maxHeap, user.tweets[i])
            elif user.tweets[i][0] > maxHeap[0][0]:
                heapq.heappushpop(maxHeap, user.tweets[i])
            else:
                # Tweets are put into the list in chronological order so if current tweets time is
                # earlier than maxHeap's top elements time, then every element before this will also
                # be earlier so we dont need to look any further, so break
                break

        for followingId in user.following:
            following = self.users[followingId]
            for i in range(len(following.tweets) - 1, -1, -1):
                if len(maxHeap) < 10:
                    heapq.heappush(maxHeap, following.tweets[i])
                elif following.tweets[i][0] > maxHeap[0][0]:
                    heapq.heappushpop(maxHeap, following.tweets[i])
                else:
                    break

        sorted_heap = sorted(maxHeap, reverse=True)

        return [tweet for time, tweet in sorted_heap]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)

        self.users[followerId].following.add(followeeId)
        self.users[followeeId].followers.add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)

        self.users[followerId].following.discard(followeeId)
        self.users[followeeId].followers.discard(followerId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
