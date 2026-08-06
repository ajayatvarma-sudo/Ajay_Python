# with open("employees.txt", "w") as file:
#     file.write("Ajay\n")
#     file.write("Rahul\n")
#     file.write("Priya\n")
#     file.write("Anita")
    

# with open("employees.txt", "r") as file:
#     for line in file:
#         print(f"Employee: {line.strip()}")


with open("employees.txt", "r") as file:
    for line in file:
        if line.strip():
            print(f"Employee: {line.strip()}")
