f=open("myfile.txt","r")
vowel=["A","E","I","O","U"]
cons=['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
a=f.read()
v=0
c=0
u=0
l=0
for i in a:
    for j in i:
        if j.upper() in vowel:
            v+=1
        if j.upper() in cons:
            c+=1
        if j.isupper():
            u+=1
        if j.islower():
            l+=1
print("The number of vowels in the file is: ",v)
print("The number of consonants in the file is: ",c)
print("The number of uppercase letters in the file is: ",u)
print("The number of lowercase letters in the file is: ",l)
f.close()