from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://www.nationalrail.co.uk/live-trains/departures/norwich/")


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

time.sleep(5)

section = driver.find_element(By.ID, "grid-live-trains-results")


ul_element = WebDriverWait(section, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "ul"))
)
li_elements = ul_element.find_elements(By.TAG_NAME, "li")

for i, li in enumerate(li_elements, start=1):
    spans = li.find_elements(By.TAG_NAME, "span")
    span_texts = [span.text.strip() for span in spans if span.text.strip()]
    
    print(span_texts)

driver.close()
