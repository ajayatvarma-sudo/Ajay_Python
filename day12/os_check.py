import os

# print(os.listdir())

# print(os.path.exists("calculator.py"))
if os.path.exists("error.log"):
    print("Error log found")
else:
    print("Error log not found")
