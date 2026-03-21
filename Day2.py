file=open("data.txt")
users=[]
for line in file:
    data = line.split(",")
    name = data[0]
    age = int(data[1].strip())

    users.append({"name": name, "age": age})
file.close()
print(users)