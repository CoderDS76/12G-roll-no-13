import pickle
found=False
f=open("rolldata.bin","rb")
rn=int(input("Enter roll no: "))
data=pickle.load(f)
d=0
for i in data:
    if i["roll:"]==rn:
        d=i
        found=True
        break
if found:
    newm=int(input("Enter new marks: "))
    d["marks:"]=newm
else:
    print("Roll number not found")
f.close()
f=open("rolldata.bin","wb")
pickle.dump(data,f)
print(data)
f.close()