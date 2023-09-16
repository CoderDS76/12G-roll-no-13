f=open("afile.txt","r")
k=open("notafile.txt","w")
while True:
    c=f.readline()
    if not c:
        break
    if c[0]!="a":
        k.write(c)
f.close()
k.close()