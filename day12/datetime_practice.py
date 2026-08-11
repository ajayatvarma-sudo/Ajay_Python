# from datetime import datetime

# now = datetime.now()

# print(now)
# print(now.date())
# print(now.time())

# print(now.strftime("%d-%m-%Y"))
# print(now.strftime("%H:%M:%S"))
# print(now.strftime("%d-%m-%Y %H:%M:%S"))


from datetime import datetime
now = datetime.now()
tyme = now.strftime("%d-%m-%Y %H:%M:%S")
print(f"[{tyme}] Health check started")
print(f"[{tyme}] Server status: UP")
