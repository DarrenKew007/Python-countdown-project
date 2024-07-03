import time

def countdown_timer(seconds):
    for t in range(seconds, 0, -1):
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
    
    print("It's Showtime!")

# Get user input for the countdown time
user_input = input("Please enter the time to countdown in seconds: ")

try:
    countdown_time = int(user_input)
    countdown_timer(countdown_time)
except ValueError:
    print("Invalid input. Please enter a valid integer for the countdown time.")
