from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time
import requests
from bs4 import BeautifulSoup
import os

base_url = 'https://seriesmoyo.blogspot.com'
# driver_path = '/mnt/c/Users/pkvj2/Downloads/geckodriver.exe'
driver_path = 'C:\\Users\\pkvj2\\Downloads\\geckodriver.exe'


options = Options()
# options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################
# Getting the URLs

# os.environ['MOZ_HEADLESS'] = '1'
service = Service(driver_path)
driver = webdriver.Firefox(service=service, options=options)
driver.get(base_url)
post_titles = []
wait_time = 2 # s
time.sleep(wait_time) 
try:
    i = 1
    while True:
        # Wait until the post titles are present
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.post-title'))
        )

        # Find all post titles
        titles = driver.find_elements(By.CSS_SELECTOR, '.post-title')
        for title in titles:
            if(title.text != ""):
                post_titles.append(title.text)

        # Find and click the "Next" button to go to the next page
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, '.page-num.page-next')
            next_button.click()
            time.sleep(wait_time) 
        except Exception as e:
            print("No more pages or error:", e)
            break
        print(i)
        i+=1
        # if(i==5):
        #     break
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()


# out_path = '\\wsl.localhost\\Ubuntu-22.04\\home\\miquel\\proyectosPython\\random\\series_extractor\\titles.txt'
out_path = 'C:\\Users\\pkvj2\\Downloads\\titles.txt'
with open(out_path,'w') as out:
    out.write("\n".join(post_titles))

# Print the first few URLs to verify
# print(post_titles)
# print()
print()
print()
print(post_titles[:5])




