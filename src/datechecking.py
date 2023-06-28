import time
import datetime
import calendar
import tweeter
import csv
import os
import csvretriever as ret

from globals import GLOBAL_TEST_BOOL
from globals import GLOBAL_MONTH_CHECKING

month_dict = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month_word_dict = {
    1: "January",
    2: "Febuary",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def get_leapyear(year) -> bool:
    return calendar.isleap(year=year)

def convert_date(month):
    return month_word_dict[month]

def get_end_of_year(month, day) -> bool:    
    if month == 12:
        return day == month_dict[month]
    return False
    
def edit_leapyear(year):
    leapyear = get_leapyear(year)
    if leapyear:
        month_dict[2] = 29
    else:
        month_dict[2] = 28

# return [bool] if today is end of month
def return_month_status(month, day):
    return month_dict[month] == day

def tweet_results(month_shootings, injured, killed, year_shootings, injured_people="people were", killed_people="people were"):
    # if it's the end of the month
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    
    edit_leapyear(year)
    
    if get_end_of_year(month, day):
        end_of_year = " so far."
    else:
        end_of_year = ""
            
        prompt = str(f"""
Results for the month:

    This month there was {month_shootings} mass_shootings.
    {injured} {injured_people} injured this month.
    {killed} {killed_people} killed this month.
    
    {year_shootings} mass shootings this year{end_of_year}.
                    """)
        
        if not GLOBAL_TEST_BOOL:
            tweeter.tweet(tweeter.client(), prompt)
        else:
            print(prompt)

def make_checks():
    time.sleep(8)
    
    print("Date checking working!")
    
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    month_word = convert_date(datetime.datetime.now().month)
    day = datetime.datetime.now().day
    
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    time_format = str(hour) + " " + str(minute)
    
    month_shootings = 0
    injured = 0
    killed = 0
    year_shootings = 0
    injured_people = ""
    killed_people = ""
    
    while GLOBAL_MONTH_CHECKING:
        if return_month_status(month, day) and time_format == "24 59" or GLOBAL_TEST_BOOL:
            
            directory = ret.working_directory
            newest_csv = os.path.join(directory, ret.return_newest_csv())
            
            date = f"{month_word} {day}, {year}"
            
            with open(newest_csv, 'r') as file:
                csvreader = csv.DictReader(file)
                for row in csvreader:
                    if str(month) in row["Incident Date"]:
                        month_shootings += 1
                        injured += int(row["# Victims Injured"])
                        killed += int(row["# Victims Killed"])
            if injured == 1:
                injured_people = "person was"
            else:
                injured_people = "people were"
            
            if killed == 1:
                killed_people = "person was"
            else:
                killed_people = "people were"
            
            tweet_results(
                        month_shootings,
                        injured, 
                        killed, 
                        year_shootings,
                        injured_people,
                        killed_people
                        )
        time.sleep(60)
        
# year = datetime.datetime.now().year
# month = convert_date(datetime.datetime.now().month)
# day = datetime.datetime.now().day
# date = f"{month} {day}, {year}"
# print(date)

# if GLOBAL_TEST_BOOL:
#     make_checks()