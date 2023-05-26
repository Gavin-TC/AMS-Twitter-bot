import tweeter
import csv
import os
import pandas as pd

import csvretriever as get_csv
import csvs

client = tweeter.client()
csv_location = "https://www.gunviolencearchive.org/query/0484b316-f676-44bc-97ed-ecefeabae077/export-csv"

directory = get_csv.folder_path

def data_clear():
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        os.remove(filepath)
    
data_clear()

def return_oldest_csv():
    for filename in os.listdir(directory):
        file = filename
        break
    return file

def return_newest_csv():    
    for filename in os.listdir(directory):
        file = filename
    
    return file