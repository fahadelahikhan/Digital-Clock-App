import tkinter as tk
from datetime import datetime


class SimpleClock:
    def __init__(self):
        # Create main window
        self.root = tk.Tk()
        self.root.title("My Digital Clock")
        self.root.geometry("400x180")
        self.root.resizable(False, False)

        # Clock display settings
        self.show_24_hour = True
        self.display_seconds = True
        self.current_theme = 0

        # Initialize UI component attributes
        self.main_frame = None
        self.time_display = None
        self.date_display = None
        self.button_frame = None
        self.format_btn = None
        self.seconds_btn = None
        self.theme_btn = None

        # Define color themes
        self.themes = [
            {"name": "Dark Green", "bg": "#1e1e1e", "time": "#00ff00", "date": "#ffffff"},
            {"name": "Ocean Blue", "bg": "#001122", "time": "#00aaff", "date": "#88ccff"},
            {"name": "Sunset", "bg": "#2a1a0a", "time": "#ff6600", "date": "#ffaa66"},
            {"name": "Purple", "bg": "#1a0a2a", "time": "#cc66ff", "date": "#ddaaff"},
            {"name": "Classic", "bg": "#000000", "time": "#ffffff", "date": "#cccccc"}
        ]

        self.create_interface()
        self.apply_current_theme()
        self.center_window()
        self.start_clock()

    def create_interface(self):
        """Create all the UI elements"""
        # Main container
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=True, padx=15, pady=15)

        # Time display (large font)
        self.time_display = tk.Label(
            self.main_frame,
            font=('Courier', 36, 'bold'),
            text="00:00:00"
        )
        self.time_display.pack(pady=(10, 5))

        # Date display (smaller font)
        self.date_display = tk.Label(
            self.main_frame,
            font=('Arial', 12),
            text="Loading date..."
        )
        self.date_display.pack(pady=(0, 15))

        # Control buttons
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)

        # Time format button (12/24 hour)
        self.format_btn = tk.Button(
            self.button_frame,
            text="12H Format",
            font=('Arial', 9),
            width=10,
            command=self.switch_time_format
        )
        self.format_btn.pack(side='left', padx=5)

        # Seconds visibility button
        self.seconds_btn = tk.Button(
            self.button_frame,
            text="Hide Seconds",
            font=('Arial', 9),
            width=12,
            command=self.toggle_seconds
        )
        self.seconds_btn.pack(side='left', padx=5)

        # Theme change button
        self.theme_btn = tk.Button(
            self.button_frame,
            text="Change Theme",
            font=('Arial', 9),
            width=12,
            command=self.change_theme
        )
        self.theme_btn.pack(side='left', padx=5)

        # Add keyboard shortcuts
        self.root.bind('<Key-f>', lambda e: self.switch_time_format())
        self.root.bind('<Key-s>', lambda e: self.toggle_seconds())
        self.root.bind('<Key-t>', lambda e: self.change_theme())
        self.root.bind('<Escape>', lambda e: self.close_app())

        # Make window accept keyboard input
        self.root.focus_set()

    def center_window(self):
        """Position window in center of screen"""
        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

    def start_clock(self):
        """Begin the clock update cycle"""
        self.update_time_display()

    def update_time_display(self):
        """Update the time and date shown on screen"""
        current_time = datetime.now()

        # Create time string based on format preference
        if self.show_24_hour:
            if self.display_seconds:
                time_text = current_time.strftime("%H:%M:%S")
            else:
                time_text = current_time.strftime("%H:%M")
        else:
            if self.display_seconds:
                time_text = current_time.strftime("%I:%M:%S %p")
            else:
                time_text = current_time.strftime("%I:%M %p")

        # Create date string
        date_text = current_time.strftime("%A, %B %d, %Y")

        # Update display labels
        self.time_display.config(text=time_text)
        self.date_display.config(text=date_text)

        # Schedule next update in 1 second
        self.root.after(1000, self.update_time_display)

    def switch_time_format(self):
        """Switch between 12-hour and 24-hour time format"""
        self.show_24_hour = not self.show_24_hour

        # Update button text to show current mode
        if self.show_24_hour:
            self.format_btn.config(text="12H Format")
        else:
            self.format_btn.config(text="24H Format")

    def toggle_seconds(self):
        """Show or hide seconds in time display"""
        self.display_seconds = not self.display_seconds

        # Update button text
        if self.display_seconds:
            self.seconds_btn.config(text="Hide Seconds")
        else:
            self.seconds_btn.config(text="Show Seconds")

    def change_theme(self):
        """Cycle through available color themes"""
        self.current_theme = (self.current_theme + 1) % len(self.themes)
        self.apply_current_theme()

    def apply_current_theme(self):
        """Apply the selected color theme to all elements"""
        theme = self.themes[self.current_theme]

        # Apply colors to main elements
        self.root.configure(bg=theme["bg"])
        self.main_frame.configure(bg=theme["bg"])
        self.time_display.configure(bg=theme["bg"], fg=theme["time"])
        self.date_display.configure(bg=theme["bg"], fg=theme["date"])
        self.button_frame.configure(bg=theme["bg"])

        # Apply colors to buttons
        button_bg = "#444444" if theme["bg"] == "#000000" else "#333333"
        for button in [self.format_btn, self.seconds_btn, self.theme_btn]:
            button.configure(
                bg=button_bg,
                fg="white",
                activebackground="#555555",
                activeforeground="white"
            )

    def close_app(self):
        """Safely close the application"""
        self.root.quit()
        self.root.destroy()

    def run(self):
        """Start the clock application"""
        try:
            self.root.mainloop()
        except Exception as error:
            print(f"An error occurred: {error}")
        finally:
            print("Clock application closed.")


# Run the clock when script is executed directly
if __name__ == "__main__":
    my_clock = SimpleClock()
    my_clock.run()