import json
from datetime import datetime

def pre_process(keyword):
    products = []

    try:
        file_name = f"raw_data/raw_{keyword}.json"
        with open(file_name, "r") as file:
            for i, line in enumerate(file.readlines()):
                try:
                    products.append(json.loads(line))
                except Exception as e:
                    print(f"Malformed JSON on line {i} of {file_name}", e)
    except Exception as e:
        return print(f"Error reading raw json for {keyword}", e)

    try: 
        with open(f"raw_data/{keyword}-pre-process.csv", "w+") as file:
            file.write("PRODUCT, DATE, PRICE\n")
            for product in products:
                try:
                    name = product["title"].replace("/","").replace(",", "")
                    prices = product["AMAZON"]
                    timestamp = product["timeStamp"]
                    for i in range(0, len(prices), 2):
                        temp_date = (timestamp - prices[i]) / 1000
                        date = datetime.fromtimestamp(temp_date).strftime("%Y/%m/%d")
                        file.write(f"{name}, {date}, {prices[i+1] / 100}\n")
                except Exception as e:
                    print(f"Error pre-processing date and prices for {keyword}", e)
    except Exception as e:
        print(f"Error pre-processing date and prices for {keyword}", e)

if __name__ == "__main__":
    import sys
    for arg in sys.argv[1:]:
        pre_process(arg)