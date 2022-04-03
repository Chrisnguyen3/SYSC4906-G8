import time
import json
from driver import Driver

class Scraper(Driver):
    def search(self, keyword):
        url = f"https://keepa.com/#!search/1-{keyword}"
        self.load(url)

        products = self.find_elements('div.content div.ag-center-cols-container div.ag-row div[col-id="title"] a')
        return [product.get_attribute('href') for product in products]
    
    def get_data(self, url):
        self.load(url)
        self.find_element('div.productTableDescriptionTitle')
        time.sleep(1)
        
        try:
            refresh = self.find_element('i.fa-refresh')
            refresh.click() 
            time.sleep(1)
        except:
            pass

        self.execute_script('console.log(JSON.stringify(dataProduct))')
        time.sleep(1)

        log = self.logs().pop()
        if "AMAZON" in log["message"]:
            dump = json.dumps(log["message"]).replace("\\", "")
            opening_bracket = dump.find("{")
            return dump[opening_bracket:-2] #return JSON object
        
        return None
    
    def quit(self):
        self.driver.quit()

if __name__ == "main":
    scraper = Scraper()
    scraper.search("Water")