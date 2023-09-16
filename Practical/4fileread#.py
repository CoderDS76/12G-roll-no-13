f=open("myfile.txt","r")
while True:
    a=f.readline()
    b=a.replace(" ","#")
    if not a:
        break
    print(b.strip())
f.close()