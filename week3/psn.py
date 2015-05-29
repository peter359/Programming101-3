import json
special_symbols = ["!", "#", "$", "%", "^", "&", "*", "(", ")", "+", "-", "=", "{", "}", ":", "|", ">", "<", "?", "[", "]", ";", "'", "\\", ",", "/"]


class Panda:
    def get_index(self):
        for i in range(1, len(self.__email)):
            if self.__email[i] == "@":
                break
        return i

    def has_no_special_symbols(self):
        for x in special_symbols:
            if x in self.__email:
                return False
        return True

    def has_dot(self):
        return 1 == self.__email.count(".", self.get_index())

    def no_symbols(self):
        return not(len(self.__email) == len(self.__email[:self.get_index()]) + 1)

    def no_dot_after_at(self):
        return "." == self.__email[Panda.get_index(self) + 1]

    def has_letters(self):
        pass

    def __init__(self, name, email, gender):
        self.__name = str(name)
        self.__email = str(email)
        self.__gender = str(gender)
        if self.__gender not in ["male", "female"]:
            raise ValueError

    def name(self):
        return self.__name

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender

    def isMale(self):
        return self.__gender == "male"

    def isFemale(self):
        return self.__gender == "female"

    def __str__(self):
        return "I am {}, I am {}, pm me: {}".format(self.__name, self.__gender, self.__email)

    def __eq__(self, other):
        return self.__name == other.__name and self.__email == other.__email and self.__gender == other.__gender

    def __hash__(self):
        return hash(self.__name + self.__email + self.__gender)

    def to_json(self):
        return self.__repr__()


class PandaSocialNetwork:
    def __init__(self):
        self.psn = {}

    def __len__(self):
        return sum([1 for key in self.psn])

    def __getitem__(self, index):
        return self.psn[index]

    def has_panda(self, panda):
        return panda in self.psn

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise Exception("PandaAlreadyThere")
        self.psn[panda] = []

    def are_friends(self, panda1, panda2):
        return panda2 in self.psn[panda1]

    def make_friends(self, panda1, panda2):
        if panda1 not in self.psn:
            self.psn[panda1] = []
        if panda2 not in self.psn:
            self.psn[panda2] = []
        if self.are_friends(panda1, panda2):
            raise Exception("PandasAlreadyFriends")
        self.psn[panda1].append(panda2)
        self.psn[panda2].append(panda1)

    def friends_of(self, panda):
        if panda not in self.psn:
            return False
        return self.psn[panda]

    def panda_connections(self, panda):
        connections = {}
        q = []
        visited = set()
        q.append((0, panda))
        visited.add(panda)
        while len(q) != 0:
            panda_data = q.pop(0)
            current_level = panda_data[0]
            current_node = panda_data[1]
            connections[current_node] = current_level
            for neighbour in self.psn[current_node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append((current_level + 1, neighbour))
        return connections

    def connection_level(self, panda1, panda2):
        panda_table = self.panda_connections(panda1)
        if panda2 not in panda_table:
            return -1
        return panda_table[panda2]

    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1, panda2) >= 1:
            return True
        else:
            return False

    def genders_in_network(self, level, gender, panda):
        panda_table = self.panda_connections(panda)
        counter = 0
        for panda in panda_table:
            p_level = panda_table[panda]
            if p_level != 0 and p_level <= level and panda.gender() == gender:
                counter += 1
        return counter

    def __repr__(self):
        for_save = {}
        for panda in self.psn:
            friends = [repr(panda_friend) for panda_friend in self.psn[panda]]
            for_save[repr(panda)] = friends
        return json.dumps(for_save, indent=True)

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(self.__repr__())

    @staticmethod
    def load(filename):
        psn = PandaSocialNetwork()
        with open(filename, "r") as f:
            contents = f.read()
            json_network = json.loads(contents)

            for panda in json_network:
                if not psn.has_panda(panda):
                    psn.add_panda(panda)
                    for friends in json_network[panda]:
                        psn.make_friends(panda, friends)

        return psn
