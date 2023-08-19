"""
    Name: moon_phase_gui_2.py
    Author: William A Loring
    Created: 07-08-23
    Purpose: Python moon phase program using ephem library
"""

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import moon_class


class MoonPhase:

    def __init__(self) -> None:
        # Create the main window
        root = tk.Tk()
        root.title("Moon Phase Calculator")
        root.geometry("250x400+100+100")
        root.iconbitmap("moon.ico")
        # Create widgets
        self.date_label = ttk.Label(root, text="Select Date:")
        self.date_label.pack()

        self.cal = Calendar(root, selectmode="day", date_pattern="yyyy/mm/dd")
        self.cal.pack(pady=10)

        self.btn_calculate = ttk.Button(
            root, text="Calculate Moon Phase", command=self.show_phase
        )
        self.btn_calculate.pack()

        self.moon_description_label = ttk.Label(root)
        self.moon_description_label.pack()
        self.moon_phase_label = ttk.Label(root)
        self.moon_phase_label.pack()
        self.canvas = tk.Canvas(root, width=94, height=94)
        self.canvas.pack()

        # Create moonclass object to access methods and properties
        self.mc = moon_class.MoonClass()

        # Run the main loop
        root.mainloop()

# ----------------------- SHOW MOON PHASE ---------------------------------#
    def show_phase(self):
        date = self.cal.selection_get().strftime('%Y/%m/%d')
        try:
            self.moon_description_label.config(
                text=f"Illumination: {(self.mc.phase_percent):.0f}%"
            )
            self.moon_phase_label.config(
                text=f"{self.mc.phase_description}")
        except Exception as e:
            self.moon_phase_label.config(text="Invalid Date")


moon_phase = MoonPhase()
