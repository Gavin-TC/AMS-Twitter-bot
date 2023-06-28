import time
import os
import csvretriever
import data as dt
import datechecking
from globals import GLOBAL_TEST_BOOL
from sys import platform

allowed_to_track = True

time_to_sleep = 900  # seconds

working_directory = os.getcwd()
csv_directory = os.path.join(working_directory, "csvs")

def main():
    global allowed_to_track
    
    current_check = 1
    minutes = 0

    if len(os.listdir(csv_directory)) == 0:
        print("Adding a csv!")
        csvretriever.get_new_csv()

    date_checking_thread = threading.Thread(target=datechecking.make_checks())
    date_checking_thread.start()

    while allowed_to_track:
        if len(os.listdir(csv_directory)) != 2:
            dt.make_comparison(True, GLOBAL_TEST_BOOL)
        else:
            dt.make_comparison(False, GLOBAL_TEST_BOOL)
        
        print(f"This is check #{current_check}. It has been {minutes} minutes since first check.")
        
        time.sleep(time_to_sleep)
        
        current_check += 1
        minutes = 15 * current_check

if __name__ == '__main__':
    main()
