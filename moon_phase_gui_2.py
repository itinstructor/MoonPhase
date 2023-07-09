"""
    Name: moon_phase_gui_2.py
    Author: William A Loring
    Created: 07-08-23
    Purpose: Python moon phase program using ephem library
"""

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import ephem


def calculate_moon_phase(date):
    # Use the ephem library to calculate the moon phase for the given date
    moon = ephem.Moon(date)
    # 0-1.0 range of illumination
    moon_phase = moon.moon_phase
    return moon_phase


def get_moon_phase_description(phase):
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


def show_moon_phase():
    date = cal.selection_get().strftime('%Y/%m/%d')
    try:
        moon_phase = calculate_moon_phase(date)
        phase_description = get_moon_phase_description(moon_phase)
        moon_description_label.config(
            text=f"Illumination: {(moon_phase * 100):.0f}%")
        moon_phase_label.config(
            text=f"{phase_description}")
    except Exception as e:
        moon_phase_label.config(text="Invalid Date")


# Create the main window
root = tk.Tk()
root.title("Moon Phase Calculator")
root.geometry("250x300+100+100")
root.iconbitmap("moon.ico")
# Create widgets
date_label = ttk.Label(root, text="Select Date:")
date_label.pack()

cal = Calendar(root, selectmode="day", date_pattern="yyyy/mm/dd")
cal.pack(pady=10)

calculate_button = ttk.Button(
    root, text="Calculate Moon Phase", command=show_moon_phase
)
calculate_button.pack()

moon_description_label = ttk.Label(root)
moon_description_label.pack()
moon_phase_label = ttk.Label(root)
moon_phase_label.pack()


# Run the main loop
root.mainloop()
