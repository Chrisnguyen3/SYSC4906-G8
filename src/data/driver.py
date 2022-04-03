import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Driver:
    driver = None
    def __init__(self):
        d = DesiredCapabilities.CHROME
        d['goog:loggingPrefs'] = { 'browser':'ALL' }
        self.driver = webdriver.Chrome(desired_capabilities=d)
        self.driver.implicitly_wait(5)

    def load(self, url):
        self.driver.get(url)

    def find_element(self, css_selector):
        return self.driver.find_element(By.CSS_SELECTOR, css_selector)

    def find_elements(self, css_selector):
        return self.driver.find_elements(By.CSS_SELECTOR, css_selector)
    
    def execute_script(self, script):
        self.driver.execute_script(script)
    
    def logs(self):
        return self.driver.get_log('browser')

    def quit(self):
        self.driver.quit()