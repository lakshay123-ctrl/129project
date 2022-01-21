import csv


dataset_1 = []
dataset_2 = []

with open("brightstars.csv","r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_1.append(row)



with open("dwarf_stars_sorted.csv","r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_2.append(row)


header1 = dataset_1[0]
star_data1 = dataset_1[1:]
headers2 = dataset_2[0]
star_data2 = dataset_2[1:]


headers = header1+headers2
star_data = []
for index,data_row in enumerate(star_data1):
    star_data.append(star_data1[index]+star_data2[index])



with open("final.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)
    

