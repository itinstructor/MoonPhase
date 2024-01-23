"""
    Name: moon_phase_cli_2.py
    Author: William A Loring
    Created: 07-08-23
    Purpose: Python moon phase program using ephem library
    Display moon information at the current time and location
"""


import geocode_geopy as gp
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
        self.lat, self.lng, self.address = gp.geocode(
            city,
            state,
            country
        )

        # Create moonclass object to access methods and properties
        self.mc = moon_class.MoonClass(
            self.lat,
            self.lng
        )
        
        # Set observer location
        self.mc.get_observer()

        # Display moon information
        print(" --------------------------------------------------------------")
        print(f" {self.address}")
        print(f"{self.mc.formatted_time}")
        print(f" Distance from Earth to Moon")
        print(f"    AU: {self.mc.earth_to_moon}")
        print(f"    KM: {self.mc.km_to_moon:,.0f}")
        print(f" Miles: {self.mc.miles_to_moon:,.0f}")

        print(f" Illumination: {self.mc.phase_percent:.1f}%")
        print(f" {self.mc.phase_description}")

        print()
        input(" Enter to exit")


moon_phase = MoonPhase()
