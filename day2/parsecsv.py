""" Boss is asking one question? - 
Load the emps.csv file into the memory then read all the data from the file and remove email column ans remaining data write it in another file.
Use Logging here
"""

import csv

with open("day2/emps.csv",'r') as fr: #file reader
    csv_data=csv.DictReader(fr) # from fr read the data using DictReader and store in csv_data which is a dist
    with open("newemps.csv",'w') as fw:  #fw is a pointer, we can keep any name
        columns=['fname','lname']
        csv_writer=csv.DictWriter(fw,fieldnames=columns,delimiter=',',lineterminator='\n')
        csv_writer.writeheader()
        for row in csv_data:
            del row['email']
            csv_writer.writerow(row)

print("process done")
