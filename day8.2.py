employee = {
    "name": "Ajay",
    "role": "Production Support",
    "experience": 4,
    "salary": 150000,
    "location": "Hyderabad"
}

employee["company"] = "MassMutual"

employee["salary"]= 180000
print("Employee Details")
print("-------------------")

for key, value in employee.items():
    print(key, ":", value)

