from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import numpy as np

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors
chrome_options.add_argument("--disable-web-security")  # Disable security checks

driver = webdriver.Chrome(options=chrome_options)
path = 'E:\\backup\\github\\proyectosPython\\Utils\\random_useful_programs\\spotify_downloader\\data\\techno_flow_state-6cR4y6y6ExPNk93BodOG56.csv'
path = 'data\\techno_flow_state-6cR4y6y6ExPNk93BodOG56.csv'
df = pd.read_csv(path, encoding='ISO-8859-1', sep=';')

try:
    # Open YouTube
    driver.get("https://www.youtube.com")

    # Accept cookies if prompted (optional, depending on region)
    try:
        input()
        accept_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Aceptar todo')]"))
        )
        accept_button.click()
    except:
        pass  # No cookies prompt
    
    for i, row in df.iterrows():
        # Locate the search bar
        if(type(row['YouTube_Title'])!=str):
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "search_query"))
            )
            # Enter the song name and press Enter
            search_box.send_keys(row['name'] + ' ' + row['artist'] + Keys.RETURN)

            # Wait for results
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//ytd-video-renderer"))
            )

            # Find the first organic result (skip ads)
            organic_results = driver.find_elements(By.XPATH, "//ytd-video-renderer[not(ancestor::ytd-ad-slot)]")
            if organic_results:
                first_video = organic_results[0]
                
                # Get the URL
                video_url = first_video.find_element(By.ID, "thumbnail").get_attribute("href")
                
                # Get the title
                video_title = first_video.find_element(By.XPATH, ".//a[@id='video-title']").text
                
                print(f"First organic result title: {video_title}")
                print(f"First organic result URL: {video_url}")
            else:
                print("No organic results found.")
        break

finally:
    driver.quit()