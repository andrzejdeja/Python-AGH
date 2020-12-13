import json

#COMMANDS:
#del <nr>
#add <task> <time>
#exit
#show

def prnt(data):
    print("TODO list:")
    for i in range(len(data)):
        print("Nr:", i, "Name:", data[i]["task"], "Time:", data[i]["time"])
        
with open("data.json", "r") as f: #read from file
    data = json.load(f)

prnt(data)
while True:
    command = []
    command = input().strip().split()
    #print(command)
    if len(command) == 2 and command[0] == "del" and command[1].isdecimal():
        del data[int(command[1])]
    elif len(command) == 3 and command[0] == "add":
        data.append({"task": command[1], "time": command[2]})
    elif len(command) == 1 and command[0] == "exit":
        break
    elif len(command) == 1 and command[0] == "show":
        prnt(data)
    else:
        print("COMMANDS:")
        print("del <nr>")
        print("add <task> <time>")
        print("exit")
        
with open("data.json", "w") as f: #save to file
    json.dump(data, f)
