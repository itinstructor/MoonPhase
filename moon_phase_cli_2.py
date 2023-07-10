"""
    Name: moon_phase_cli_2.py
    Author: William A Loring
    Created: 07-08-23
    Purpose: Python moon phase program using ephem library
"""

import os
# pip install epmem
import ephem
import geocode_geopy
import moon_class


class MoonPhase:
    def __init__(self) -> None:
        # Create moonclass object to access methods
        self.moon_class = moon_class.MoonClass()

        # Get location input from user
        city = input(" Enter city: ")
        state = input(" Enter state: ")
        country = input(" Enter country: ")

        # Get location lat, lng, and address from geopy
        # NWS is US only
        self.lat, self.lng, self.address = geocode_geopy.geocode(
            city, state, country)
        print(f" {self.address}")

        observer = ephem.Observer()
        observer.lat = self.lat
        observer.long = self.lng

        # Get current date and time
        date = ephem.now()
        # Convert to local time
        local_time = ephem.localtime(date)

        # Time format on Windows modified by #
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
        moon_description = self.moon_class.phase_description(phase)

        print(f" Illumination: {phase_percent:.0f}%")
        print(f" {moon_description}")

        print()
        input(" Press any key to exit")


moon_phase = MoonPhase()
