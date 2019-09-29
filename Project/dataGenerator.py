with open("users.csv") as original:
    head = [next(original) for x in range(10001)]
#print(head)
newUsers = open("nUsers.csv","w")

newUsers.writelines(head)
newUsers.close

