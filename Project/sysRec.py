import csv

class User(object):
    def __init__(self, id, name, ratings):
        self.id = int(id)
        self.name = name
        self.ratings = ratings

    def print(self):
        print(f'ID: {self.id} Nome: {self.name} Avaliações: {self.ratings}')


def getUsers(fileName):
    users = []
    with open(fileName, 'r') as usersFile:
        reader = csv.reader(usersFile)
        lines = list(reader)
        for line in range(1,10001):
            a = []
            for i in range(2, 12):
                a.append(lines[line][i])

            users.append(User(lines[line][0],lines[line][1], a))
    
    return users


def debug():
    users = getUsers('users.csv')
    for user in users:
        user.print()

debug()