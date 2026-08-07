# with open("notes.txt", "a") as file:
#     file.write("\nPython is Awesome\n")
#     file.write("Practice makes Perfect")

# with open("notes.txt", "r") as file:
#     print(file.read())


# with open("notes.txt", "r") as file:
#     for line in file:
#         print(line.strip())


# with open("notes.txt", "r") as file:
#     count = 0
#     for line in file:
#         count = count + 1
# print(f"Total lines: {count}")

# total_words = 0
# with open("notes.txt", "r") as file:
#     for line in file:
#         words = line.split()
#         total_words= total_words+len(words)

# print(total_words)
count=0
with open("notes.txt", "r") as file:
    for line in file:
        words = line.split()
        for i in words:
            if i == "Python":
                count= count + 1
print(f"Python appears {count} times")