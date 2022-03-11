import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def load(url):
    driver.get(url)

def find_element(css_selector):
    return driver.find_element(By.CSS_SELECTOR, css_selector)

def find_elements(css_selector):
    return driver.find_elements(By.CSS_SELECTOR, css_selector)

d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(desired_capabilities=d)
driver.implicitly_wait(5)
keyword = "water"
url = f"https://keepa.com/#!search/1-{keyword}"
load(url)

products = find_elements('div.content div.ag-center-cols-container div.ag-row div[col-id="title"] a')
links = [product.get_attribute('href') for product in products]
print(links)

for link in links:
    load(link)
    find_element('div.productTableDescriptionTitle')
    time.sleep(1)

    driver.execute_script('console.log(JSON.stringify(dataProduct))')
    time.sleep(1)

time.sleep(2)
logs = driver.get_log('browser')

driver.quit()

product_dicts = []
with open("test.json", "w+") as file:
    for log in logs:
        if "AMAZON" in log["message"]:
            dump = json.dumps(log["message"]).replace("\\", "")
            opening_bracket = dump.find("{")
            dump = dump[opening_bracket:-2]
            product_dicts.append(json.loads(dump))
            file.write(dump + "\n")

for product in product_dicts:
    with open(product["title"].replace("/","") + ".csv", "w+") as file:
        for i in range(len(product["AMAZON"], step=2)):
            file.write(pro)
