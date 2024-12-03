"""
    Name: moon_phase_gui.py
    Author: William A Loring
    Created: 07-08-23
    Purpose: Python moon phase program using ephem library
"""

import tkinter as tk
from tkinter import ttk
# pip install tkcalendar
from tkcalendar import Calendar
from base64 import b64decode
# from PIL import Image, ImageTk
import moon_class
from moon_icon import moon_16
from moon_icon import moon_32


class MoonPhase:
    def __init__(self) -> None:
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Moon Phase")
        self.root.geometry("325x425+100+100")

        small_icon = tk.PhotoImage(data=b64decode(moon_16))
        large_icon = tk.PhotoImage(data=b64decode(moon_32))
        self.root.iconphoto(False, large_icon, small_icon)

        self.create_widgets()

        # Create moonclass object to access methods and properties
        # Default location is lat and lng of Scottsbluff, NE
        self.mc = moon_class.MoonClass()

        # Create observer
        self.mc.get_observer()

        # Display moon information based on current time when program starts
        self.display_moon_phase()

        # Run the main loop
        self.root.mainloop()

# -------------------------- GET TIME ------------------------------------ #
    def get_time(self, *args):
        # Change date of observation based on selected date
        # Get the Python date object from the from the calendar
        cal_time = self.cal.selection_get()
        # Uncomment the line below for debugging purposes
        # print(cal_time)

        # Set observer location and current time for moon phase calculation
        self.mc.get_observer(cal_time)
        self.display_moon_phase()

# ----------------------- DISPLAY MOON PHASE ----------------------------- #
    def display_moon_phase(self):
        """
        Updates moon phase information displayed based on the selected date.

        Inputs:
        - self: The instance of the MoonPhase class.

        Flow:
        1. Get the selected date from the calendar widget
        2. Try to retrieve the phase description and phase percentage 
           from the mc object (an instance of the MoonClass class).
        3. Update the text of the moon_description_label widget
           with the moon phase percentage.
        4. Update the text of the moon_phase_label widget with the
           moon phase description.
        5. If an exception occurs, update the text of the moon_phase_label
           widget with the error message.

        Outputs:
        - None. The method updates the text of the moon_description_label
          and moon_phase_label widgets in the GUI.
        """

        # Attempt to retrieve moon phase information
        try:
            # Retrieve moon phase description and percentage illumination
            phase_description = self.mc.phase_description
            moon_phase = self.mc.illumination
            km_to_moon = self.mc.km_to_moon
            miles_to_moon = self.mc.miles_to_moon
            moon_age = self.mc.moon_age

            # Update the GUI label with the moon phase description
            self.lbl_moon_phase.config(
                text=f"{phase_description}"
            )

            # Moon illumination percentage
            self.lbl_moon_illumination.config(
                text=f"    Illumination: {moon_phase:.2f}%"
            )

            # KM to Moon
            self.lbl_km_to_moon.config(
                text=f"   KM to Moon: {km_to_moon:,.0f}"
            )

            # Miles to Moon
            self.lbl_miles_to_moon.config(
                text=f"Miles to Moon: {miles_to_moon:,.0f}"
            )

            # Days since the last new moon
            self.lbl_moon_age.config(
                text=f"       Moon Age: {moon_age:.2f}"
            )

            # Update the GUI label with the moon phase image
            self.lbl_image.config(
                image=self.mc.phase_img
            )

        # Handle exceptions and update label
        except Exception as e:
            self.lbl_moon_phase.config(text=f"Error: {e}")

# ----------------------- CREATE WIDGETS --------------------------------- #
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
            command=self.get_time
        )

        # Fill the frame to the width of the window
        self._entry_frame.pack(fill=tk.X)
        self._main_frame.pack(fill=tk.X)

        # Keep the frame size regardless of the widget sizes
        self._entry_frame.pack_propagate(False)
        self._main_frame.pack_propagate(False)

        # Calendar configure column and row to expand
        self._entry_frame.columnconfigure(0, weight=1)
        self._entry_frame.rowconfigure(0, weight=1)
        # Grid calendar
        self.cal.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.lbl_moon_phase = ttk.Label(self._main_frame)
        self.lbl_moon_illumination = ttk.Label(self._main_frame, width=35)
        self.lbl_km_to_moon = ttk.Label(self._main_frame)
        self.lbl_miles_to_moon = ttk.Label(self._main_frame)
        self.lbl_moon_age = ttk.Label(self._main_frame)

        self.lbl_image = ttk.Label(self._main_frame)

        self.btn_calculate.grid(row=0, column=0, sticky=tk.W)
        self.lbl_moon_phase.grid(row=1, column=0, sticky=tk.W)
        self.lbl_moon_illumination.grid(row=2, column=0, sticky=tk.W)
        self.lbl_km_to_moon.grid(row=3, column=0, sticky=tk.W)
        self.lbl_miles_to_moon.grid(row=4, column=0, sticky=tk.W)
        self.lbl_moon_age.grid(row=5, column=0, sticky=tk.W)

        self.lbl_image.grid(row=1, column=1, rowspan=3, sticky=tk.W)

        # Set padding between frame and window
        self._entry_frame.pack_configure(padx=10)
        self._main_frame.pack_configure(padx=10, pady=10)
        for child in self._entry_frame.winfo_children():
            child.grid_configure(padx=5, pady=3, ipadx=1, ipady=1)
        for child in self._main_frame.winfo_children():
            child.grid_configure(padx=5, pady=3, ipadx=1, ipady=1)

        # Iterate over each row in the calendar widget
        for row in self.cal._calendar:
            # Iterate over each label in the current row
            for lbl in row:
                # Bind the double-click event to the get_time method
                lbl.bind("<Double-1>", self.get_time)

        # Either enter key will call the method
        self.root.bind("<Return>", self.get_time)
        self.root.bind("<KP_Enter>", self.get_time)
        self.root.bind("<Escape>", self.quit)

# ------------------------- QUIT PROGRAM --------------------------------- #
    def quit(self, *args):
        self.root.destroy()


# Create program object to start program
moon_phase = MoonPhase()
