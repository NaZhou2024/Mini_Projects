import tkinter as tk

class Countdown:
    def __init__(self, root, my_time, entry_field, status_label):
        """Initialize the countdown timer with the specified time."""
        self.seconds = int(my_time)
        self._isRunning = False
        self.root = root
        self.entry_field = entry_field  # Store reference to entry field
        self.status_label = status_label  # Store reference to status label

        # Create a fixed-width label to prevent shifting
        self.label = tk.Label(root, text="Time remaining: 00:00", font=("Helvetica", 24), width=20, anchor="center", pady=10)
        self.label.grid(column=0, row=2, columnspan=2, padx=10, pady=5, sticky="ew")

        # Create buttons with colors
        self.stop_button = tk.Button(root, text="Stop", fg="white", command=self.stopCountdown, padx=10, pady=5)
        self.stop_button.grid(column=0, row=3, padx=10, pady=5, sticky="ew")

        self.reset_button = tk.Button(root, text="Reset", command=self.resetCountdown, padx=10, pady=5)
        self.reset_button.grid(column=1, row=3, padx=10, pady=5, sticky="ew")

        self.apply_button_colors()  # Apply button colors
        self.update_label()
        
    def apply_button_colors(self):
        """Set button colors depending on OS (Fix for macOS)."""
        system = self.root.tk.call("tk", "windowingsystem")
        if system == "aqua":  # macOS
            self.stop_button.config(highlightbackground="red")
            self.reset_button.config(highlightbackground="yellow")
        else:  # Windows/Linux
            self.stop_button.config(bg="red")
            self.reset_button.config(bg="yellow")

    def update_label(self):
        """Update the label with the remaining time."""
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        self.label.config(text=f"Time remaining: {minutes:02}:{seconds:02}")

    def startCountdown(self):
        """Start the countdown timer."""
        if not self._isRunning:
            self._isRunning = True
            self.runCountdown()

    def runCountdown(self):
        """Run the countdown timer and update the label every second."""
        if self._isRunning and self.seconds > 0:
            self.seconds -= 1
            self.update_label()
            self.root.after(1000, self.runCountdown)
        elif self.seconds == 0:
            self.label.config(text="Timer Is UP!", bg="Orange")

    def stopCountdown(self):
        """Stop the countdown timer."""
        self._isRunning = False
        self.label.config(text="Countdown Stopped.")

    def resetCountdown(self):
        """Reset the countdown timer and clear the entry field."""
        self.stopCountdown()
        self.entry_field.delete(0, tk.END)  # Clear entry field
        self.label.config(text="Time remaining: 00:00")  # Reset label
        self.status_label.config(text="")  # Clear error messages

def main():
    # Create the main window
    window = tk.Tk()
    window.title("Countdown Timer")
    window.geometry("400x300")  # Fixed size
    window.resizable(False, False)  # Prevent resizing

    # Force equal column width for centering
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)

    timer = None  # To store the Countdown object

    def start_timer():
        """Start the countdown with the specified time."""
        nonlocal timer

        # Stop previous timer if running
        if timer:
            timer.stopCountdown()  
            timer.label.destroy()  # Remove previous label to prevent overlap

        my_time = entry_field.get().strip()

        # Handle invalid input
        if not my_time.isdigit():
            status_label.config(text="Invalid input! Enter a number.", fg="red")
            entry_field.delete(0, tk.END)  # Allow re-entry of correct input
            return

        status_label.config(text="")  # Clear error message
        timer = Countdown(window, my_time, entry_field, status_label)
        timer.startCountdown()

    # Instruction Label
    prompt = tk.Label(window, text="Enter your time in seconds:", font=("Helvetica", 14), pady=10)
    prompt.grid(column=0, row=0, columnspan=2, padx=10, sticky="ew")

    # Entry field
    entry_field = tk.Entry(window, font=("Helvetica", 14), justify="center")
    entry_field.grid(column=0, row=1, columnspan=2, padx=10, pady=5, sticky="ew")

    # Error status label (for invalid input messages)
    status_label = tk.Label(window, text="", fg="red", pady=5)
    status_label.grid(column=0, row=4, columnspan=2, sticky="ew")

    # Start button (Green)
    start_button = tk.Button(window, text="Start", fg="white", command=start_timer, padx=10, pady=5)
    start_button.grid(column=0, row=5, columnspan=2, pady=10, sticky="ew")

    # Apply button color fix for macOS
    system = window.tk.call("tk", "windowingsystem")
    if system == "aqua":  # macOS
        start_button.config(highlightbackground="green")
    else:  # Windows/Linux
        start_button.config(bg="green")

    window.mainloop()

if __name__ == "__main__":
    main()
