import pickle
found=False
r=int(input("Enter roll no: "))
f=open("data.bin","rb")
data= pickle.load(f)
for i in data.keys():
    if i==r:
        found=True
        break
if found:
    print("Name: ",data[r])
else:
    print("Roll Number not found")
print(data)
f.close()