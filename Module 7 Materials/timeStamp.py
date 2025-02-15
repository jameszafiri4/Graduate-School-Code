# much of this is from https://pynative.com/python-timestamp/
from datetime import datetime

# Getting the current date and time
dt = datetime.now()

# getting the timestamp
ts = datetime.timestamp(dt)

print("Date and time is:", dt)
print("Timestamp is:", ts)

# date in string format
birthday = "01.01.2000 09:12:34"

# convert to datetime instance
date_time = datetime.strptime(birthday, '%d.%m.%Y %H:%M:%S')

# timestamp in milliseconds
ts = date_time.timestamp() * 1000
print(f"The timestamp of {birthday} in ms is {ts}")
