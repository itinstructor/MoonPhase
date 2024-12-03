import ephem
from abc import ABC, abstractmethod
from typing import Dict, Any
from datetime import datetime


class MoonCalculator(ABC):
    """
    Abstract base class for moon phase and illumination calculations
    """

    def __init__(self, date: datetime = None):
        """
        Initialize the moon calculator

        Args:
            date (datetime, optional): Date for calculations. 
                Defaults to current date if not provided.
        """
        self.date = date or datetime.now()
        self.moon_details = self._calculate_moon_details()

# --------------------- CALCULATE MOON DETAILS --------------------------- #
    def _calculate_moon_details(self) -> Dict[str, Any]:
        """
        Calculate detailed moon information using PyEphem

        Returns:
            Dict containing comprehensive moon details
        """
        # Create an observer at a neutral location (Greenwich, UK)
        observer = ephem.Observer()
        observer.lon = '0'  # Longitude of Greenwich
        observer.lat = '0'  # Latitude of Greenwich
        observer.date = self.date  # Set the observation date

        # Create a Moon object for the specified date and observer
        moon = ephem.Moon(observer)

        # Calculate moon illumination
        phase_illumination = moon.moon_phase * 100

        # Find the date of the next new moon after the given date
        new_moon = ephem.next_new_moon(self.date)

        # Calculate moon age (days since last new moon)
        moon_age = ephem.Date(self.date) - ephem.Date(new_moon)

        # Calculate lunar cycle phase (0 to 1)
        lunar_cycle = moon_age / 29.53058885

        return {
            'phase_numeric': lunar_cycle,
            'phase_name': self._get_moon_state(lunar_cycle),
            'illumination_percent': phase_illumination,
            'illumination_description': self._get_illumination_description(phase_illumination),
            'moon_age_days': moon_age,
            'next_new_moon': new_moon
        }

# ---------------------- GET MOON STATE ---------------------------------- #
    def _get_moon_state(self, phase: float) -> str:
        """
        Determine the descriptive name of the moon phase

        Args:
            phase (float): Lunar cycle phase (0 to 1)

        Returns:
            str: Descriptive name of the moon phase
        """
        # List of tuples mapping phase thresholds to moon phase names
        states = [
            (0, "New Moon"),
            (0.125, "Waxing Crescent"),
            (0.25, "First Quarter"),
            (0.375, "Waxing Gibbous"),
            (0.5, "Full Moon"),
            (0.625, "Waning Gibbous"),
            (0.75, "Last Quarter"),
            (0.875, "Waning Crescent"),
            (1.0, "New Moon")
        ]

        """For each phase in the list, it checks if our phase number is
        very close to that list number (within 0.0625, or about one-sixteenth).

        For example, if the phase number is 0.51, that iSs very close to
        0.5 (which is "Full Moon").
        
        If it finds a phase in the list that is close enough, 
        it immediately stops and returns that phase's name.
        So in our example, it would return "Full Moon."""

        # Loop through each threshold and name in the states list
        for threshold, name in states:
            # Check if the phase is within a close range (±0.0625) of the threshold
            if abs(phase - threshold) < 0.0625:
                # Return the moon phase name if it matches the threshold range
                return name

        # If no close match is found, return "Unknown Phase"
        return "Unknown Phase"

# -------------------- GET ILLUMINATION DESCRIPTION ---------------------- #
    def _get_illumination_description(self, illumination: float) -> str:
        """
        Provide a human-readable description of moon illumination

        Args:
            illumination (float): Percentage of moon surface illuminated

        Returns:
            str: Descriptive interpretation of illumination
        """
        if illumination < 1:
            return "Virtually Dark"
        elif illumination < 10:
            return "Barely Visible"
        elif illumination < 25:
            return "Thin Crescent"
        elif illumination < 50:
            return "Half Illuminated"
        elif illumination < 75:
            return "More than Half Illuminated"
        elif illumination < 99:
            return "Almost Full"
        else:
            return "Fully Illuminated"

# ------------------------ DISPLAY --------------------------------------- #
    @abstractmethod
    def display(self):
        """
        Abstract method to display moon details
        Must be implemented by subclasses
        """
        pass
