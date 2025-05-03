from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

station = "london-liverpool-street"

driver.get(f"https://www.nationalrail.co.uk/live-trains/departures/{station.lower()}/")


try:
    cookie_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))
    )
    cookie_button.click()
    print("Cookie banner dismissed.")
except:
    print("No cookie banner found or timed out.")



# search = driver.find_element(By.ID, "live-trains-origin")
# search.send_keys("norwich")
# search.send_keys(Keys.RETURN)

# time.sleep(5)



section = driver.find_element(By.ID, "grid-live-trains-results")


ul_element = WebDriverWait(section, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "ul"))
)
li_elements = ul_element.find_elements(By.TAG_NAME, "li")



for i, li in enumerate(li_elements, start=0):
    
    

    station_title = li.find_element(By.CLASS_NAME, "cwnatJ").text
    arrival_time = li.find_element(By.CLASS_NAME, "bVsjOO").text
    try:
        on_time = li.find_element(By.CLASS_NAME, "gOVYjf").text
    except:
        on_time = False
    try:
        late = li.find_element(By.CLASS_NAME, "HkKYv").text
    except:
        late = False
    platform_number = li.find_element(By.CLASS_NAME, "iXOvam").text

    train_info = {
        "from" : station,
        "to" : station_title,
        "leave_time" : arrival_time,
        "on_time" : on_time,
        "late" : late,
        "platform_number" : platform_number
    }
    
    print(train_info["from"])
    print(train_info["to"])
    print(train_info["leave_time"])
    print(train_info["on_time"])
    print(train_info["late"])
    print(train_info["platform_number"])

driver.close()
