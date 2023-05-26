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

    oldest_csv = os.path.join(get_csv.directory, get_csv.return_oldest_csv())
    latest_csv = os.path.join(get_csv.directory, get_csv.return_oldest_csv())

    now = datetime.now()
    today = now.strftime("%B %d, %Y")

    old_incidents = 0
    new_incidents = 0
    
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
                new_incidents += 1
    
    if old_incidents > 0:
        if new_incidents > old_incidents:
            with open(latest_csv, 'r') as file:
                print("Newest csv is " + str(file.name))
                csvreader = csv.DictReader(file)
                for row in csvreader:
                    if row["Incident Date"] == today:
                        state = row["State"]
                        injured = row["# Victims Injured"]
                        killed = row["# Victims Injured"]
                    num_mass_shootings = sum(1 for row in csvreader)
            print("There has been a new shooting today.")
            
            tweeter.tweet(client, f"""
A mass shooting has occured in {state}.

{injured} people were injured.
{killed} people were killed.

This makes {num_mass_shootings} mass shootings so far this year.
            """)
            
            print("Incident tweeted.")
        else:
            print("There has not been a new shooting today.")
    else:
        print("There has not been any shootings so far today.")
    
    # Remove the oldest CSV effectively making the newest CSV the new oldest.
    #get_csv.remove_csv(oldest_csv)
    os.remove(oldest_csv)

