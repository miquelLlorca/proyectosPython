from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
import numpy as np


chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors
chrome_options.add_argument("--disable-web-security")  # Disable security checks

driver = webdriver.Chrome(options=chrome_options)
path = 'E:\\backup\\github\\proyectosPython\\Utils\\random_useful_programs\\spotify_downloader\\data\\techno_flow_state-6cR4y6y6ExPNk93BodOG56.csv'
path = 'data\\techno_flow_state-6cR4y6y6ExPNk93BodOG56.csv'
df = pd.read_csv(path, encoding='ISO-8859-1', sep=';')

if('downloaded' not in df.columns):
    df['downloaded'] = [False for i in range(len(df))]
    
try:
    driver.get("https://y2mate.nu/en-efXo/")  # Replace with your webpage URL

    for i, row in df.iterrows():
        # 1. Look for the textbox
        textbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "video")))

        if(type(row['YouTube_URL'])==str and not row['downloaded']):
            # 2. Write some data
            textbox.send_keys(row['YouTube_URL'])

            # 3. Click on convert button
            convert_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Convert']"))
            )
            convert_button.click()

            # 4. Wait for download button to appear and click it
            dowload_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Download']"))
            )
            dowload_button.click()
            
            # 5. Sleep for a bit so downloads have time to finish
            time.sleep(2)
            df.at[i, 'downloaded'] = True
            df.to_csv(path, index=False, sep=';')
            print(f'Downloaded {i} - {row["YouTube_Title"]}')
            
            # 6. Click on next to continue donwloading
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))
            )
            next_button.click()
            


finally:
    df.to_csv(path, index=False, sep=';')
    driver.quit()