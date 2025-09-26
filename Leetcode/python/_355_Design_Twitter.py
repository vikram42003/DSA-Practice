import heapq
import time
from typing import List


# Linked Lists and Heaps - Time = O(n log n) - Space = O(n)
# Store the tweets as linked lists and then when getting the top 10 latest, put the heads of users tweets and all followers tweets in a max heap
# and then pop the first 10, that will be the top 10 latest tweets, and we'll only count 10 times
# The Space and time are O(n log n) and O(n) only because we're using heaps and may do heap operations n times, and we store heaps and linked lists,
# and thats n space taken
class User:
    def __init__(self, userId):
        self.userId = userId
        self.tweets = None
        self.followers = set()
        self.following = set()

    def __repr__(self):
        return f"User {{\n userId: {self.userId},\n tweets: {self.tweets},\n followers: {self.followers},\n following: {self.following}\n }}"

    def addTweet(self, time, tweetId):
        # We store each tweet as latest tweet first
        if not self.tweets:
            self.tweets = Tweet(time, tweetId)
            return

        newTweet = Tweet(time, tweetId)
        newTweet.next = self.tweets
        self.tweets = newTweet


class Tweet:
    def __init__(self, time, tweetId):
        self.time = time
        self.tweetId = tweetId
        self.next = None


class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User(userId)

        self.users[userId].addTweet(self.time, tweetId)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []

        user = self.users[userId]
        following = user.following

        maxHeap = []

        # Put the heads of user.tweets and following user's tweets
        if user.tweets:
            heapq.heappush(maxHeap, (-user.tweets.time, user.tweets))
        for followingId in following:
            f = self.users[followingId]
            if f.tweets:
                heapq.heappush(maxHeap, (-f.tweets.time, f.tweets))

        ans = []
        i = 0
        while i < 10 and maxHeap:
            # Pop the top one 10 times, that'll give us the top 10 tweets
            popped = heapq.heappop(maxHeap)
            ans.append(popped[1].tweetId)

            nextOne = popped[1].next
            if nextOne:
                heapq.heappush(maxHeap, (-nextOne.time, nextOne))

            i += 1

        return ans

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
