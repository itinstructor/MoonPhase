import tkinter as tk
from tkcalendar import Calendar

# Create main window
root = tk.Tk()
root.title("Centered Calendar")

# Configure column and row to expand
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Add a Calendar widget and place it in the center
calendar = Calendar(root, selectmode="day", year=2023, month=10, day=26)
calendar.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Run the main loop
root.mainloop()
