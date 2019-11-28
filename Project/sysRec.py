import csv
import math
from fuzzywuzzy import fuzz

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

class Anime(object):
    def __init__(self, id, name, genre, media, episodes, rating, views):
        self.id = int(id)
        self.name = name
        self.genre = genre
        self.media = media
        self.rating = rating
        self.views = views

    def print(self):
        return(f'ID: {self.id} || Nome: {self.name} || Gêneros: {self.genre}')

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

def getAnimes(fileName):
    animes = []
    with open(fileName, 'r') as animeFile:
        reader = csv.reader(animeFile)

        lines = list(reader)
        for line in lines:
            animes.append(Anime(line[0],line[1], line[2], line[3], line[4], line[5], line[6]))
            

    return animes

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

def searchAnime(id, animes):
    first = 0
    last = len(animes)
    middle = 0
    found = False

    while (first <= last and found != True):
        middle = (math.ceil((first + last)/2))
        aID = animes[middle].id

        if(aID == id):
            found = True

        elif(id < aID):
            last = middle - 1

        else:
            first = middle + 1

    if (found):
        return animes[middle]
    else:
      return False

def wightedAverage(anime1, anime2):

    
    totWeight = (3 + 5 + 1 + 3 + 3)
    acmSim = 0
    acmSim += fuzz.token_sort_ratio(anime1.name, anime2.name) * 3
    acmSim += fuzz.token_sort_ratio(anime1.genre, anime2.genre) * 5
    acmSim += fuzz.token_sort_ratio(anime1.media, anime2.media) * 1
    acmSim += fuzz.token_sort_ratio(anime1.rating, anime2.rating) * 3
    acmSim += fuzz.token_sort_ratio(anime1.views, anime2.views) * 3

    return (acmSim / totWeight * 1.0)

def getNeighbours(id, k, animes):
    neighbours = {}
    neig = []
    ani = searchAnime(id, animes)

    for anime in animes:
        if (id != anime.id):
            sim = wightedAverage(ani, anime)
            #sims = Similarity(usr.id,user.id,'Cosseno',sim)
            neighbours[anime.id] = sim

    n = sorted(neighbours.items(), reverse=True, key=lambda x: x[1])

    for a in range(k):
        neig.append(searchAnime(int(n[a][0]), animes))

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

def main():

    '''users = getUsers('users.csv')
    print('Digite o ID de um usuário para realizar uma recomendação: ')
    uid = int(input())
    print('Digite um valor para K para encontrar os vizinhos mais próximos: ')
    k = int(input())
    u = searchUser(uid,users)
    rec = recommend(uid, users, k)

    print(f'Para o usuario {u.name} são: {rec}')'''


    animes = getAnimes('anime.csv')

    print("Digite o ID de um anime para realizar a recomendação: ")
    aid = int(input())
    print("Digite um valor para K para encontrar os vizinhos mais próximos: ")
    k = int(input())
    ## a = searchAnime(aid, animes)
    rec = getNeighbours(aid, k, animes)
    for r in rec:
        print(r.print())

    """a1 = searchAnime(1, animes)
    a2 = searchAnime(5, animes)

    print(wightedAverage(a1,a2))
"""
main()
