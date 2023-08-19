"""
    Name: moon_phase_gui_1.py
    Author: William A Loring
    Created: 07-08-23
    Purpose: Python moon phase program using ephem library
"""

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import ephem


class MoonPhase:
    def __init__(self) -> None:
        # Create the main window
        root = tk.Tk()
        root.title("Moon Phase Calculator")
        root.geometry("250x300+100+100")
        root.iconbitmap("moon.ico")

        self.cal = Calendar(
            root,
            selectmode="day",
            date_pattern="yyyy/mm/dd",
            firstweekday="sunday"
        )
        self.cal.pack(pady=10)

        self.calculate_button = ttk.Button(
            root, text="Calculate Moon Phase", command=self.show_moon_phase
        )
        self.calculate_button.pack()

        self.moon_description_label = ttk.Label(root)
        self.moon_description_label.pack()
        self.moon_phase_label = ttk.Label(root)
        self.moon_phase_label.pack()

        # Run the main loop
        root.mainloop()

# ----------------------- CALCULATE MOON PHASE ----------------------------#
    def calculate_moon_phase(self, date):
        # Use the ephem library to calculate the moon phase for the given date
        moon = ephem.Moon(date)
        # 0-1.0 range of illumination
        moon_phase = moon.moon_phase
        return moon_phase

# ----------------------- GET MOON PHASE DESCRIPTION ----------------------#
    def get_moon_phase_description(self, phase):
        # Determine the moon phase description based on the phase value
        phases = {
            (0, 0.02): "New Moon (totally dark)",
            (0.02, 0.23): "Waxing Crescent (increasing to full)",
            (0.23, 0.27): "First Quarter (increasing to full)",
            (0.27, 0.48): "Waxing Gibbous (increasing to full)",
            (0.48, 0.52): "Full Moon",
            (0.52, 0.73): "Waning Gibbous (decreasing from full)",
            (0.73, 0.77): "Last Quarter (decreasing from full)",
            (0.77, 0.98): "Waning Crescent (decreasing from full)",
            (0.98, 1.0): "New Moon (totally dark)",
        }
        for key, value in phases.items():
            if key[0] <= phase < key[1]:
                return value

# ----------------------- SHOE MOON PHASE ---------------------------------#
    def show_moon_phase(self):
        date = self.cal.selection_get().strftime('%Y/%m/%d')
        try:
            moon_phase = self.calculate_moon_phase(date)
            phase_description = self.get_moon_phase_description(moon_phase)
            self.moon_description_label.config(
                text=f"Illumination: {(moon_phase * 100):.0f}%")
            self.moon_phase_label.config(
                text=f"{phase_description}")
        except Exception as e:
            self.moon_phase_label.config(text=f"Invalid Date: {e}")


moon_phase = MoonPhase()
