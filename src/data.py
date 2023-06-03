import tweeter
import csv
import os
import pandas as pd
from datetime import datetime

import csvretriever as get_csv

client = tweeter.client()
csv_location = "https://www.gunviolencearchive.org/query/0484b316-f676-44bc-97ed-ecefeabae077/export-csv"

def compare_dates():
    # get_csv.retrieve_csv()
    get_csv.get_new_csv()

<<<<<<< Updated upstream
    oldest_csv = os.path.join(get_csv.directory, get_csv.return_oldest_csv())
    latest_csv = os.path.join(get_csv.directory, get_csv.return_newest_csv())

    now = datetime.now()
    today = now.strftime("%B %d, %Y")

    old_incidents = 0
    new_incidents = 0
=======
def make_comparison():
    ret.get_new_csv()
    directory = ret.working_directory
>>>>>>> Stashed changes
    
    # Check oldest CSV
    with open(oldest_csv, 'r') as file:
        print("Oldest csv is " + str(file.name))
        csvreader = csv.DictReader(file)
        for row in csvreader:
            if row["Incident Date"] == today:
                old_incidents += 1
    
    # Check newest CSV
    with open(latest_csv, 'r') as file:
        print("Newest csv is " + str(file.name))
        csvreader = csv.DictReader(file)
        for row in csvreader:
            if row["Incident Date"] == today:
                print("new incident")
                new_incidents += 1

    print(f"{old_incidents} old incidents")
    print(f"{new_incidents} new incidents")

    difference = new_incidents - old_incidents

    # if we have any incidents today, begin checks.
    # if old_incidents >= 0:
    # if there is a positive difference in incidents, continue
    if difference > 0:
        # now we need to read the oldest of the latest incident.
        # i.e. 1 at 3pm, 1 at 4pm. read the one at 3pm first, then 4pm.
        with open(latest_csv, 'r') as file:
            csvreader = csv.DictReader(file)
            mass_shootings = []

            for row in csvreader:
                if row["Incident Date"] == today:
                    city = row["City Or County"]
                    state = row["State"]
                    injured = row["# Victims Injured"]
                    killed = row["# Victims Killed"]
                    mass_shootings.append({"city": city, "state": state, "injured": injured, "killed": killed})

            num_to_print = min(difference, len(mass_shootings))
            for i in range(num_to_print):
                shooting = mass_shootings[i]
                city = shooting["city"]
                state = shooting["state"]
                injured = shooting["injured"]
                killed = shooting["killed"]
                total_shootings_today = len(mass_shootings)

                tweeter.tweet(client, f"""
A mass shooting has occurred today in {city}, {state}.

{injured} people were injured.
{killed} people were killed.
                        """)
    else:
        print("There has not been any shootings so far today.")
    
<<<<<<< Updated upstream
    # Remove the oldest CSV effectively making the newest CSV the new oldest.
    os.remove(oldest_csv)
    #get_csv.remove_csv(oldest_csv)
=======
    # remove the old file
    os.remove(oldest_csv)
>>>>>>> Stashed changes

