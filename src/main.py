import time
import threading
import os

import csvretriever
import data as dt

allowed_to_track = True
tracking = True

time_to_sleep = 600  # seconds

working_directory = os.getcwd()
csv_directory = os.path.join(working_directory, "csvs")

def main():
    current_check = 1
    if len(os.listdir(csv_directory)) == 0:
        print("Adding a csv!")
        csvretriever.get_new_csv()

    while allowed_to_track:
        dt.compare_dates()
        print(f"This is check #{current_check}.")
        time.sleep(time_to_sleep)
        current_check += 1

if __name__ == '__main__':
    main()
