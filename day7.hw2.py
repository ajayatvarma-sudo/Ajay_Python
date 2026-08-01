def calculator(a, b, operation="+"):
    if operation=="+":
        return a+b
    elif operation=="-":
        return a-b
    elif operation=="*":
        return a*b
    else:
        return a/b

result =calculator(10, 5, "*")

print(result)