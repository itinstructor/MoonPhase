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
import moon_class


class MoonPhase:
    def __init__(self) -> None:
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Moon Phase")
        self.root.geometry("+100+100")
        self.root.iconbitmap("moon.ico")
        self.create_widgets()

        # Create moonclass object to access methods and properties
        # Default location is lat and lng of Scottsbluff, NE
        self.mc = moon_class.MoonClass()

        # Run the main loop
        self.root.mainloop()

# ----------------------- DISPLAY MOON PHASE ------------------------------#
    def display_moon_phase(self, *args):
        """
        Updates moon phase information displayed based on the selected date.

        Inputs:
        - self: The instance of the MoonPhase class.

        Flow:
        1. Get the selected date from the calendar widget
           and convert it to the format 'YYYY/MM/DD'.
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
        # Change date of observation based on selected date

        # Extract the selected date from the calendar and format as a string
        current_time = self.cal.selection_get().strftime('%Y/%m/%d')

        # Uncomment the line below for debugging purposes
        # print(current_time)

        # Set observer location and current time for moon phase calculation
        self.mc.get_observer(current_time)

        # Attempt to retrieve moon phase information
        try:
            # Retrieve moon phase description and percentage illumination
            phase_description = self.mc.phase_description
            moon_phase = self.mc.illumination

            # Update the GUI label with moon illumination percentage
            self.lbl_moon_description.config(
                text=f"Illumination: {moon_phase:.0f}%"
            )

            # Update the GUI label with the moon phase description
            self.lbl_moon_phase.config(
                text=f"{phase_description}"
            )

        # Handle exceptions and update label
        except Exception as e:
            self.lbl_moon_phase.config(text=f"Error: {e}")

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

        self.lbl_moon_description = ttk.Label(self._main_frame)
        self.lbl_moon_phase = ttk.Label(self._main_frame)
        # Fill the frame to the width of the window
        self._entry_frame.pack(fill=tk.X)
        self._main_frame.pack(fill=tk.X)
        # Keep the frame size regardless of the widget sizes
        self._entry_frame.pack_propagate(False)
        self._main_frame.pack_propagate(False)

        self.cal.grid(row=0, column=0)
        self.btn_calculate.grid(row=1, column=0, sticky=tk.W)
        self.lbl_moon_description.grid(row=2, column=0, sticky=tk.W)
        self.lbl_moon_phase.grid(row=3, column=0, sticky=tk.W)

        # Set padding between frame and window
        self._entry_frame.pack_configure(padx=10)
        self._main_frame.pack_configure(padx=10, pady=(10))
        for child in self._entry_frame.winfo_children():
            child.grid_configure(padx=5, pady=3, ipadx=1, ipady=1)
        for child in self._main_frame.winfo_children():
            child.grid_configure(padx=5, pady=3, ipadx=1, ipady=1)

        # Iterate over each row in the calendar widget
        for row in self.cal._calendar:
            # Iterate over each label in the current row
            for lbl in row:
                # Bind the double-click event to the display_moon_phase method
                lbl.bind("<Double-1>", self.display_moon_phase)

        # Either enter key will call the method
        self.root.bind("<Return>", self.display_moon_phase)
        self.root.bind("<KP_Enter>", self.display_moon_phase)
        self.root.bind("<Escape>", self.quit)

# ------------------------- QUIT PROGRAM ----------------------------------#
    def quit(self, *args):
        self.root.destroy()


# Create program object to start program
moon_phase = MoonPhase()
