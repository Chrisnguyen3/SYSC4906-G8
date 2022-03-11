import time
import json
from scraper import Scraper
from cleaning import pre_process

if __name__ == "__main__":
    scraper = Scraper()

    print("What do you want to search? ")
    keyword = input()
    links = scraper.search(keyword)

    with open(f"raw_data/raw_{keyword}.json", "w+") as f:
        for link in links:
            f.write(scraper.get_data(link) + "\n")
    
    pre_process(keyword)

    scraper.quit()