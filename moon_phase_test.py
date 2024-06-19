import datetime
import ephem
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


def get_moon_info(date):
    """
    Returns a dictionary containing moon phase and illumination percentage.

    Args:
        date: A datetime.date object representing the date for which to calculate information.

    Returns:
        A dictionary with keys:
            - 'phase': A float between 0 (new moon) and 1 (next new moon) representing the moon phase.
            - 'illumination': A float between 0 and 100 representing the illuminated percentage of the moon.
    """
    # Convert date to ephem format
    ephem_date = ephem.Date(date)

    # Get moon object and compute
    moon = ephem.Moon()
    moon.compute(ephem_date)

    # Calculate lunation
    previous_new_moon = ephem.previous_new_moon(ephem_date)
    next_new_moon = ephem.next_new_moon(ephem_date)
    lunation = (ephem_date - previous_new_moon) / \
        (next_new_moon - previous_new_moon)
    lunation = lunation % 1

    return {
        'phase': lunation,
        'illumination': moon.phase  # Convert to percentage
    }


# Example usage
today = datetime.date.today()

moon_info = get_moon_info(today)
moon_phase = moon_info.get("phase")
print(f"Moon phase on {today}: {moon_info['phase']:.2f}")
print(f"Moon illumination on {today}: {moon_info['illumination']:.0f}%")


if (moon_phase <= 0.0339):
    moon_description = moon_phase_descriptions[0]
    # self._img = Image.open(r"./assets/new.png")

elif (moon_phase <= 0.2161):
    moon_description = moon_phase_descriptions[1]
    # self._img = Image.open(r"./assets/waxing_crescent.png")

elif (moon_phase <= 0.2839):
    moon_description = moon_phase_descriptions[2]
    # self._img = Image.open(r"./assets/first_quarter.png")

elif (moon_phase <= 0.4661):
    moon_description = moon_phase_descriptions[3]
    # self._img = Image.open(r"./assets/waxing_gibbous.png")

elif (moon_phase <= 0.5339):
    moon_description = moon_phase_descriptions[4]
    # self._img = Image.open(r"./assets/full.png")

elif (moon_phase <= 0.7161):
    moon_description = moon_phase_descriptions[5]
    # self._img = Image.open(r"./assets/waning_gibbous.png")

elif (moon_phase <= 0.7839):
    moon_description = moon_phase_descriptions[6]
    # self._img = Image.open(r"./assets/last_quarter.png")

elif (moon_phase <= 1.0):
    moon_description = moon_phase_descriptions[7]
    # self._img = Image.open(r"./assets/waning_crescent.png")
print(moon_description)
# Interpretation
# if phase < 0.5:
#   print("Waxing phase")
# elif phase > 0.5:
#   print("Waning phase")
# else:
#   print("Full moon")
