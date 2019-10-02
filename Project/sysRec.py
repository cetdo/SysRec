import csv

class User(object): #cria a classe usuário
    def __init__(self, id, name, ratings): #define o construtor da classe usuário
        self.id = int(id)
        self.name = name
        self.ratings = ratings

    def print(self): #imprime os dados do usuário
        print(f'ID: {self.id} Nome: {self.name} Avaliações: {self.ratings}')


def getUsers(fileName): # função para recurepar os dados do .csv e colocar num array da classe usuario
    users = []
    with open(fileName, 'r') as usersFile: # abre o csv no modo leitura
        reader = csv.reader(usersFile) # cria um leitor de csv com o arquivo aberto em modo leitura
        lines = list(reader) # transcreve todas as linhas o csv pra um vetor separando os campos diferentes
        for line in range(1,10001): #for que percorre todo o csv menos o cabeçalho
            a = [] # variável auxiliar que vai receber os usuarios instanciados
            for i in range(2, 12): # pega todas as classificações (colunas de 3 a 12) e coloca num vetor
                a.append(lines[line][i]) # adiciona as classificações em ordem num vetor

            users.append(User(lines[line][0],lines[line][1], a)) # instancia e adiciona no vetor um objeto da classe usuario
    
    return users # retorna um vetor de usuários instanciados e suas avalizações


def debug():
    users = getUsers('users.csv')
    for user in users:
        user.print()

debug()