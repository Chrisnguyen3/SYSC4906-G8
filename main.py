import os
import time
import json
from scraper import Scraper
from cleaning import pre_process

import tkinter as tk
from tkinter import filedialog

if __name__ == "__main__":
    scraper = Scraper()

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Choose input file", 
        initialdir=os.getcwd(),
        initialfile="supplies.txt"
    )

    with open(file_path, "r") as f:
        for line in f.readlines():
            keyword = line.replace("\n", "").replace("\\", "").replace("/", " ")
            links = scraper.search(keyword)

            with open(f"raw_data/raw_{keyword}.json", "w+") as f:
                for link in links:
                    f.write(scraper.get_data(link) + "\n")
            
            pre_process(keyword)

    # scraper.quit()