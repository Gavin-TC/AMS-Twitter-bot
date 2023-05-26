import requests
import os
from datetime import datetime

download_url = "https://www.gunviolencearchive.org/export-finished/download?uuid=0484b316-f676-44bc-97ed-ecefeabae077&filename=public%3A//export-402c5545-b4c5-4051-a2d9-003742886ada.csv"

folder_path = "src\\csvs"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}

def retrieve_csv():
    response = requests.get(download_url, headers=headers)

    if response.status_code == 200:
        now = datetime.now()
        dt_string = now.strftime("%d_%H-%M-%S")
        
        file_name = "mass_shootings_" + dt_string

        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "wb") as file:
            file.write(response.content)
        
        print(f"CSV retrieved successfully. ({datetime})")
    else:
        print(response.status_code)
        print("CSV retrieval unsuccessful.")
