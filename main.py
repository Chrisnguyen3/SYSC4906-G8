import os
import time
import json
from scraper import Scraper
from cleaning import pre_process

import tkinter as tk
from tkinter import filedialog

if __name__ == "__main__":
    scraper = Scraper()

    # get file of supplies
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Choose input file", 
        initialdir=os.getcwd(),
        initialfile="supplies.txt"
    )

    # get keywords from file
    with open(file_path, "r") as f:
        for line in f.readlines():
            keyword = line.replace("\n", "").replace("\\", "").replace("/", " ")
            links = scraper.search(keyword) # look through search page for links

            with open(f"raw_data/raw_{keyword}.json", "w+") as f:
                for link in links:
                    f.write(scraper.get_data(link) + "\n") # get data from search results
            
            pre_process(keyword) # clean a little

    #TODO: Add graceful error catching
    #TODO: Add logging
    
    scraper.quit()