import math

patients = {"Jose":[30,95,205,119,'S'], "Maria": [25,58,160,60,"N"],
            "Pedro": [50,73,150,70,"N"], "Francisco": [28,102,200,123,"S"],
            "Isabel": [60,80,204,90,"S"]}
new_patient = {"Joao": [36,65,140,75]}

#for pat in patients:
#    print(str(pat + str(patients[pat])))

#print(new_patient)

#print(new_patient["Joao"])


def eucledean(person1, person2):
    a = 0
    for i in range(4):
        a += math.pow(person1[i] - person2[i],2)
    
    a = math.sqrt(a)

    return a

def getNearests(patients, new_patient, k):
    aux = {}
    for name in patients:
        aux[name]= eucledean(patients[name],new_patient["Joao"])
    return aux

print(getNearests(patients, new_patient, 3))

#print(eucledean(patients["Jose"],patients["Isabel"]))