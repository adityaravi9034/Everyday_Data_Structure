"""You are tasked with designing a social media platform. Users can create accounts, post messages, follow other users, and view posts from the users they follow.
Each post has a timestamp associated with it.

Design a data structure and implement the necessary functions to support the social media platform. 
The data structure should store information about users, posts, and their relationships (followers/following). Additionally, the functions
should include the ability -to create user accounts, post messages, follow/unfollow users, and retrieve posts from followed users in chronological order.

Write a class SocialMediaPlatform that represents the social media platform. The class should include the following methods:

create_user(username): Creates a new user account with the given username.
post_message(username, message): Posts a message from the specified user.
follow_user(follower_username, following_username): Adds a following relationship between the follower and the user being followed.
unfollow_user(follower_username, following_username): Removes the following relationship between the follower and the user being unfollowed.
get_timeline(username): Returns the list of posts from the users that the specified user follows in chronological order.
You can assume that usernames are unique within the platform.

Implement the SocialMediaPlatform class with the above methods, along with any additional helper methods or data structures you may need.

Note: You do not need to handle edge cases such as input validation or error handling in this implementation."""


class SocialMediaPlatform:
    def __init__(self):
        self.users = {}
        self.posts = []

    def create_user(self, username):
        self.users[username] = set()

    def post_message(self, username, message):
        post = {"username": username, "message": message}
        self.posts.append(post)

    def follow_user(self, follower_username, following_username):
        if follower_username in self.users:
            self.users[follower_username].add(following_username)

    def unfollow_user(self, follower_username, following_username):
        if follower_username in self.users:
            if following_username in self.users[follower_username]:
                self.users[follower_username].remove(following_username)

    def get_timeline(self, username):
        timeline = [post for post in self.posts if post["username"] in self.users[username]]
        timeline.sort(key=lambda x: x["timestamp"])
        return timeline

# Example usage:
social_media = SocialMediaPlatform()

# Create user accounts
social_media.create_user("user1")
social_media.create_user("user2")
social_media.create_user("user3")

# Post messages
social_media.post_message("user1", "Hello world!")
social_media.post_message("user2", "Great day today!")
social_media.post_message("user1", "I love social media!")

# Follow users
social_media.follow_user("user1", "user2")
social_media.follow_user("user1", "user3")

# Get the timeline for a user
timeline = social_media.get_timeline("user1")
print("Timeline for user1:")
for post in timeline:
    print(post["username"], ":", post["message"])
