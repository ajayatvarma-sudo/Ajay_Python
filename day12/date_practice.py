from datetime import datetime, timedelta

# now = datetime.now()
# timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
# old = now - timedelta(days=7)

# print(f"Current: {timestamp}")
# print(f"7 days ago: {old}")

# start = datetime(2026, 8, 1)
# end = datetime(2026, 8, 11)

# difference = end - start

# print(f"{difference.days} days")

log_date = datetime(2026, 8, 3)
today = datetime(2026, 8, 11)

difference = today - log_date

print(f"{difference.days} days")

if difference.days >7:
    print("Log is older than 7 days")