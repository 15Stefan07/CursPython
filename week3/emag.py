import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import selenium.common.exceptions as exceptions

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.emag.ro/#opensearch')
get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
get_element.send_keys('telefon')
get_element.submit()
# date = browser.find_element(by=By.XPATH, value='//*[@id="card_grid"]')
date = browser.find_elements(by=By.CLASS_NAME, value='card-v2')

for i in date:
    try:
        # print(i.next)
        title_of_product = i.find_element(by=By.CLASS_NAME, value='card-v2-title-wrapper')
        print(title_of_product)
        price = i.find_element(by=By.CLASS_NAME, value='product-new-price')
        print(f"\tTitle: {title_of_product.text}\n\tPrice: {price.text}\n\n\n")
    except selenium.common.exceptions.StaleElementReferenceException:
        pass
    except Exception as e:
        # print("Unexpected error:", e)
        pass
# print(date.text)
time.sleep(10)