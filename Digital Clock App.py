"""
Simple Digital Clock GUI Application
A beginner-friendly tkinter application that displays current time
"""

import tkinter as tk
from datetime import datetime
from functools import partial

class DigitalClock:
    def __init__(self):
        # Initialize the main window
        self.window = tk.Tk()
        self.window.title("My Digital Clock")
        self.window.geometry("400x150")
        self.window.configure(bg='black')

        # Make window non-resizable for better appearance
        self.window.resizable(False, False)

        # Initialize label attributes (fixes PyCharm warnings)
        self.time_label = None
        self.date_label = None

        # Center the window on screen
        self.center_window()

        # Create and configure the time display
        self.setup_display()

        # Start the clock
        self.update_clock()

    def center_window(self):
        """Center the window on the screen"""
        self.window.update_idletasks()
        width = 400  # Use fixed width instead of winfo_width()
        height = 150  # Use fixed height instead of winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')

    def setup_display(self):
        """Create and configure the time display label"""
        self.time_label = tk.Label(
            self.window,
            font=('Arial', 32, 'bold'),
            bg='black',
            fg='cyan',
            text="00:00:00"
        )
        self.time_label.pack(expand=True)

        # Add a date label for extra functionality
        self.date_label = tk.Label(
            self.window,
            font=('Arial', 12),
            bg='black',
            fg='lightgray',
            text=""
        )
        self.date_label.pack()

    @staticmethod
    def get_current_time():
        """Get formatted current time"""
        now = datetime.now()
        return now.strftime("%H:%M:%S")

    @staticmethod
    def get_current_date():
        """Get formatted current date"""
        now = datetime.now()
        return now.strftime("%A, %B %d, %Y")

    def update_clock(self):
        """Update the clock display every second"""
        # Update time
        current_time = self.get_current_time()
        self.time_label.config(text=current_time)

        # Update date
        current_date = self.get_current_date()
        self.date_label.config(text=current_date)

        # Schedule next update after 1000 ms (1 second)
        self.window.after(1000, partial(self.update_clock))

    def run(self):
        """Start the application"""
        self.window.mainloop()

# Create and run the digital clock
if __name__ == "__main__":
    clock = DigitalClock()
    clock.run()