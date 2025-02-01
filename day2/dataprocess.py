# Reader and Writer

from csv import writer #from csv module importing writer and reader function
from csv import reader

default_text = "Some Text"

with open("day2/data.csv",'r') as read_obj:
    with open("newdata.csv",'w',newline='') as write_obj:
        csv_reader = reader(read_obj)
        csv_writer = writer(write_obj)
        for row in csv_reader:
            row.append(default_text)
            csv_writer.writerow(row)

print("All wwork done")