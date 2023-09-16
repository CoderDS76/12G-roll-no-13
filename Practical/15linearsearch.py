a=[1,2,3,4,5,6]
c=-1
b=int(input("Enter term to search"))
for i in a:
    c+=1
    if i==b:
        print(f"Found term {b} at index: {c}")