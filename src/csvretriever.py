import os
import time
import glob
import shutil


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import datetime
from datetime import datetime

current_dir = os.getcwd()
relative_path = 'src\\csvs'
working_directory = os.path.join(current_dir, relative_path)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.5000.0 Safari/537.36'
}

def get_new_csv():
    csv_url = "https://www.gunviolencearchive.org/reports/mass-shooting"
    export_button_xpath = "//a[@href='/query/0484b316-f676-44bc-97ed-ecefeabae077/export-csv']"
    download_button_xpath = "//a[@class='button big']"

    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--headless=new")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")

    prefs = {
    "download.default_directory": working_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    }

    chrome_options.add_experimental_option("prefs", prefs)

    browser = webdriver.Chrome(options=chrome_options)
    browser.get(csv_url)    
    
    wait = WebDriverWait(browser, 5)
    export_button = wait.until(EC.element_to_be_clickable((By.XPATH, export_button_xpath)))
    export_button.click()

    download_button = wait.until(EC.element_to_be_clickable((By.XPATH, download_button_xpath)))
    download_button.click()

    time.sleep(0.5) # allow the download to complete.

    print("CSV downloaded.")

    # get the time that the file was downloaded
    now = datetime.now()
    dt_string = now.strftime("%d-%H-%M-%S")
    download_filename = dt_string + ".csv"

    files = glob.glob(os.path.join(working_directory, '*'))
    files.sort(key=os.path.getmtime, reverse=True)
    most_recent_file = files[0]

    # now we need to rename the file.
    os.rename(most_recent_file, download_filename)
    shutil.move(download_filename, working_directory)
    
    browser.quit()

def data_clear(name=''):
    if not name:
        for filename in os.listdir(working_directory):
            filepath = os.path.join(working_directory, filename)
            os.remove(filepath)
            break
    else:
        for filename in os.listdir(working_directory):
            filepath = os.path.join(working_directory, name)
            os.remove(filepath)
            break

def get_file_timestamp(filename):
    # Extract the timestamp portion of the file name
    timestamp_str = filename.split('_')[-1].split('.')[0]
    
    # Convert the timestamp string to a datetime object
    return datetime.strptime(timestamp_str, "%d-%H-%M-%S")

def return_oldest_csv():
    file_list = os.listdir(working_directory)
    
    # Filter out non-csv files
    file_list = [file for file in file_list if file.endswith('.csv')]
    
    if len(file_list) < 2:
        return "Insufficient number of files in the directory."
    
    oldest_file = file_list[0]
    oldest_timestamp = get_file_timestamp(oldest_file)
    
    for file in file_list[1:]:
        timestamp = get_file_timestamp(file)
        
        if timestamp < oldest_timestamp:
            oldest_file = file
            oldest_timestamp = timestamp
    
    return oldest_file

def return_newest_csv():
    file_list = os.listdir(working_directory)
    
    # Filter out non-csv files
    file_list = [file for file in file_list if file.endswith('.csv')]
    
    if len(file_list) < 2:
        return "Insufficient number of files in the directory."
    
    newest_file = file_list[0]
    newest_timestamp = get_file_timestamp(newest_file)
    
    for file in file_list[1:]:
        timestamp = get_file_timestamp(file)
        
        if timestamp > newest_timestamp:
            newest_file = file
            newest_timestamp = timestamp
    
    return newest_file