import csv
import math
import random
from operator import itemgetter
#from sortedcontainers import SortedDict


class User(object):  # cria a classe usuário
    def __init__(self, id, name, ratings):  # define o construtor da classe usuário
        self.id = int(id)
        self.name = name
        self.ratings = ratings

    def getRatings(self):
        return self.ratings

    def print(self):  # imprime os dados do usuário
        return(f'ID: {self.id} || Nome: {self.name} || Avaliações: {self.ratings}')


class Similarity(object):
    def __init__(self, id1, id2, category, sim):
        self.id1 = id1
        self.id2 = id2
        self.category = category
        self.sim = sim

    def getSim(self):
        return (f'Usuarios {self.id1} e {self.id2}, Tipo: {self.category}, Taxa de Similaridade: {self.sim}')


def getUsers(fileName):  # função para recurepar os dados do .csv e colocar num array da classe usuario
    users = []
    with open(fileName, 'r') as usersFile:  # abre o csv no modo leitura
        # cria um leitor de csv com o arquivo aberto em modo leitura
        reader = csv.reader(usersFile)
        # transcreve todas as linhas o csv pra um vetor separando os campos diferentes
        lines = list(reader)
        for line in range(1, len(lines)):  # for que percorre todo o csv menos o cabeçalho
            a = []  # variável auxiliar que vai receber os usuarios instanciados
            # pega todas as classificações (colunas de 3 a 12) e coloca num vetor
            for i in range(2, 12):
                # adiciona as classificações em ordem num vetor
                a.append(int(lines[line][i]))

            # instancia e adiciona no vetor um objeto da classe usuario
            users.append(User(lines[line][0], lines[line][1], a))

    return users  # retorna um vetor de usuários instanciados e suas avalizações


def searchUser(id, users):
    first = 0
    last = len(users)
    middle = 0
    found = False

    while (first <= last and found != True):
        middle = (math.ceil((first + last)/2))
        uID = users[middle].id

        if(uID == id):
            found = True

        elif(id < uID):
            last = middle - 1

        else:
            first = middle + 1

    if (found):
        return users[middle]
    else:
        return False


def getPearson(user1, user2):
    sumXY = 0
    sumX = 0
    sumY = 0
    sumX2 = 0
    sumY2 = 0

    x = user1.getRatings()
    y = user2.getRatings()

    n = len(x)

    for i in range(n):
        sumXY += x[i] * y[i]
        sumX += x[i]
        sumY += y[i]
        sumX2 += math.pow(x[i], 2)
        sumY2 += math.pow(y[i], 2)

    over = sumXY - ((sumX*sumY)/n)

    under1 = math.sqrt(sumX2-(math.pow(sumX, 2)/n))
    under2 = math.sqrt(sumY2-(math.pow(sumY, 2)/n))

    under = under1 * under2

    return (over/under)


def getCosine(user1, user2):
    sumXY = 0
    sumX2 = 0
    sumY2 = 0
    x = user1.getRatings()
    y = user2.getRatings()

    for i in range(len(x)):
        sumXY += x[i]*y[i]
        sumX2 += math.pow(x[i], 2)
        sumY2 += math.pow(y[i], 2)

    ret = math.sqrt(sumX2)*math.sqrt(sumY2)

    if (ret != 0):
        ret = (sumXY/(math.sqrt(sumX2)*math.sqrt(sumY2)))
    else:
        ret = -1
    return ret


def getNeighbours(id, k, users):
    neighbours = {}
    neig = []
    usr = searchUser(id, users)

    for user in users:
        if (id != user.id):
            sim = getCosine(usr, user)
            #sims = Similarity(usr.id,user.id,'Cosseno',sim)
            neighbours[user.id] = sim

    n = sorted(neighbours.items(), reverse=True, key=lambda x: x[1])

    for a in range(k):
        neig.append(searchUser(int(n[a][0]), users))

    return neig


def recommend(id, users, k):

    usr = searchUser(id, users).ratings
    nei = getNeighbours(id, k, users)

    recommendation = []

    for i in range(k):
        for j in range(len(usr)):
            if (usr[j] == 0 and nei[i].ratings[j] > 0):
                rec = (f'Show {j + 1}')
                if rec not in recommendation:
                    #print(f'usr[j] == {usr[j]} j == {j} nei[i].ratings[j] == {nei[i].ratings[j]}')
                    recommendation.append(rec)

    return recommendation

def debug():
    users = getUsers('users.csv')
    #sims = []
    #user = users[0]
    # for i in range(1, len(users)):
    #    simi = getCosine(user, users[i])
    #    sims.append(Similarity('1', users[i].id, 'Cosseno', simi))

    # for s in sims:
    #    print(s.getSim())
    # print(searchUser(random.randint(0,9999),users).print())
    # print(searchUser(51834,users))

    #user3 = User('01', 'Cadu', [4.75, 4.5, 5, 4.25, 4])
    #user4 = User('02', 'Gabe', [4, 3, 5, 2, 1])
    #sim = Similarity(user3.id, user4.id, 'Cossenos', getCosine(user3, user4))

    # print(sim.getSim())

    #n = getNeighbours(9574, 5, users)
    #sort = SortedDict(n)
    #print(searchUser(9574, users).ratings)
    #for a in n:
    #   print(a.ratings)
    users = getUsers('users.csv')
    print('Digite o ID de um usuário para realizar uma recomendação: ')
    uid = int(input())
    print('Digite um valor para K para enconrar os vizinhos mais próximos: ')
    k = int(input())
    u = searchUser(uid,users)
    rec = recommend(uid, users, k)

    print(f'Para o usuario {u.name} são: {rec}')

    
debug()
