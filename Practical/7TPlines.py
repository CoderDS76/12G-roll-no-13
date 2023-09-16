f=open("myfile.txt","r")
k=open("TptPfile.txt","w")
while True:
    c=f.readline()
    if not c:
        break
    if c[0].lower()=="t" or c[0].lower()=="p":
        k.write(c)
f.close()
k.close()