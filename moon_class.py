"""
    Name: moon_class.py
    Author: William A Loring
    Created: 07-08-23
    Purpose: Python moon phase methods class
    06/21/24: Use new method of calculating moon phase
"""
# pip install epmem
import ephem
import os
import datetime
from base64 import b64decode
from tkinter import PhotoImage
import moon_icon
import moon_phases_ascii


class MoonClass:
    moon_phase_descriptions = [
        "New (totally dark)",
        "Waxing Crescent (increasing to full)",
        "First Quarter (increasing to full)",
        "Waxing Gibbous (increasing to full)",
        "Full Moon (full light)",
        "Waning Gibbous (decreasing from full)",
        "Last Quarter (decreasing from full)",
        "Waning Crescent (decreasing from full)"
    ]

    def __init__(self,  gui_mode=True, lat: str = '41.862302', lng: str = '-103.6627088') -> None:
        # Set latitude and longitude properties
        # Default argument lat lng: Scottsbluff, NE, US
        self._lat = lat
        self._lng = lng

        self._gui_mode = gui_mode

# ----------------------- MOON CLASS PROPERTIES ---------------------------#
    @property
    def moon_phase(self) -> float:
        # print(f"Moon Phase: {self._moon_phase}")
        return self._moon_phase

    @property
    def illumination(self) -> float:
        return self._illumination

    @property
    def phase_description(self) -> str:
        """Return phase description"""
        return self._phase_description

    @property
    def phase_img(self) -> PhotoImage:
        if self._gui_mode == True:
            """Return moon phase image"""
            return self._phase_img

    @property
    def phase_ascii(self) -> str:
        """Return moon phase image in ascii"""
        return self._phase_ascii
    
    @property
    def moon_age(self) -> float:
        return self._moon_age

    @property
    def earth_to_moon(self) -> float:
        """Distance in AU"""
        return self._earth_to_moon

    @property
    def miles_to_moon(self) -> float:
        """Convert from AU to Miles"""
        self._miles_to_moon = self._earth_to_moon * 92955807.273
        return self._miles_to_moon

    @property
    def km_to_moon(self) -> float:
        """Convert from AU to KM"""
        self._km_to_moon = 149597870.7 * self._earth_to_moon
        return self._km_to_moon

    @property
    def current_time(self):
        """Return current Python time object"""
        return self._current_time

    @property
    def formatted_time(self) -> str:
        """Return formatted time"""
        return self._formatted_time

# ----------------------- GET EPHEM OBSERVER ----------------------------- #
    def get_observer(self, dte=None):
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
        # If date is not passed as a argument, replace with current time
        if dte is None:
            # Get the current local computer date
            # self._current_time = datetime.date.today()
            self._current_time = datetime.datetime.now()
            dte = self._current_time
            self.get_formatted_time(dte)
            # Convert dte (date) to ephem format
            dte = ephem.Date(dte)

        # If a date is passed as an argument
        else:
            # Set formatted time to date passed in
            self.get_formatted_time(dte)
            # Convert dte (date) to ephem format
            dte = ephem.Date(dte)
            # TKCalendar date comes in at 12 am
            # Set time to 12 noon
            dte = ephem.Date(dte + 12 * ephem.hour)

        # Create observer object with the time of observation
        observer = ephem.Observer()
        observer.date = dte

        # self.observer.lat = self._lat
        # self.observer.long = self._lng

        # Create moon object from time parameter
        moon = ephem.Moon(dte)

        # Calculate moon information based on observer information
        moon.compute(observer)

    # --------------------- CALCULATE LUNATION --------------------------- #
        # Find the date of the previous new moon relative to the input date
        previous_new_moon = ephem.previous_new_moon(dte)

        # Tind the date of the next new moon relative to the input date (dte)
        next_new_moon = ephem.next_new_moon(dte)

        # Calculate moon age (days since last new moon)
        self._moon_age = ephem.Date(dte) - ephem.Date(previous_new_moon)

        # Calculate the lunation which is the fractional position of the
        # moon in its cycle. It does this by subtracting the date of the
        # previous new moon from the input date (dte) and then dividing
        # by the difference between the date of the next new moon and
        # the previous new moon.
        lunation = (dte - previous_new_moon) / \
            (next_new_moon - previous_new_moon)

        # This line calculates the moon phase by taking the remainder of
        # lunation divided by 1. The remainder will be a value between
        # 0 and 1, which represents the fractional part of the lunation
        # cycle that has passed. 0 represents a new moon, 0.5 represents
        # a full moon, and values in between represent waxing or
        # waning crescent, gibbous, or quarter moons.
        self._moon_phase = lunation % 1

        # Distance from earth to the moon
        self._earth_to_moon = moon.earth_distance

        # Surface illumination of the moon in decimal
        self._illumination = moon.phase
        # print(self._illumination)
        if self._gui_mode == True:
            self.get_phase_description_gui()
        else:
            self.get_phase_description_cli()

# --------------- MOON PHASE GUI DESCRIPTION AND IMAGE ------------------- #
    def get_phase_description_gui(self):
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
        # print(self._moon_phase)

        if (abs(self._moon_phase - 0) < 0.0625):
            # Moon phase description
            self._phase_description = MoonClass.moon_phase_descriptions[0]
            # photo = Image.open(r"./assets/new.png")
            self._phase_img = PhotoImage(data=b64decode(moon_icon.new))

        elif (abs(self._moon_phase - 0.125) < 0.0625):
            self._phase_description = MoonClass.moon_phase_descriptions[1]
            # photo = Image.open(r"./assets/waxing_crescent.png")
            self._phase_img = PhotoImage(
                data=b64decode(moon_icon.waxing_crescent))

        elif (abs(self._moon_phase - 0.25) < 0.0625):
            self._phase_description = MoonClass.moon_phase_descriptions[2]
            # photo = Image.open(r"./assets/first_quarter.png")
            self._phase_img = PhotoImage(
                data=b64decode(moon_icon.first_quarter))

        elif (abs(self._moon_phase - 0.375) < 0.0625):
            self._phase_description = MoonClass.moon_phase_descriptions[3]
            # photo = Image.open(r"./assets/waxing_gibbous.png")
            self._phase_img = PhotoImage(
                data=b64decode(moon_icon.waxing_gibbous))

        elif (abs(self._moon_phase - 0.5) < 0.0625):
            self._phase_description = MoonClass.moon_phase_descriptions[4]
            self._phase_img = PhotoImage(data=b64decode(moon_icon.full))

        elif (abs(self._moon_phase - 0.625) < 0.0625):
            self._phase_description = MoonClass.moon_phase_descriptions[5]
            self._phase_img = PhotoImage(
                data=b64decode(moon_icon.waning_gibbous))

        elif (abs(self._moon_phase - 0.75) < 0.0625):
            self._phase_description = MoonClass.moon_phase_descriptions[6]
            self._phase_img = PhotoImage(
                data=b64decode(moon_icon.last_quarter))

        elif (abs(self._moon_phase - 0.875) < 0.0625):
            self._phase_description = MoonClass.moon_phase_descriptions[7]
            self._phase_img = PhotoImage(
                data=b64decode(moon_icon.waning_crescent))

        elif (abs(self._moon_phase - 1.0) < 0.0625):
            self._phase_description = MoonClass.moon_phase_descriptions[0]
            self._phase_img = PhotoImage(data=b64decode(moon_icon.new))

# -------------- MOON PHASE CLI DESCRIPTION AND ASCII IMAGE -------------- #
    def get_phase_description_cli(self):
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

        if (abs(self._moon_phase - 0) < 0.0625):
            self._phase_description = MoonClass.moon_phase_descriptions[0]
            # New moon
            self._phase_ascii = moon_phases_ascii.moon_phases[0]

        elif (abs(self._moon_phase - 0.125) < 0.0625):
            self._phase_description = MoonClass.moon_phase_descriptions[1]
            # Waxing crescent
            self._phase_ascii = moon_phases_ascii.moon_phases[1]

        elif (abs(self._moon_phase - 0.25) < 0.0625):
            self._phase_description = MoonClass.moon_phase_descriptions[2]
            # First quarter
            self._phase_ascii = moon_phases_ascii.moon_phases[2]

        elif (abs(self._moon_phase - 0.375) < 0.0625):
            self._phase_description = MoonClass.moon_phase_descriptions[3]
            # Waxing gibbous
            self._phase_ascii = moon_phases_ascii.moon_phases[3]

        elif (abs(self._moon_phase - 0.5) < 0.0625):
            self._phase_description = MoonClass.moon_phase_descriptions[4]
            # Full moon
            self._phase_ascii = moon_phases_ascii.moon_phases[4]

        elif (abs(self._moon_phase - 0.625) < 0.0625):
            self._phase_description = MoonClass.moon_phase_descriptions[5]
            # Waning gibbous
            self._phase_ascii = moon_phases_ascii.moon_phases[5]

        elif (abs(self._moon_phase - 0.75) < 0.0625):
            # Last Quarter
            self._phase_description = MoonClass.moon_phase_descriptions[6]
            self._phase_ascii = moon_phases_ascii.moon_phases[6]

        elif (abs(self._moon_phase - 0.875) < 0.0625):
            # Waning crescent
            self._phase_description = MoonClass.moon_phase_descriptions[7]
            self._phase_ascii = moon_phases_ascii.moon_phases[7]

        elif (abs(self._moon_phase - 1.0) < 0.0625):
            # New moon
            self._phase_description = MoonClass.moon_phase_descriptions[0]
            self._phase_ascii = moon_phases_ascii.moon_phases[0]

# -------------------- GET FORMATTED TIME -------------------------------- #
    def get_formatted_time(self, dte):
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
            self._formatted_time = dte.strftime(
                " %A %B %#d, %Y"
            )
        else:
            self._formatted_time = dte.strftime(
                " %-m/%-d/%Y"
            )
