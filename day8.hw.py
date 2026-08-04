server  = {
    "hostname": "app01",
    "status": "Running",
    "cpu": 35,
    "memory": 68,
    "location": "Hyderabad"
}

for keys in server.keys():
    print(keys)

for values in server.values():
    print(values)

for key, values in server.items():
    print(key, values)

server["cpu"]=48
server["environment"]="Production"
for key, values in server.items():
    print(key, ":", values)

