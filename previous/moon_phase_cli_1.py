"""
    Name: moon_phase_cli_1.py
    Author: William A Loring
    Created: 07-08-23
    Purpose: Python moon phase program using ephem library
"""

import os
# pip install epmem
import ephem
"""The phase of the moon is returned as a fraction,
0.0 being a New Moon, 0.125 waxing crescent
0.25 being a First Quarter, 0.325 waxing gibbous
0.5 being a Full Moon, .625 waning gibbous
0.75 being a Last Quarter, 0.825 waning cresent
and 1.0 being a New Moon again.
"""
description = [
    "New (totally dark)",
    "Waxing Crescent (increasing to full)",
    "First Quarter (increasing to full)",
    "Waxing Gibbous (increasing to full)",
    "Full Moon (full light)",
    "Waning Gibbous (decreasing from full)",
    "Last Quarter (decreasing from full)",
    "Waning Crescent (decreasing from full)"
]


def moon_phase_to_description(phase):
    # Convert moon phase to description
    # from 0 (the new moon) to 0.5 (the full moon)
    # and back to 1 (the next new moon)
    if (phase <= 0.02):
        moon_description = description[0]
    elif (phase <= 0.23):
        moon_description = description[1]
    elif (phase <= 0.2839):
        moon_description = description[2]
    elif (phase <= .4661):
        moon_description = description[3]
    elif (phase <= 0.5339):
        moon_description = description[4]
    elif (phase <= 0.7161):
        moon_description = description[5]
    elif (phase <= 0.7839):
        moon_description = description[6]
    elif (phase <= 1.0):
        moon_description = description[7]
    return moon_description


# Define the observer's location Scottsbluff NE
observer = ephem.Observer()
observer.lat = '41.8666'
observer.long = '-103.6672'

# Define the date yyyy/mm/dd
# observer.date = '2023/07/9'

# Get current date and time
date = ephem.now()
# Convert to local time
local_time = ephem.localtime(date)

# Time from on Windows modified by #
if os.name == "nt":
    formatted_time = local_time.strftime(" %#I:%M %p %#m/%#d/%Y")
# Time format on Linux modified by -
else:
    formatted_time = local_time.strftime(" %-I:%M %p %-m/%-d/%Y")

print(f" {formatted_time}")

# Create moon object from local time
moon = ephem.Moon(local_time)

# Calculate moon information based on observer information
moon.compute(observer)

# Distance from earth to the moon
earth_to_moon = moon.earth_distance
print(f"    AU: {earth_to_moon}")
km_to_moon = 149597870.7 * earth_to_moon
print(f"    KM: {km_to_moon:,.0f}")
miles_to_moon = earth_to_moon * 92955807.273
print(f" Miles: {miles_to_moon:,.0f}")


# Surface illumination of the moon from 0.0 to 1.0
phase = moon.moon_phase
phase_percent = moon.phase

moon_description = moon_phase_to_description(phase)

print(f" {phase_percent:.0f} % light {moon_description}")

print()
input(" Press any key to exit")
