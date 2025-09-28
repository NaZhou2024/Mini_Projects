import time
import sys
import threading

class Countdown:
    def __init__(self, my_time):
        self.seconds = int(my_time)
        self._isRunning = True

    def startCountdown(self):
        """Start the countdown timer."""
        print(f"Countdown started for {self.seconds} seconds. Press 'x' to stop.")

        for x in range(self.seconds, 0, -1):
            if not self._isRunning:
                print("\nCountdown stopped early.")
                return

            minutes = x // 60
            seconds = x % 60
            print(f"\rTime remaining: {minutes:02}:{seconds:02}  ", end='', flush=True)
            time.sleep(1)

        print("\nCongratulations, you finished today's exercise!")

    def stopCountdown(self):
        """Stop the countdown timer."""
        self._isRunning = False
        print("\nCountdown timer has stopped.")

def check_for_stop(timer):
    """Check for 'x' key press without blocking."""
    try:
        import msvcrt  # Windows-only
        while timer._isRunning:
            if msvcrt.kbhit():  # Detects keypress
                key = msvcrt.getch().decode("utf-8").lower()
                if key == 'x':
                    timer.stopCountdown()
                    break
    except ImportError:
        import sys, select  # Unix-based system
        while timer._isRunning:
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                key = sys.stdin.read(1).strip().lower()
                if key == 'x':
                    timer.stopCountdown()
                    break

def main():
    my_time = input('Please enter time in seconds: ').strip()

    if not my_time.isdigit():
        print("Invalid input. Please enter a number.")
        return

    timer = Countdown(my_time)

    # Start the countdown in a separate thread
    countdown_thread = threading.Thread(target=timer.startCountdown)
    countdown_thread.start()

    # Listen for 'x' keypress in another thread
    stop_thread = threading.Thread(target=check_for_stop, args=(timer,))
    stop_thread.daemon = True  # Stops automatically when main program exits
    stop_thread.start()

    countdown_thread.join()  # Wait for countdown to finish

if __name__ == "__main__":
    main()
