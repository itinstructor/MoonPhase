"""
    Name: moon_class.py
    Author: William A Loring
    Created: 07-08-23
    Purpose: Python moon phase methods class
"""
# pip install epmem
import ephem
import os
from datetime import datetime


class MoonClass:

    def __init__(self, lat='41.862302', lng='-103.6627088') -> None:
        # Set latitude and longitude properties
        # Default argument lat lng: Scottsbluff, NE, US
        self._lat = lat
        self._lng = lng
        # self.formatted_time = None
        # current_time = now.strftime("%H:%M:%S")

        # Get the current local computer time
        self._current_time = datetime.now()
        # self._current_time = None

# ----------------------- MOON CLASS PROPERTIES ---------------------------#
    @property
    def phase_percent(self) -> float:
        return self._phase

    @property
    def phase_description(self) -> str:
        return self._phase_description

    @property
    def earth_to_moon(self: float):
        return self._earth_to_moon

    @property
    def miles_to_moon(self: float):
        """Convert from AU to Miles"""
        self._miles_to_moon = self._earth_to_moon * 92955807.273
        return self._miles_to_moon

    @property
    def km_to_moon(self: float):
        """Convert from AU to KM"""
        self._km_to_moon = 149597870.7 * self._earth_to_moon
        return self._km_to_moon

    @property
    def current_time(self):
        """Return current time"""
        return self._current_time

# -------------------- GET FORMATTED TIME ---------------------------------#
    @property
    def formatted_time(self):
        """
        Returns current time in a specific format
          based on the operating system.

        Returns:
            str: The formatted current time.

        Example Usage:
            moon = MoonClass()
            moon.get_current_time()
            print(moon.formatted_time())
        """
        if os.name == "nt":
            self._formatted_time = self._current_time.strftime(
                " %#I:%M %p %#m/%#d/%Y"
            )
        else:
            self._formatted_time = self._current_time.strftime(
                " %-I:%M %p %-m/%-d/%Y"
            )
        return self._formatted_time

# ----------------------- GET CURRENT TIME --------------------------------#
    def get_current_time(self):
        """
        Retrieves the current date and time, 
        converts it to the local time, 
        and stores it in the `_current_time` attribute.

        Example Usage:
        moon = MoonClass()
        moon.get_current_time()
        # Output: the current date in the format 'YYYY/MM/DD'
        print(moon.current_time)  

        Inputs: None

        Flow:
        1. Get current date and time using the `ephem.now()` function.
        2. Convert date and time to local time
          using `ephem.localtime()` function.
        3. Format local time as a string in the format 'YYYY/MM/DD' 
          using the `strftime()` method.
        4. Store formatted time in the `_current_time` attribute
          of the `MoonClass` instance.

        """
        # Get current date and time
        time = ephem.now()
        # Convert to local time
        time = ephem.localtime(time)
        # Format local time as string
        self._current_time = time.strftime('%Y/%m/%d')
        # print(self._current_time)

# ----------------------- GET EPHEM OBSERVER ------------------------------#
    def get_observer(self, time=None):
        """
        Calculate and retrieve information about the moon based
        on a given time and observer location.

        Args:
            time (str, optional): A string representing the date
            and time in the format 'YYYY/MM/DD'.
            If not provided, the current time is used.

        Example Usage:
            moon = MoonClass()
            moon.get_observer('2022/01/01')
            # Output: distance from earth to the moon
            print(moon.earth_to_moon)
            # Output: surface illumination of the moon in percent
            print(moon.phase_percent)
            # Output: description of the moon phase
            print(moon.phase_description)
        """
        if time is None:
            time = self._current_time
        # print(time)

        # Create observer object: the location and time we are observing from
        self.observer = ephem.Observer()
        self.observer.lat = self._lat
        self.observer.long = self._lng
        self.observer.date = time

        # Create moon object from time
        moon = ephem.Moon(time)

        # Calculate moon information based on observer information
        moon.compute(self.observer)

        # Distance from earth to the moon
        self._earth_to_moon = moon.earth_distance

        # Surface illumination of the moon in percent
        # self._phase_percent = moon.phase

        # Surface illumination of the moon from 0.0 to 1.0
        self._phase = moon.moon_phase
        # print(self._phase)
        # self.get_phase_description()

# ----------------------- MOON PHASE DESCRIPTION --------------------------#
    def get_phase_description(self):
        """ Convert moon phase to description
        from 0 (the new moon) to 0.5 (the full moon)
        and back to 1 (the next new moon)

        The phase of the moon is returned as a fraction,
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
        # Get the current date in UTC
        # target_date_utc = self.observer.date
        # Convert UTC date to local date
        # target_date_local = ephem.localtime(target_date_utc).date()

        target_date_utc = self.observer.date
        # Calculate dates for various moon phases
        # target_date_local = ephem.localtime(target_date_utc).date()
        target_date_local = target_date_utc

        # Calculate dates for various moon phases
        next_full = ephem.localtime(
            ephem.next_full_moon(target_date_utc)).date()
        next_new = ephem.localtime(ephem.next_new_moon(target_date_utc)).date()
        next_last_quarter = ephem.localtime(
            ephem.next_last_quarter_moon(target_date_utc)).date()
        next_first_quarter = ephem.localtime(
            ephem.next_first_quarter_moon(target_date_utc)).date()
        previous_full = ephem.localtime(
            ephem.previous_full_moon(target_date_utc)).date()
        previous_new = ephem.localtime(
            ephem.previous_new_moon(target_date_utc)).date()
        previous_last_quarter = ephem.localtime(
            ephem.previous_last_quarter_moon(target_date_utc)).date()
        previous_first_quarter = ephem.localtime(
            ephem.previous_first_quarter_moon(target_date_utc)).date()

        # Determine the moon phase based on dates
        if target_date_local in (
            next_full, previous_full
        ):
            self._phase_description = description[4]

        elif target_date_local in (
            next_new, previous_new
        ):
            self._phase_description = description[0]

        elif target_date_local in (
            next_first_quarter,
            previous_first_quarter
        ):
            self._phase_description = description[2]

        elif target_date_local in (next_last_quarter, previous_last_quarter):
            self._phase_description = description[6]
        elif previous_new < next_first_quarter < next_full < next_last_quarter < next_new:
            self._phase_description = description[1]
        elif previous_first_quarter < next_full < next_last_quarter < next_new < next_first_quarter:
            self._phase_description = description[3]
        elif previous_full < next_last_quarter < next_new < next_first_quarter < next_full:
            self._phase_description = description[5]
        elif previous_last_quarter < next_new < next_first_quarter < next_full < next_last_quarter:
            self._phase_description = description[7]
