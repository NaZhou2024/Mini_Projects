import tkinter as tk
from tkinter import messagebox
import os, datetime, platform, time, math

# –––––––––––––––––––––––––––––––– Sound setup –––––––––––––––––––––––––––––––––––
import platform, subprocess
os_name = platform.system()
if os_name == 'Windows':
    import winsound
    def play_sound():
        # Windows simple beep
        winsound.Beep(1000, 500)
elif os_name == 'Darwin':
    def play_sound():
        # macOS system beep via AppleScript
        subprocess.call(['osascript', '-e', 'beep'])
else:
    def play_sound():
        # fallback: terminal bell
        print('', end='', flush=True)
# –––––––––––––––––––––––––––––– Analog clock face –––––––––––––––––––––––––––––––
class AnalogClock(tk.Canvas):
    def __init__(self, master=None, size=300, **kwargs):
        super().__init__(master, width=size, height=size, bg="white", **kwargs)
        self.size = size
        self.center = size//2
        self.radius = self.center*0.9

        # countdown values
        self.initial = 0
        self.remaining = 0
        self._draw_face()
        self.hands = {
            'hour': self.create_line(0,0,0,0, width=6, fill='black'),
            'minute': self.create_line(0,0,0,0, width=4, fill='blue'),
            'second': self.create_line(0,0,0,0, width=2, fill='red'),
        }
        self._update()

    def _draw_face(self):
        # initial static clock face
        self.create_oval(
            self.center - self.radius, self.center - self.radius,
            self.center + self.radius, self.center + self.radius,
            width=4
        )
        for h in range(12):
            ang = math.radians(h * 30)
            x1 = self.center + (self.radius - 10) * math.sin(ang)
            y1 = self.center - (self.radius - 10) * math.cos(ang)
            x2 = self.center + self.radius * math.sin(ang)
            y2 = self.center - self.radius * math.cos(ang)
            self.create_line(x1, y1, x2, y2, width=3)

    def _update(self):
        # elapsed = initial - remaining
        elapsed = max(self.initial - self.remaining, 0)
        secs = elapsed % 60
        mins = (elapsed // 60) % 60 + secs / 60.0
        hrs  = (elapsed // 3600) % 12 + mins / 60.0
        angles = {
            'second': math.radians(secs * 6),
            'minute': math.radians(mins * 6),
            'hour':   math.radians(hrs * 30),
        }
        lengths = {
            'second': self.radius * 0.9,
            'minute': self.radius * 0.75,
            'hour':   self.radius * 0.5,
        }
        for hand, line_id in self.hands.items():
            ang = angles[hand]
            ln = lengths[hand]
            x = self.center + ln * math.sin(ang)
            y = self.center - ln * math.cos(ang)
            self.coords(line_id, self.center, self.center, x, y)
        self.after(1000, self._update)

    def set(self, initial, remaining):
        self.initial = initial
        self.remaining = remaining

    def reset(self):
        self.set(0, 0)
    
# –––––––––––––––––––––––––––––––– Countdown timer ––––––––––––––––––––––––––––––––
class Countdown:
    def __init__(self, root, clock, my_time, entry_field, status_label):
        """Initialize the countdown timer with the specified time."""
        self.initial = int(my_time)
        self._isRunning = False
        self.root = root
        self.clock = clock
        self.after_id = None
        self._start_time = None # Add start time for monotonic timing (every second)
        self.seconds = self.initial
        self.entry_field = entry_field  # Store reference to entry field
        self.status_label = status_label  # Store reference to status label
        self.log_file = "log.txt" # log file name

        # Create a fixed-width label to prevent shifting
        self.label = tk.Label(root, text="Time remaining: 00:00", font=("Helvetica", 24), width=20, anchor="center", pady=10)
        self.label.grid(column=1, row=4, columnspan=2, padx=10, pady=5, sticky="ew")

        # Create buttons with colors
        self.stop_button = tk.Button(root, text="Stop", fg="white", command=self.stopCountdown, padx=10, pady=5)
        self.stop_button.grid(column=0, row=6, padx=10, pady=5, sticky="ew")

        self.reset_button = tk.Button(root, text="Reset", command=self.resetCountdown, padx=10, pady=5)
        self.reset_button.grid(column=3, row=6, padx=10, pady=5, sticky="ew")

        self.apply_button_colors()  # Apply button colors
        self.update_label()
        self.log_action(f"Timer initialized with {self.initial} seconds")

    def initialize_log(self):
        """Initialize the log file."""
        try:
            if not os.path.exists(self.log_file):
                with open(self.log_file, "w") as log:
                    log.write("Log File Initialized\n")
            self.log_action("Program started.")
        except Exception as e:
            self.show_error_dialog(f"Error initializing log file: {str(e)}")

    def log_action(self, action):
        """Write action to log file."""
        try:
            with open(self.log_file, "a") as log:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log.write(f"{timestamp} - {action}\n")
        except Exception as e:
            self.show_error_dialog(f"Error writing to log file: {str(e)}")

    def show_error_dialog(self, message):
        """Show error dialog to the user."""
        messagebox.showerror("Error", message)
        
        
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
        self.initial = self.seconds
        self.update_label()
        self.clock.set(self.initial, self.seconds)
        # schedule first tick after 1 second
        self.after_id = self.root.after(1000, self._tick)

    def _tick(self):
        if not self._isRunning:
            return
        if self.seconds > 0:
            self.seconds -= 1
            if self.seconds <= 10:
                self.label.config(fg="red")
            self.update_label()
            self.clock.set(self.initial, self.seconds)
            # schedule next tick
            self.after_id = self.root.after(1000, self._tick)
        elif self.seconds == 0:
            self.update_label()
            self.label.config(text="Timer Is UP!", bg="Orange")
            play_sound()
            self.log_action("Timer finished")
            self._isRunning = False

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
        
# –––––––––––––––––––––––––––––– Main application ––––––––––––––––––––––––––––––––        
def quitProgram(root, log_file="log.txt"):
    """Verify if the user wants to quit and close the program."""
    answer = messagebox.askyesno("Quit", "Are you sure you want to quit?")
    if answer:
        try:
            with open(log_file, "a") as log:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log.write(f"{timestamp} - Program exited by user.\n")
        except Exception as e:
            messagebox.showerror("Error", f"Error writing to log file: {str(e)}")
        root.destroy()

def main():
    # Create the main window
    window = tk.Tk()
    window.title("Countdown Timer")
    window.geometry("500x650")  # Fixed size
    window.resizable(False, False)  # Prevent resizing
    for col in range(3): window.columnconfigure(col, weight=1)

    clock = AnalogClock(window, size=300)
    clock.grid(row=0, column=1, columnspan=2, pady=10)

    # Force equal column width for centering
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)

    timer = None  # To store the Countdown object
    log_file = "log.txt"  # Log file name

    def start_timer():
        """Start the countdown with the specified time."""
        nonlocal timer

        # Stop previous timer if running
        if timer:
            timer.stopCountdown()

        my_time = entry_field.get().strip()

        # Handle invalid input
        if not my_time.isdigit():
            status_label.config(text="Invalid input! Enter a number.", fg="red")
            entry_field.delete(0, tk.END)  # Allow re-entry of correct input
            return

        status_label.config(text="")  # Clear error message
        timer = Countdown(window, clock, my_time, entry_field, status_label)
        timer.startCountdown()

    # Instruction Label
    prompt = tk.Label(window, text="Enter your time in seconds:", font=("Helvetica", 14), pady=10)
    prompt.grid(column=1, row=1, columnspan=2, padx=10, sticky="ew")

    # Entry field
    entry_field = tk.Entry(window, font=("Helvetica", 14), justify="center")
    entry_field.grid(column=1, row=2, columnspan=2, padx=10, pady=5, sticky="ew")

    # Error status label (for invalid input messages)
    status_label = tk.Label(window, text="", fg="red", pady=5)
    status_label.grid(column=1, row=5, columnspan=2, sticky="ew")

    # Start button (Green)
    start_button = tk.Button(window, text="Start", fg="white", command=start_timer, padx=10, pady=5)
    start_button.grid(column=1, row=6, columnspan=2, pady=10, sticky="ew")

    # Apply button color fix for macOS
    system = window.tk.call("tk", "windowingsystem")
    if system == "aqua":  # macOS
        start_button.config(highlightbackground="green")
    else:  # Windows/Linux
        start_button.config(bg="green")
        
    # Quit button
    quit_button = tk.Button(window, text="Quit", fg="white", command=lambda: quitProgram(window, log_file), padx=10, pady=5, bg="red")
    quit_button.grid(column=1, row=8, columnspan=2, pady=10, sticky="ew")

    window.mainloop()

if __name__ == "__main__":
    main()
