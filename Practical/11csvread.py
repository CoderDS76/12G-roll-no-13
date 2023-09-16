import csv
f=open("11q.csv")
reader=csv.reader(f)
print("%10s"%"roll no: ","%10s"%"Name: ","%10s"%"Marks: ")
print("-"*60)
for i in reader:
    print("%5s"%i[0],"%15s"%i[1],"%6s"%i[2])
f.close()