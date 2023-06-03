import requests
import os
import time
import glob
import shutil


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime

current_dir = os.getcwd()
<<<<<<< Updated upstream
relative_path = 'src\\csvs\\'
=======
relative_path = 'src\csvs'
>>>>>>> Stashed changes
working_directory = os.path.join(current_dir, relative_path)
directory = "src\\csvs"

chrome_driver_path = os.path.join(current_dir, "src\\chromedriver.exe")

print(chrome_driver_path)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}

def get_new_csv():
    csv_url = "https://www.gunviolencearchive.org/reports/mass-shooting"
    export_button_xpath = "//a[@href='/query/0484b316-f676-44bc-97ed-ecefeabae077/export-csv']"
    download_button_xpath = "//a[@class='button big']"

    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
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
    dt_string = now.strftime("%d_%H-%M-%S")
    download_filename = "mass_shootings_" + dt_string + ".csv"

    files = glob.glob(os.path.join(directory, '*'))
    files.sort(key=os.path.getmtime, reverse=True)
    most_recent_file = files[0]

    # now we need to rename the file.
    os.rename(most_recent_file, download_filename)
    shutil.move(download_filename, directory)
    
    browser.quit()

# def retrieve_csv():
#     response = requests.get(download_url, headers=headers)

#     if response.status_code == 200:
#         now = datetime.now()
#         dt_string = now.strftime("%d_%H-%M-%S")
        
#         file_name = "mass_shootings_" + dt_string

#         file_path = os.path.join(directory, file_name)
#         with open(file_path, "wb") as file:
#             file.write(response.content)
        
#         print(f"CSV retrieved successfully. ({dt_string})")
#     else:
#         print(response.status_code)
#         print("CSV retrieval unsuccessful.")


def data_clear(name=''):
    if not name:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            os.remove(filepath)
            break
    else:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, name)
            os.remove(filepath)
            break

def remove_csv(file):
    pass

def return_oldest_csv():
    for filename in os.listdir(directory):
        file = filename
        break
    return file

def return_newest_csv():    
    for filename in os.listdir(directory):
        file = filename
    
    return file
