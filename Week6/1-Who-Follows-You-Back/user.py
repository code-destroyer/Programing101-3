from directed_graph import DirectedGraph
import requests


class User:

    def __init__(self, username, level=0):
        self.resource = "https://api.github.com/users/{}".format(username)
        self.username = username
        self.level = level
        self.graph = DirectedGraph()

    def do_you_follow(self, user):
        return user in self.get_followings(self.username)

    def get_followings(self, user):
        user_resource = "https://api.github.com/users/{}".format(user)
        r = requests.get(user_resource + "/following").json()
        followings = [x["login"] for x in r]
        return followings

    def does_he_she_follows(self, user):
        return user in self.get_followers(self.username)

    def get_followers(self, user):
        user_resource = "https://api.github.com/users/{}".format(user)
        r = requests.get(user_resource + "/followers").json()
        followers = [x["login"] for x in r]
        return followers


def main():
    user = User("code-destroyer", 2)
    print(user.do_you_follow("lucifer666"))
    print(user.does_he_she_follows("RadoRado"))
    print(user.get_followers('code-destroyer'))


if __name__ == '__main__':
    main()
