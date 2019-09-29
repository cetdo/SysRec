import csv, random


def indexing():
    with open('users.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        for index in range(10001):
            if index > 0:
                lines[index][0] = index
    
    with open('users.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    readFile.close()
    writeFile.close()
    return lines

def rating():
    with open('users.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        watched = [True, False]
        for index in range(10001):
            if index > 0:
                for show in range(10):
                    if(random.choice(watched)):
                        lines[index][show+3] = random.randint(0,100)
                    else:
                        lines[index][show+3] = 0
    
    with open('users.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    readFile.close()
    writeFile.close()

def readingAsDictonary():
    with open('users.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count +=1
            print(f'\t{row["name"]}, {row["sex"]}')
            line_count += 1
        print(f'Processed {line_count} lines.')

        csv_file.close()
    return csv_reader

def main():
    users = indexing()
    rating()
    print(users[1])

main()