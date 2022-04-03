import csv

#Parameters
#Select csv to filter by specific product name and year
#Averages prices to obtain a single price per date 
filename = "data/Battery bank-pre-process.csv"
name = "INIU Portable Charger USB C Slimmest Triple 3A High-Speed 10000mAh Phone Power Bank Flashlight External Battery Pack Compatible with iPhone 13 12 11 X Samsung S20 Google LG iPad etc [2022 Version]"
year = "2021"


temp_list = []
filtered = {}

with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        item = row[0]
        dates = row[1]
        price = row[2]
        if dates[1:5] == year and item == name:
            if float(price) > 0:
                temp_list.append((dates, price))
         
curr_date = temp_list[0][0]
count = 0
curr_total = 0.0

for i in temp_list:
    if curr_date == i[0]:
        if float(i[1]) > 0.0:
            curr_total += float(i[1])
            count += 1

    else:
        if count > 0:
            filtered[curr_date] = curr_total / count
            curr_date = i[0]
            count = 1
            curr_total = float(i[1])


csv_file = open(filename,"w")
writer = csv.writer(csv_file)
for key, value in filtered.items():
    writer.writerow([name,key,value])
csv_file.close()
