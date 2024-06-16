from PIL import Image, ImageTk


class MoonPhaseCalc:
    moon_phase_descriptions = [
        "New (totally dark)",
        "Waxing Crescent (increasing to full)",
        "First Quarter (increasing to full)",
        "Waxing Gibbous (increasing to full)",
        "Full (full light)",
        "Waning gibbous (decreasing from full)",
        "Last Quarter (decreasing from full)",
        "Waning Crescent (decreasing from full)"
    ]

    def __init__(self, moon_phase:float):
        """Takes moon_phase as a number, calculates description """
        self._moon_phase = moon_phase
        self._moon_description = ""
        self._img = None
        self.get_moon_phase()

    @property
    def moon_description(self):
        return self._moon_description

    @moon_description.setter
    def moon_description(self, moon_description):
        self._moon_description = moon_description

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, img):
        self._img = img

# --------------------------------- MOONPHASE -----------------------------#
    def get_moon_phase(self):
        """
        Retrieves the moon phase from the weather data and updates the 
        moon description and image accordingly.
        Calculates the moon phase in percent.
        """
        # moon_phase = self.weather_data.get("days")[0].get("moonphase")

        # Convert moon phase to description
        # from 0 (the new moon) to 0.5 (the full moon)
        # and back to 1 (the next new moon)
        # print(self.moon_phase)
        if (self._moon_phase <= 0.0339):
            self._moon_description = MoonPhaseCalc.moon_phase_descriptions[0]
            self._img = Image.open(r"./assets/new.png")

        elif (self._moon_phase <= 0.2161):
            self._moon_description = MoonPhaseCalc.moon_phase_descriptions[1]
            self._img = Image.open(r"./assets/waxing_crescent.png")

        elif (self._moon_phase <= 0.2839):
            self._moon_description = MoonPhaseCalc.moon_phase_descriptions[2]
            self._img = Image.open(r"./assets/first_quarter.png")

        elif (self._moon_phase <= 0.4661):
            self._moon_description = MoonPhaseCalc.moon_phase_descriptions[3]
            self._img = Image.open(r"./assets/waxing_gibbous.png")

        elif (self._moon_phase <= 0.5339):
            self._moon_description = MoonPhaseCalc.moon_phase_descriptions[4]
            self._img = Image.open(r"./assets/full.png")

        elif (self._moon_phase <= 0.7161):
            self._moon_description = MoonPhaseCalc.moon_phase_descriptions[5]
            self._img = Image.open(r"./assets/waning_gibbous.png")

        elif (self._moon_phase <= 0.7839):
            self._moon_description = MoonPhaseCalc.moon_phase_descriptions[6]
            self._img = Image.open(r"./assets/last_quarter.png")

        elif (self._moon_phase <= 1.0):
            self._moon_description = MoonPhaseCalc.moon_phase_descriptions[7]
            self._img = Image.open(r"./assets/waning_crescent.png")

        # Display moon image
        self._img = ImageTk.PhotoImage(self._img)

        # Calculate moon phase in percent
        # Check if the moon phase is in the first half of its cycle
        if self._moon_phase <= 0.5:
            # Scale the moon phase to a value between 0 and 100
            self._moon_phase = self._moon_phase * 200.0
        else:
            # Scale the moon phase to a value between 100 and 0
            self._moon_phase = (1.0 - self._moon_phase) * 200.0
