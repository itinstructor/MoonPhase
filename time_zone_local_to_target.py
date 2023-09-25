"""
    Filename: time_zone_local_to_target.py
    Description: Convert local computer timezone and time
    to destination timezone and time
"""

import datetime
import pytz

# Define the target timezone
target_timezone = pytz.timezone('US/Eastern')

# Get the current local time
local_time = datetime.datetime.now()

# Get the timezone information from the local computer
local_timezone = local_time.astimezone().tzinfo

# Get the current local time
local_time = datetime.datetime.now(local_timezone)

# Convert the local time to the target timezone
target_time = local_time.astimezone(target_timezone)

# Build display strings
local_str = local_time.strftime("%H:%M %m/%d/%Y")
target_str = target_time.strftime("%H:%M %m/%d/%Y")

# Print current computer time in local timezone
print(f'Current time {local_timezone}: {local_str}')

# Print the current time in target timezone
print(f'Current time {target_timezone}: {target_str}')
