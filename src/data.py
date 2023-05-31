import tweeter
import csv
import os
import pandas as pd
import time
from datetime import datetime
from collections import deque

import csvretriever as ret

client = tweeter.client()
csv_location = "https://www.gunviolencearchive.org/query/0484b316-f676-44bc-97ed-ecefeabae077/export-csv"

# TODO: make a tweet at the end of the day summarizing the events.
# TODO: basically, just tweet the # of injured/killed, # of incidents, maybe more?

def make_comparison():
    ret.get_new_csv()
    directory = ret.working_directory
    
    # put the csvs into variables
    oldest_csv = os.path.join(directory, ret.return_oldest_csv())
    newest_csv = os.path.join(directory, ret.return_newest_csv())
    
    # initialize shootings variables
    old_shootings = 0
    new_shootings = 0
    
    # count the number of mass shootings in each csv
    with open(oldest_csv, 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            old_shootings += 1
    with open(newest_csv, 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            new_shootings += 1
    
    # the difference between the # of shootings
    dif = new_shootings - old_shootings
    
    # essentially, if there's a new shooting
    if dif > 0 or True:
        # we should look through the last entries and check what is new.
        check_entries = 15
                
        old_entries = []
        new_entries = []
        
        with open(oldest_csv, 'r') as file:
            csvreader = csv.DictReader(file)
            entries = list(csvreader)

            num_entries = len(entries)

            # Print the newest entries in reverse order
            num_to_print = min(check_entries, num_entries)
                  
            for i in range(num_to_print-1, -1, -1):
                row = entries[i]
                old_entries.append(row)

        print()
        
        with open(newest_csv, 'r') as file:
            csvreader = csv.DictReader(file)
            entries = list(csvreader)
            num_entries = len(entries)

            # Print the newest entries in reverse order
            num_to_print = min(check_entries, num_entries)
            for i in range(num_to_print-1, -1, -1):
                row = entries[i]
                new_entries.append(row)
        
        go_around = 1
        old_on_date = 0
        prev_date = 0
        
        # lets check if new_entries has an entry that old_entries doesn't (i.e. a new shooting)
        for num, new_entry in enumerate(new_entries):
            new_entry_id = new_entry["Incident ID"]

            found = any(new_entry_id == old_entry["Incident ID"] for old_entry in old_entries)

            # if we found a missing entry, we gotta tweet it
            if not found:
                date = new_entry["Incident Date"]
                state = new_entry["State"]
                city = new_entry["City Or County"]
                injured = new_entry["# Victims Injured"]
                killed = new_entry["# Victims Killed"]
              
                injured_people = ""
                killed_people = ""

                if injured != 1:
                    injured_people = "people were"
                else:
                    injured_people = "person was"
                    print("else, person was")

                if killed != 1:
                    killed_people = "people were"
                else:
                    killed_people = "person was"
                    print("else, person was")
                
                print(f"injured people : {injured_people}")
                print(f"killed people : {killed_people}")

                # if the new entry has a different date, reset the go_around counter
                if prev_date and prev_date != date:
                    prev_date = date
                    go_around = 1
                
                # reset old_on_date to 0 or we get massive addition problems
                old_on_date = 0
                for row in old_entries:
                    if row["Incident Date"] == date:
                        old_on_date += 1
                        
                        # current date we're looking at will be previous date soon
                        prev_date = date

                shootings_on_date = old_on_date + go_around
                
                # <summary>
                # to get this value, we need to find the index of the entry.
                # this way if something gets added from previous days,
                # it will count how many shootings happened from that day.
                # and the more i explain this the more i realize that i shouldn't do that.
                # </summary>
                shootings_on_year = old_shootings + num

                #tweeter.tweet(client, f"""
                print(f"""
A mass shooting occurred on {date} in {city}, {state}.

{injured} {injured_people} injured.
{killed} {killed_people} killed.

This makes {shootings_on_date} shooting(s) on {date}.
                """)
                
                # Add this to tweets once calculation is actually good
                # This makes a total of {shootings_on_year} shooting(s) this year)
                
                # add 1 every time we go around; effectively how many shootings there were in the day
                go_around += 1
                
                # wait 5 seconds to make next tweet incase theres more to make (don't want api problems).
                time.sleep(5)
    
    # remove the old file
    os.remove(oldest_csv)

make_comparison()
