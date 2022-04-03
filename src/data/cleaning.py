import json
import logging
from datetime import datetime, timedelta

def pre_process(keyword=None, file_name=None):
    products = []

    try:
        if file_name == None:
            file_name = f"raw_data/raw_{keyword}.json"
        
        with open(file_name, "r") as file:
            for i, line in enumerate(file.readlines()):
                try:
                    products.append(json.loads(line))
                except Exception as e:
                    logging.error(f"Malformed JSON on line {i} of {file_name}", e)
    except Exception as e:
        return logging.error(f"Error reading raw json for {keyword}", e)

    try: 
        with open(f"raw_data/{keyword}-pre-process.csv", "w+") as file:
            file.write("PRODUCT, DATE, PRICE\n")
            for product in products:
                try:
                    name = product["title"].replace("/","").replace(",", "")
                    prices = product["MARKET_NEW"]
                    current_time = product["lastUpdate"]
                    for i in range(0, len(prices), 2):
                        time_delta = timedelta(minutes=(current_time - prices[i]))
                        date = datetime.now() - time_delta
                        date_str = date.strftime("%Y/%m/%d")
                        file.write(f"{name}, {date_str}, {prices[i+1] / 100}\n")
                except Exception as e:
                    logging.error(f"Error pre-processing date and prices for {keyword}", e)
    except Exception as e:
        logging.error(f"Error pre-processing date and prices for {keyword}", e)
    
    logging.info(f"Finished processing keyword={keyword} or file={file_name}")

if __name__ == "__main__":
    import os
    import sys
    
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            pre_process(arg)
    else:
        cwd = os.getcwd()
        for file_path in os.listdir(cwd + '\\raw_data\\'):
            if 'raw_' in file_path and '.json' in file_path:
                pre_process(file_name=f"raw_data/{file_path}")