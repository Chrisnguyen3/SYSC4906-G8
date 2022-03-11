if __name__ == "__main__":
    import os
    import sys
    import time
    import json
    import logging

    from scraper import Scraper
    from cleaning import pre_process

    import tkinter as tk
    from tkinter import filedialog

    logging.basicConfig(filename='scraper.log')

    try:
        scraper = Scraper()

        keywords = []
        if (len(sys.argv) > 1):
            keywords = sys.argv[1:]
        else:
            # get file of supplies
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename(
                title="Choose input file", 
                initialdir=os.getcwd(),
                initialfile="supplies.txt"
            )

            with open(file_path, "r") as f:
                keywords = [line.replace("\n", "") for line in f.readlines()]

        # get keywords from file
        for keyword in keywords:
            links = scraper.search(keyword) # look through search page for links

            with open(f"raw_data/raw_{keyword}.json", "w+") as f:
                for link in links:
                    f.write(scraper.get_data(link) + "\n") # get data from search results
            
            pre_process(keyword) # clean a little
    except Exception as e:
        logger.error("Error in main scraper", e)

    #TODO: Add graceful error catching
    #TODO: Add logging
    scraper.quit()