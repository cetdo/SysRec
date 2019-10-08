import csv, random

def indexing():
    with open('users.csv', 'r') as readFile: #abre o arquivo como um arquivo tipo texto
        reader = csv.reader(readFile) #digo que é um csv
        lines = list(reader) # coloco cada linha do arquivo em um vetor (essencialmente vira uma matriz)
        for index in range(1, len(lines)): # percorro todas as linhas do arquivo
            if index > 0:   # garantindo que não vou modificar a primeira linha que contém o nome dos campos
                lines[index][0] = index # cria um índice único para cada usuário e coloca na primeira coluna do csv
    
    with open('users.csv', 'w') as writeFile: # abre o arquivo no modo escrita
        writer = csv.writer(writeFile) # diz que o arquivo aberto é um arquivo csv para escrita
        writer.writerows(lines) # sobrescreve as linhas do arquivo
    readFile.close() # fecha o arquivo em modo leitura
    writeFile.close() # fecha o arquivo no modo escrita
    return index # retorna a matriz com os dados do csv

def rating():
    with open('users.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        watched = [True, False] # vetor com 2 opções que vai ser utilizado para decidir se o usuario viu ou não o show
        for index in range(1,len(lines)):
            if index > 0:
                for show in range(10):
                    if(random.choice(watched)): # escolhe aleatoriamente se o usuario viu ou não o show
                        lines[index][show+2] = random.randint(1,100) # diz quanto do show o usuario viu
                    else:
                        lines[index][show+2] = 0 # se ele não viu o show zera o valor
    
    with open('users.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    readFile.close()
    writeFile.close()

def main():
    users = indexing()
    rating()
    print(f'{users - 1} foram processados')

main()