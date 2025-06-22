import tkinter as tk
from datetime import datetime
import time


class DigitalClock:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Digital Clock")
        self.window.geometry("450x200")
        self.window.resizable(False, False)
        self.window.configure(bg='#1a1a1a')

        # Clock settings
        self.is_24_hour = True
        self.show_seconds = True

        # Colors
        self.bg_color = '#1a1a1a'
        self.time_color = '#00ff41'  # Matrix green
        self.date_color = '#ffffff'
        self.button_color = '#333333'

        self.setup_ui()
        self.update_clock()

    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.window, bg=self.bg_color)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Time display
        self.time_label = tk.Label(
            main_frame,
            font=('Digital-7', 48, 'bold'),  # Digital font style
            bg=self.bg_color,
            fg=self.time_color,
            text="00:00:00"
        )
        self.time_label.pack(pady=(20, 10))

        # Date display
        self.date_label = tk.Label(
            main_frame,
            font=('Arial', 14, 'normal'),
            bg=self.bg_color,
            fg=self.date_color,
            text="Monday, January 1, 2024"
        )
        self.date_label.pack(pady=(0, 20))

        # Control buttons frame
        button_frame = tk.Frame(main_frame, bg=self.bg_color)
        button_frame.pack(pady=(10, 0))

        # 12/24 hour toggle button
        self.format_button = tk.Button(
            button_frame,
            text="12H",
            font=('Arial', 10, 'bold'),
            bg=self.button_color,
            fg='white',
            activebackground='#555555',
            activeforeground='white',
            bd=0,
            padx=15,
            pady=5,
            command=self.toggle_format
        )
        self.format_button.pack(side='left', padx=(0, 10))

        # Seconds toggle button
        self.seconds_button = tk.Button(
            button_frame,
            text="Hide Sec",
            font=('Arial', 10, 'bold'),
            bg=self.button_color,
            fg='white',
            activebackground='#555555',
            activeforeground='white',
            bd=0,
            padx=15,
            pady=5,
            command=self.toggle_seconds
        )
        self.seconds_button.pack(side='left', padx=(0, 10))

        # Theme toggle button
        self.theme_button = tk.Button(
            button_frame,
            text="Theme",
            font=('Arial', 10, 'bold'),
            bg=self.button_color,
            fg='white',
            activebackground='#555555',
            activeforeground='white',
            bd=0,
            padx=15,
            pady=5,
            command=self.cycle_theme
        )
        self.theme_button.pack(side='left')

        # Bind keyboard shortcuts
        self.window.bind('<Key-f>', lambda e: self.toggle_format())
        self.window.bind('<Key-s>', lambda e: self.toggle_seconds())
        self.window.bind('<Key-t>', lambda e: self.cycle_theme())
        self.window.bind('<Escape>', lambda e: self.window.quit())

        # Make window focusable for keyboard events
        self.window.focus_set()

        # Center window on screen
        self.center_window()

    def center_window(self):
        """Center the window on the screen"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')

    def update_clock(self):
        """Update the clock display"""
        now = datetime.now()

        # Format time based on settings
        if self.is_24_hour:
            if self.show_seconds:
                time_format = "%H:%M:%S"
            else:
                time_format = "%H:%M"
        else:
            if self.show_seconds:
                time_format = "%I:%M:%S %p"
            else:
                time_format = "%I:%M %p"

        time_string = now.strftime(time_format)

        # Format date
        date_string = now.strftime("%A, %B %d, %Y")

        # Update labels
        self.time_label.config(text=time_string)
        self.date_label.config(text=date_string)

        # Schedule next update
        self.window.after(1000, self.update_clock)

    def toggle_format(self):
        """Toggle between 12-hour and 24-hour format"""
        self.is_24_hour = not self.is_24_hour
        button_text = "12H" if self.is_24_hour else "24H"
        self.format_button.config(text=button_text)

    def toggle_seconds(self):
        """Toggle seconds display"""
        self.show_seconds = not self.show_seconds
        button_text = "Hide Sec" if self.show_seconds else "Show Sec"
        self.seconds_button.config(text=button_text)

    def cycle_theme(self):
        """Cycle through different color themes"""
        themes = [
            # Matrix theme (default)
            {'bg': '#1a1a1a', 'time': '#00ff41', 'date': '#ffffff'},
            # Blue theme
            {'bg': '#0d1421', 'time': '#00bfff', 'date': '#87ceeb'},
            # Red theme
            {'bg': '#2d1b1b', 'time': '#ff4444', 'date': '#ffaaaa'},
            # Purple theme
            {'bg': '#2d1b2d', 'time': '#dd44dd', 'date': '#ddaadd'},
            # Orange theme
            {'bg': '#2d2d1b', 'time': '#ffaa00', 'date': '#ffddaa'}
        ]

        # Find current theme and switch to next
        current_bg = self.bg_color
        current_index = 0

        for i, theme in enumerate(themes):
            if theme['bg'] == current_bg:
                current_index = i
                break

        # Get next theme (cycle back to 0 if at end)
        next_index = (current_index + 1) % len(themes)
        new_theme = themes[next_index]

        # Apply new theme
        self.bg_color = new_theme['bg']
        self.time_color = new_theme['time']
        self.date_color = new_theme['date']

        # Update all components
        self.window.configure(bg=self.bg_color)
        self.time_label.configure(bg=self.bg_color, fg=self.time_color)
        self.date_label.configure(bg=self.bg_color, fg=self.date_color)

        # Update frames
        for widget in self.window.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.configure(bg=self.bg_color)
                for child in widget.winfo_children():
                    if isinstance(child, tk.Frame):
                        child.configure(bg=self.bg_color)

    def run(self):
        """Start the clock application"""
        try:
            self.window.mainloop()
        except KeyboardInterrupt:
            print("\nClock application stopped.")


# Create and run the digital clock
if __name__ == "__main__":
    clock = DigitalClock()
    clock.run()