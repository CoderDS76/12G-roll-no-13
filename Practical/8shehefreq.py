f=open("F:\Dhawal\Class 12\CS\Practical\8.txt","r")
h=f.readlines()
hc=0
sc=0
for i in h:
    hc+=i.count("He")
    sc+=i.count("She")
print("The frequency of He in file is: ",hc)
print("The frequency of She in file is: ",sc)
f.close()