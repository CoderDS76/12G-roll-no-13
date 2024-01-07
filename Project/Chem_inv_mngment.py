import mysql.connector as mysql
import csv 

mycon=mysql.connect(host="localhost",user="root",password="saxena123")
mycur=mycon.cursor()
mycur.execute("create database if not exists cheminv;")
mycur.execute("use cheminv;")
mycur.execute("create table if not exists UserInfo(username char(20),password char(20));")
mycon.commit()
while True:
    print("Welcome to Chemical Inventory Management! ",end="\n\n")
    print("1: SignUp")
    print("2: Login")
    ans=input("Enter your choice (1/2): ")
    if ans=="1":
        username=input("Enter the username: ")
        password=input("Enter the password: ")
        mycur.execute("insert into UserInfo Values(\"{0}\",\"{1}\");".format(username,password))
        mycon.commit()
        print("Successfully added!! ")
    elif ans=="2":
        username=input("Enter the username: ")
        mycur.close()
        mycur=mycon.cursor()
        mycur.execute("select username from UserInfo where username=\"{0}\";".format(username))
        x=mycur.fetchall()
        if len(x)!=0:
            password=input("Enter the password: ")
            mycur.close()
            mycur=mycon.cursor()
            mycur.execute("select password from UserInfo where password=\"{0}\";".format(password))
            y=mycur.fetchall()
            if len(y)!=0:
                print("Login Successful!!")
                mycur.close()
                mycur=mycon.cursor()
                mycur.execute("create table if not exists Inv(Id int primary key AUTO_INCREMENT,name char(40),casnum char(13),price float, unit char(10),qty int,lstockqty int);")
                mycur.execute("create table if not exists Log(s_Id int primary key AUTO_INCREMENT,CustomerName char(20),PhoneNumber char(10), id int,Quantity int(100),SPrice float,foreign key (id) references Inv(id));")
                mycon.commit()
                while True:
                    print("1: Add Chemicals ")
                    print("2: Edit Qty")
                    print("3: Sell Chemicals")
                    print ("4: Search Chemicals")
                    print("5: Sales Log")
                    print("6: Total Revenue")
                    print("7: Available Chemicals")
                    print("8: Check Low stocks")
                    print("9: Generate CSV report on inventory")
                    print("10: Import Data from CSV(file must be in same directory as program with correct format): ")
                    print("0: Exit")
                    a=int(input("Enter your choice: "))
                    if a==1:
                        mycur.close()
                        mycur=mycon.cursor()
                        print("All information prompted are mandatory to be filled")
                        Chemicalname=input("Enter Chemical Name: ")
                        casnum=input("Enter Cas Number(2_7dig-2dig-checkdig): ")
                        price=int(input("Enter the price: "))
                        unit=input("Enter unit: ")
                        quantity=int(input("Enter quantity: "))
                        lstockqty=int(input("Enter low stock quantity alert: "))
                        mycur.execute("select * from Inv where name=\"{0}\";".format(Chemicalname))
                        row=mycur.fetchall()
                        if len(row)!=0:
                            print("Chemical already exists!! ")
                        else:
                            mycur.close()
                            mycur=mycon.cursor()
                            mycur.execute("insert into Inv(name,casnum,price,unit,qty,lstockqty) values(\"{0}\",\"{1}\",{2},\"{3}\",{4},{5}); ".format(Chemicalname,casnum,price,unit,quantity,lstockqty))
                            mycon.commit()
                            print("Successfully Added!!")
                    elif a==2:
                        
                        print("All information prompted are mandatory to be filled")
                        Chemicalname=input("Enter Chemical Name: ")
                        quantity=int(input("Enter quantity: "))
                        mycur.close()
                        mycur=mycon.cursor()
                        mycur.execute("select * from Inv where name=\"{0}\";".format(Chemicalname))
                        row=mycur.fetchall()
                        if len(row)!=0:
                            mycur.close()
                            mycur=mycon.cursor()
                            mycur.execute("update Inv set qty={0} where name=\"{1}\";".format(quantity,Chemicalname))
                            mycon.commit()
                            print("Successfully Edited!!")
                        else:
                            print("Chemical is not in inventory!!")

                    elif a==3:
                        
                        print("AVAILABLE Chemicals")
                        mycur.close()
                        mycur=mycon.cursor()
                        mycur.execute("select * from Inv; ")
                        x=mycur.fetchall()
                        for i in x:
                            print(i)
                        cusname=input("Enter customer name: ")
                        phno=int(input("Enter phone number: "))
                        Id=int(input("Enter Id: "))
                        price=int(input("Enter the price: "))
                        n=int(input("Enter quantity(mind the units!!): "))
                        Sprice=n*price
                        mycur.close()
                        mycur=mycon.cursor()
                        mycur.execute("select qty from Inv where Id={0};".format(Id))
                        lk=mycur.fetchall()
                        if max(lk)<n:
                            print(n,"Chemical Quantity required is not available!!!!")
                        else:
                            mycur.close()
                            mycur=mycon.cursor()
                            mycur.execute("select Id from Inv where Id={0};".format(Id))
                            log=mycur.fetchall()
                            if len(log)!=0:
                                mycur.close()
                                mycur=mycon.cursor()
                                mycur.execute("insert into Log(CustomerName,PhoneNumber,id,Quantity,SPrice) values(\"{0},\",{1},{2},{3},{4};".format(cusname,phno,Id,n,Sprice))
                                mycur.close()
                                mycur=mycon.cursor()
                                mycur.execute("update Inv set qty=qty-{n} where Id={id};".format(n,Id))
                                mycon.commit()
                                print("Successfully sold and logged!! ")
                            else:
                                print("Chemical is NOT AVAILABLE!! ")

                    elif a==4:
                        print("1: Search by Chemical name: ")
                        print("2: Search by Cas No: ")
                        l=int(input("Search by?: "))
        #BY Chemical name
                        if l==1:
                            s=input("Enter Chemical to search: ")
                            mycur.close()
                            mycur=mycon.cursor()
                            mycur.execute("select name from Inv where name=\"{0}\";".format(s))
                            ava=mycur.fetchall()
                            if len(ava)!=0:
                                print("Chemical is in Stock!! ")
                                mycur.execute("select * from Inv where name=\"{0}\";".format(s))
                                x=mycur.fetchall()
                                for i in x:
                                    print(i)
                            else:
                                print("CHEMICAL IS NOT IN STOCK!! ")
        #BY casnum
                        elif l==2:
                            g=input("Enter Cas no to search: ")
                            mycur.close()
                            mycur=mycon.cursor()
                            mycur.execute("select casnum from Inv where casnum=\"{0}\";".format(g))
                            ava=mycur.fetchall()
                            if len(ava)!=0:
                                print("Chemical is in stock!! ")
                                mycur.execute("select * from Inv where casnum=\"{0}\";".format(g))
                                x=mycur.fetchall()
                                for i in x:
                                    print(i)
                            else:
                                print("CHEMICAL IS NOT IN STOCK!! ")
                    elif a==5:
                        print("1:Log details")
                        print("2:Reset Log")
                        ty=int(input("Enter your choice: "))
                        if ty==1:
                            mycur.close()
                            mycur=mycon.cursor()
                            mycur.execute("select * from Log;")
                            u=mycur.fetchall()
                            for i in u:
                                print(i)
                        if ty==2:
                            ask=input("Are you sure(Y/N):")
                            if ask.upper()=="Y":
                                mycur.close()
                                mycur=mycon.cursor()
                                mycur.execute("delete from Log;")
                                mycon.commit()
                            elif ask.upper()=="N":
                                pass
                    elif a==6:
                        mycur.close()
                        mycur=mycon.cursor()
                        mycur.execute("select sum(SPrice) from Log;")
                        rev=mycur.fetchall()
                        print("Total Revenue is: ",rev)
                    elif a==7:
                        mycur.close()
                        mycur=mycon.cursor()
                        mycur.execute("select * from Inv order by Id;")
                        v=mycur.fetchall()
                        for i in v:
                            print(i)
                    elif a==8:
                        mycur.close()
                        mycur=mycon.cursor()
                        mycur.execute("select name,qty,lstockqty from Inv where qty<(lstockqty+1);")
                        j=mycur.fetchall()
                        for i in j:
                            print(i)
                    elif a==9:
                        f=open("InvData.csv",mode="w")
                        writer=csv.writer(f)
                        mycur.close()
                        mycur=mycon.cursor()
                        mycur.execute("select * from Inv;")
                        k=mycur.fetchall()
                        for i in k:
                            writer.writerow(i)
                        f.close()
                        i=open("ChemLogData",mode="w")
                        writer=csv.writer(i)
                        mycur.close()
                        mycur=mycon.cursor()
                        mycur.execute("select * from Log;")
                        k=mycur.fetchall()
                        for m in k:
                            writer.writerow(m)
                        i.close()
                    elif a==10:
                        file=input("Enter File name: ")
                        f=open("{0}.csv".format(file),mode="r")
                        reader=csv.reader(f)
                        for da in reader:
                            Chemicalname=da[0]
                            casnum=da[1]
                            price=da[2]
                            unit=da[3]
                            quantity=da[4]
                            lstockqty=da[5]
                            mycur.close()
                            mycur=mycon.cursor()
                            mycur.execute("insert into Inv(name,casnum,price,unit,qty,lstockqty) values(\"{0}\",\"{1}\",{2},\"{3}\",{4},{5}); ".format(Chemicalname,casnum,price,unit,quantity,lstockqty))
                            mycon.commit()
                        print("Successfully Added from CSV!!")
                        f.close()
                    elif a==0:
                        quit=True
                        break
            else:
                print("INCORRECT PASSWORD!! ")
        else:
            print("INCORRECT USERNAME!! ")
    else:
        print("Incorrect Choice! ")
    if quit==True:
        break
print("Thank You for Using Chemical Inventory Management System! ")