"""
    Name: moon_phase_cli_2.py
    Author: William A Loring
    Created: 07-08-23
    Purpose: Python moon phase program using ephem library
"""


import geocode_geopy
import moon_class


class MoonPhase:
    def __init__(self) -> None:
        print(" +------------------------------------------+")
        print(" |              Moon Phase App              |")
        print(" +------------------------------------------+")

        # Get location input from user
        city = input(" Enter city: ")
        state = input(" Enter state: ")
        country = input(" Enter country: ")

        # Get location lat, lng, and address from geopy
        self.lat, self.lng, self.address = geocode_geopy.geocode(
            city, state, country)

        # Create moonclass object to access methods and properties
        self.mc = moon_class.MoonClass(self.lat, self.lng)

        print(f" {self.address}")

        print(f"{self.mc.formatted_time}")
        print(f"    AU: {self.mc.earth_to_moon}")
        print(f"    KM: {self.mc.km_to_moon:,.0f}")
        print(f" Miles: {self.mc.miles_to_moon:,.0f}")

        print(f" Illumination: {self.mc.phase_percent:.0f}%")
        print(f" {self.mc.phase_description}")

        print()
        input(" Enter to exit")


moon_phase = MoonPhase()
