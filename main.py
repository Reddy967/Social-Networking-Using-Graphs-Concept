# main.py
from social_network import SocialNetwork

if __name__ == "__main__":
    network = SocialNetwork()
    network.add_user("Bharath")
    network.add_user("Narendra")
    network.add_user("Hemanth")
    network.add_user("Deelip")

    network.add_connection("Bharath", "Narendra")
    network.add_connection("Bharath", "Hemanth")
    network.add_connection("Narendra", "Deelip")

    # Friend Recommendations
    network.recommend_friends("Bharath")

    # Messages
    Bharath = network.users["Bharath"]
    Narendra = network.users["Narendra"]
    Bharath.send_message(Narendra, "Hello Narendra!")
    Narendra.read_messages()

    # Posts and Feed
    Bharath.create_post("Loving this social network!")
    Hemanth = network.users["Hemanth"]
    Hemanth.create_post("Enjoying the day.")
    Bharath.get_feed()

    # Connection Level
    network.find_connection_level("Bharath", "Deelip")
