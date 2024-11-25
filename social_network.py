# social_network.py
from collections import deque
from user import User

class SocialNetwork:
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        if username in self.users:
            print(f"{username} already exists.")
        else:
            self.users[username] = User(username)
            print(f"User {username} added to the network.")

    def add_connection(self, username1, username2):
        if username1 in self.users and username2 in self.users:
            user1 = self.users[username1]
            user2 = self.users[username2]
            user1.add_connection(user2)
        else:
            print(f"One or both users '{username1}' and '{username2}' do not exist.")

    def recommend_friends(self, username):
        if username not in self.users:
            print(f"User '{username}' does not exist.")
            return []

        user = self.users[username]
        recommendations = {}
        
        for friend in user.connections:
            for mutual in friend.connections:
                if mutual != user and mutual not in user.connections:
                    recommendations[mutual.username] = recommendations.get(mutual.username, 0) + 1

        recommended_friends = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
        
        print(f"Friend recommendations for {username}: {[u for u, _ in recommended_friends]}")
        return recommended_friends

    def find_connection_level(self, username1, username2):
        if username1 not in self.users or username2 not in self.users:
            print("One or both users do not exist.")
            return -1

        visited = set()
        queue = deque([(self.users[username1], 0)])

        while queue:
            current_user, level = queue.popleft()
            if current_user.username == username2:
                print(f"Connection level between {username1} and {username2} is {level}.")
                return level

            visited.add(current_user)
            for friend in current_user.connections:
                if friend not in visited:
                    queue.append((friend, level + 1))

        print(f"No connection found between {username1} and {username2}.")
        return -1
