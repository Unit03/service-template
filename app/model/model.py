class User(object):

    _users = []

    def __init__(self, name):
        self.name = name

    def save(self):
        User._users.append(self)

    def say_name(self):
        return self.name
