import csv

data = []

with open ("dwarf_stars.csv","r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)

headers = data[0]
star_data = data[1:]

for data2 in star_data:
    data2[1] = data2[1].lower()
star_data.sort(key = lambda star_data:star_data[1])
with open ("dwarf_stars_sorted.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data) 

