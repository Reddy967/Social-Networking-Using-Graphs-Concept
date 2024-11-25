class User:
    def __init__(self, username):
        self.username = username
        self.connections = set()
        self.inbox = []
        self.posts = []

    def add_connection(self, other_user):
        self.connections.add(other_user)
        other_user.connections.add(self)
        print(f"{self.username} and {other_user.username} are now friends.")

    def create_post(self, content):
        post = {"content": content, "author": self.username}
        self.posts.append(post)
        print(f"{self.username} posted: '{content}'")

    def send_message(self, receiver, message):
        if receiver in self.connections:
            receiver.inbox.append((self.username, message))
            print(f"Message sent from {self.username} to {receiver.username}.")
        else:
            print(f"Cannot send message. {receiver.username} is not a friend of {self.username}.")

    
    def read_messages(self):
        if not self.inbox:
            print(f"{self.username} has no new messages.")
        else:
            print(f"{self.username}'s Messages:")
            for sender, message in self.inbox:
                print(f"From {sender}: {message}")
            self.inbox.clear()

    def get_feed(self):
        feed = []
        for friend in self.connections:
            feed.extend(friend.posts)
        feed.sort(key=lambda post: post['content'], reverse=True)
        print(f"{self.username}'s Feed:")
        for post in feed:
            print(f"{post['author']} posted: {post['content']}")
            
            
            
    