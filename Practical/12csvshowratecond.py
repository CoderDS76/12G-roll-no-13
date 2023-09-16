import csv
f=open("12q.csv")
reader=csv.reader(f)
print("%10s"%"Sno: ","%10s"%"Item: ","%10s"%"Price: ","%10s"%"QOH: ")
print("-"*60)
for i in reader:
    if int(i[2])>200:
        print("%7s"%i[0],"%14s"%i[1],"%9s"%i[2],"%5s"%i[3])
f.close()