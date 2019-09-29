import math

per1 = []
per2 = []

def manhattan(x1, x2, y1, y2):
    dist = (x1-x2)+(y1-y2)
    return dist

def euclidean(x1,x2,y1,y2):
    x = math.pow(x1-x2,2)
    y = math.pow(y1-y2,2)
    dist = math.sqrt(x+y)
    return dist

print("Hailey and Veronica: ")
print("Manhattan: "+ str(manhattan(4,5,4,3)))
print("Euclidean: "+ str(euclidean(4,5,4,3))) 