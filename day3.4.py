print("---------Simple ATM Menu--------")

balance = int(input("enter balance: "))

if balance >= 5000:
    print("Premium Account")
elif balance >= 1000:
    print("Standard Account")
elif balance >= 1:
    print("Low Balance")
else:
    print("Account Empty")