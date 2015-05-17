import re
import json


class Panda:

    def __init__(self, name, email, gender):
        self.name = name
        self.gender = gender
        self.set_email(email)

    def get_name(self):
        return self.name

    def __str__(self):
        return "The panda name, email and gender are {}, {} and {}".format(self.name, self.email, self.gender)

    def __eq__(self, other):
        equal_names = self.name == other.name
        equal_emails = self.email == other.email
        equal_genders = self.gender == other.gender
        return equal_names and equal_emails and equal_genders

    def __repr__(self):
        return "The panda name, email and gender are {}, {} and {}".format(self.name, self.email, self.gender)

    def set_email(self, email):
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            raise ValueError
        self.email = email

    def gender(self):
        return self.gender

    def isMale(self):
        return self.gender.lower() == "male"

    def isFemale(self):
        return self.gender.lower() == "female"

    def __hash__(self):
        return hash(self.name + self.email + self.gender)

ivo = Panda("Ivo", "ivo@pandamail.com", "male")
alf = Panda("Ivan", "Ceco@abv.bg", "male")


class PandaAlreadyThere:
    pass


class PandasAlreadyFriends:
    pass


class PandaSocialNetwork:

    def __init__(self):
        self.network_pandas = {}

    def add_panda(self, panda):
        if panda in self.network_pandas:
            raise PandaAlreadyThere
        else:
            self.network_pandas[panda] = []


    def has_panda(self, panda):
        if panda in self.network_pandas:
            return True
        return False

    def are_friends(self, panda1, panda2):
        if panda1 in self.network_pandas[panda2] and panda2 in self.network_pandas[panda1]:
            return True
        return False

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        if self.are_friends(panda1, panda2):
            raise PandasAlreadyFriends
        else:
            self.network_pandas[panda1].append(panda2)
            self.network_pandas[panda2].append(panda1)

    def friends_of(self, panda):
        if panda not in self.network_pandas:
            return False
        return self.network_pandas[panda]


    """
    1<->2
    1<->3
    2<->4
    4<->5
    5<->1
    6<->4
    3<->6
    7<->7
    7<->8
    9<->8
    10<->9
    10<->1

    """

    graph = {
        "1": ["2", "3", "5"],
        "2": ["4", "1"],
        "3": ["1", "6"],
        "4": ["2", "5", "6"],
        "5": ["4", "1"],
        "6": ["3", "4", "7"],
        "7": ["6", "8"],
        "8": ["7", "9"],
        "9": ["8", "10"],
        "10": ["9"],
        "11": ["12"],
        "12": ["11"]
    }


    def connection_level(self, panda1, panda2):  # graph=network, start=panda1, end=panda2, bfs=connection_level
        visited = set()
        queue = []
        # path_to[x] = y
        # if we go to x through y
        path_to = {}
        queue.append(panda1)
        visited.add(panda1)
        path_to[panda1] = None
        found = False
        path_length = 0
        # obhojdane v dulbochina(kogato imame nasochen put/izpolzva se stek)
        # obhojdane v shirochinna(kogato imame dvuposochen put)
        while len(queue) != 0:
            current_node = queue.pop(0)
            if current_node == panda2:
                found = True
                break
            for neighbour in self.network_pandas[current_node]:
                if neighbour not in visited:
                    path_to[neighbour] = current_node
                    visited.add(neighbour)
                    queue.append(neighbour)
        if found:
            while path_to[panda2] is not None:
                path_length += 1
                panda2 = path_to[panda2]
        # print(json.dumps(path_to, sort_keys=True, indent=4))
        return path_length

    def are_connected(self, panda1, panda2):
        level_of_connection = PandaSocialNetwork.connection_level(self, panda1, panda2)
        return level_of_connection > 0

    def how_many_genders_in_network(self, level, panda, gender):
        counter = 0
        for curr_panda in self.network_pandas.keys():
            if curr_panda != panda:
                if self.connection_level(panda, curr_panda) == level:
                    if curr_panda.gender == gender:
                        counter += 1
        return counter

    def save_json(self):
        with open("pandas.json", "w") as file:
            json.dump(self.network_pandas, file)


network = PandaSocialNetwork()

ivo = Panda("Ivo", "ivo@pandamail.com", "male")
rado = Panda("Rado", "rado@pandamail.com", "male")
tony = Panda("Tony", "tony@pandamail.com", "female")

for panda in [ivo, rado, tony]:
    network.add_panda(panda)

print(network.make_friends(ivo, rado))
print(network.make_friends(rado, tony))

print(network.connection_level(ivo, rado)) == 1 # True
print(network.connection_level(ivo, tony)) == 2 # True
print(network.save_json())
