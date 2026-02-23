
import csv

f=open("/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/data.csv", "r")

csvReader=csv.reader(f)
print(csvReader)

# for rows in csvReader():
#     print(rows)




#CSV DicReader

ff=open("/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/data.csv", "r")

rdr=csv.DictReader(f)

for row in rdr():
    print(row)
    f.close()