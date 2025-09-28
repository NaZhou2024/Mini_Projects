import time
import keyboard

def countdown(seconds):
    """
    Countdown time function counts down the exercise time from a given number of seconds.
    Allows the user to interrupt the countdown by pressing 'x'
    """
    for i in range(seconds, 0, -1):
        if keyboard.is_pressed('x'): # press 'x' to exit the countdown
            print('Countdown interrupted!')
            return
        print(i)       # print out time value every second
        time.sleep(1)  # Wait for 1 second between prints

    print('Time is up!')

def main():
    seconds = int(input('Please Enter How Many Seconds You Want to Exercise?:'))
    countdown(seconds) # User enter the input
    print('Congratulations, you finish today\'s exercise!')
    
main()
