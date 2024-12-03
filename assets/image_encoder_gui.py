# Import required libraries
import tkinter as tk                  # Main GUI library
from tkinter import filedialog        # For opening file dialog
from tkinter import messagebox        # For showing error messages
from base64 import b64encode          # For encoding files to base64
# pip install pyperclip
import pyperclip                      # For copying to clipboard


class ImageEncoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Base64 Encoder")
        self.root.geometry("400x250")
        self.create_widgets()

# ----------------------- CREATE WIDGETS --------------------------------- #
    def create_widgets(self):
        # Create and configure main frame
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(expand=True, fill='both')

        # Create widgets
        self.label = tk.Label(
            self.main_frame,
            text="Select an image file to convert to base64",
            wraplength=350
        )
        self.label.pack(pady=(0, 20))

        self.select_button = tk.Button(
            self.main_frame,
            text="Select Image File",
            command=self.select_file,
            width=20
        )
        self.select_button.pack(pady=10)

        self.filename_label = tk.Label(
            self.main_frame,
            text="No file selected",
            wraplength=350
        )
        self.filename_label.pack(pady=10)

        self.status_label = tk.Label(
            self.main_frame,
            text="",
            wraplength=350
        )
        self.status_label.pack(pady=10)

# ------------------------- SELECT FILE ---------------------------------- #
    def select_file(self):
        """
        Opens a file dialog for selecting an image file.
        Called when the select button is clicked.
        """
        # Define the file types that can be selected
        filetypes = (
            # Common image formats
            ('Image files', '*.png *.jpg *.jpeg *.gif *.bmp'),
            # Option to show all files
            ('All files', '*.*')
        )

        # Open the file dialog and get selected filename
        filename = filedialog.askopenfilename(
            title='Select an image file',
            filetypes=filetypes
        )

        # If a file was selected (user didn't cancel)
        if filename:
            # Update the label to show selected filename
            self.filename_label.config(text=filename)
            # Process the selected file
            self.encode_file(filename)

# ------------------------ ENCODE FILE ----------------------------------- #
    def encode_file(self, filename):
        """
        Reads the selected file and converts it to base64.

        Args:
            filename (str): Path to the selected file
        """
        try:
            # Open the file in binary mode
            with open(filename, "rb") as f:
                # Read file content and convert to base64
                encoded = b64encode(f.read()).decode("ascii")
                # Copy the encoded string to clipboard
                pyperclip.copy(encoded)
                # Update status label to show success
                self.status_label.config(
                    text="Base64 encoded content copied to clipboard!",
                    fg="green"          # Set text color to green for success
                )
        except Exception as e:
            # If any error occurs during the process
            # Show error message in a popup
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            # Update status label to show error
            self.status_label.config(
                text="Error occurred while processing the file.",
                fg="red"               # Set text color to red for error
            )


def main():
    # Create the main window
    root = tk.Tk()
    # Create an instance of our application
    app = ImageEncoderApp(root)
    # Start the application's main loop
    root.mainloop()


if __name__ == "__main__":
    main()
