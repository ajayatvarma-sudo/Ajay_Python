with open("logs.txt", "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())     ##strip() will remove extra lines from \n
