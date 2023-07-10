
class MoonClass:

    def __init__(self) -> None:
        """The phase of the moon is returned as a fraction,
        0.0 being a New Moon, 0.125 waxing crescent
        0.25 being a First Quarter, 0.325 waxing gibbous
        0.5 being a Full Moon, .625 waning gibbous
        0.75 being a Last Quarter, 0.825 waning cresent
        and 1.0 being a New Moon again.
        """
        self.description = [
            "New (totally dark)",
            "Waxing Crescent (increasing to full)",
            "First Quarter (increasing to full)",
            "Waxing Gibbous (increasing to full)",
            "Full Moon (full light)",
            "Waning Gibbous (decreasing from full)",
            "Last Quarter (decreasing from full)",
            "Waning Crescent (decreasing from full)"
        ]

# ----------------------- MOON PHASE DESCRIPTION --------------------------#
    def phase_description(self, phase):
        # Convert moon phase to description
        # from 0 (the new moon) to 0.5 (the full moon)
        # and back to 1 (the next new moon)
        if (phase <= 0.02):
            moon_description = self.description[0]
        elif (phase <= 0.23):
            moon_description = self.description[1]
        elif (phase <= 0.2839):
            moon_description = self.description[2]
        elif (phase <= .4661):
            moon_description = self.description[3]
        elif (phase <= 0.5339):
            moon_description = self.description[4]
        elif (phase <= 0.7161):
            moon_description = self.description[5]
        elif (phase <= 0.7839):
            moon_description = self.description[6]
        elif (phase <= 1.0):
            moon_description = self.description[7]
        return moon_description
