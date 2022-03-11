import json
from datetime import datetime

def pre_process(keyword):
    products = []
    with open(f"raw_data/raw_{keyword}.json", "r") as file:
        for line in file.readlines():
            products.append(json.loads(line))
    print(len(products))

    with open(f"raw_data/{keyword}-pre-process.csv", "w+") as file:
        file.write("PRODUCT, DATE, PRICE\n")
        for product in products:
            name = product["title"].replace("/","").replace(",", "")
            prices = product["AMAZON"]
            timestamp = product["timeStamp"]
            for i in range(0, len(prices), 2):
                temp_date = (timestamp - prices[i]) / 1000
                date = datetime.fromtimestamp(temp_date).strftime("%Y/%m/%d")
                file.write(f"{name}, {date}, {prices[i+1] / 100}\n")