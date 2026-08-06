name = input("Enter your name: ")
city = input("Enter your city: ")

with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("City: " + city)
    