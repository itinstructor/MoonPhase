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
        self.root = tk.Tk()
        self.root.title("Moon Phase Calculator")
        self.root.geometry("+100+100")
        self.root.iconbitmap("moon.ico")
        self.create_widgets()
        # Run the main loop
        self.root.mainloop()

# ----------------------- CALCULATE MOON PHASE ----------------------------#
    def calculate_moon_phase(self, date):
        # Use ephem library to calculate moon phase for the given date
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

# ----------------------- DISPLAY MOON PHASE ------------------------------#
    def display_moon_phase(self):
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

# ----------------------- CREATE WIDGETS ----------------------------------#
    def create_widgets(self):
        """Create frames"""
        self._entry_frame = tk.LabelFrame(
            self.root,
            text="Choose Date",
            relief=tk.GROOVE)
        self._main_frame = tk.LabelFrame(
            self.root,
            text="Calculate Moon Phase",
            relief=tk.GROOVE)

        self.cal = Calendar(
            self._entry_frame,
            selectmode="day",
            date_pattern="yyyy/mm/dd",
            firstweekday="sunday"
        )
        self.btn_calculate = ttk.Button(
            self._main_frame, text="Calculate Moon Phase",
            command=self.display_moon_phase
        )
        self.moon_description_label = ttk.Label(self._main_frame)
        self.moon_phase_label = ttk.Label(self._main_frame)
        # Fill the frame to the width of the window
        self._entry_frame.pack(fill=tk.X)
        self._main_frame.pack(fill=tk.X)
        # Keep the frame size regardless of the widget sizes
        self._entry_frame.pack_propagate(False)
        self._main_frame.pack_propagate(False)

        self.cal.grid(row=0, column=0)
        self.btn_calculate.grid(row=1, column=0, sticky=tk.W)
        self.moon_description_label.grid(row=2, column=0, sticky=tk.W)
        self.moon_phase_label.grid(row=3, column=0, sticky=tk.W)

        # Set padding between frame and window
        self._entry_frame.pack_configure(padx=10)
        self._main_frame.pack_configure(padx=10, pady=(10))
        for child in self._entry_frame.winfo_children():
            child.grid_configure(padx=5, pady=3, ipadx=1, ipady=1)
        for child in self._main_frame.winfo_children():
            child.grid_configure(padx=5, pady=3, ipadx=1, ipady=1)


# Create program object to start program
moon_phase = MoonPhase()
