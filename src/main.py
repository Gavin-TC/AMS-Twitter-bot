import time
import threading
import os

import csvretriever
import data as dt

allowed_to_track = True
tracking = True

time_to_sleep = 600  # seconds

csv_directory = "src\\csvs"

def main():
    input_thread = threading.Thread(target=check_input)
    input_thread.start()

    if len(os.listdir(csv_directory)) == 0:
        print("Adding a csv!")
        csvretriever.get_new_csv()

    while allowed_to_track:
        if tracking:
            dt.compare_dates()
            time.sleep(time_to_sleep)
        else:
            pass

def check_input():
    global allowed_to_track, tracking
    time.sleep(1)
    while allowed_to_track:
        print()
        user_input = input("Enter 'p' to pause tracking: ")

        # Pause tracking.
        if user_input == "p":
            tracking = not tracking

if __name__ == '__main__':
    main()