import mysql.connector as my
import time
import warnings
import getpass
import colorama
warnings.filterwarnings(action='ignore')
C=['Country:','Denomination:','Year:','Front side:','Back side:','Material:','Diameter:','Thickness:','\t\t\t\t\t\t\t\t\t   ©','\t\t\t\t\t\t\t\t\t   Last updated on:']
N=['Country:','Denomination:','Year:','Front side:','Back side:','Material:','Length:','Breadth:','Watermark:','\t\t\t\t\t\t\t\t\t   ©','\t\t\t\t\t\t\t\t\t   Last updated on:']
#########################################################################################################
def run1():
    file=open("run.txt","r+")
    lst=file.readlines()
    length=len(lst)                                                    #count
    string=lst[length-1]                                      
    file.close()
    return string
#########################################################################################################
def run2(string):
    file=open("run.txt","r+")
    number=int(string)+1
    file.write(str(number)+"\n")
    lst=file.readlines()
    length=len(lst)
    file.close()
    if length>2:                                                      #clearing count
        file2=open("run.txt","w+")
        file2.write(str(number)+"\n")
        file2.close()
#########################################################################################################
                                                                       #update coin details
def update_c(col,c,v):
    if col.lower()=='country':
        new=input("Enter new country name:")
        cursor2.execute("update coin set country='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='name':
        new=input("Enter new name:")
        cursor2.execute("update coin set name='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='denomination':
        new=int(input("Enter new denomination:"))
        cursor2.execute("update coin set denomination={} where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='year':
        new=input("Enter new year:")
        cursor2.execute("update coin set year='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='front side':
        new=input("Enter new details of front side:")
        cursor2.execute("update coin set front side='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='back side':
        new=input("Enter new details of back side:")
        cursor2.execute("update coin set back side='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='material':
        new=input("Enter new material:")
        cursor2.execute("update coin set material='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='diameter':
        new=input("Enter new diameter:")
        cursor2.execute("update coin set diameter='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='thickness':
        new=input("Enter new thickness:")
        cursor2.execute("update coin set thickness='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    else:
        print("No such field found.")
        global A
        A=False
    mycon2.commit()
#########################################################################################################
   
                                                                             #update note details
def update_n(col,c,v):
    if col.lower()=='country':
        new=input("Enter new country name:")
        cursor2.execute("update note set country='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='name':
        new=input("Enter new name:")
        cursor2.execute("update note set name='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='denomination':
        new=int(input("Enter new denomination:"))
        cursor2.execute("update note set denomination={} where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='year':
        new=input("Enter new year:")
        cursor2.execute("update note set year='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='front side':
        new=input("Enter new details of front side:")
        cursor2.execute("update note set front side='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='back side':
        new=input("Enter new details of back side:")
        cursor2.execute("update note set back side='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='material':
        new=input("Enter new material:")
        cursor2.execute("update note set material='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='length':
        new=input("Enter new length:")
        cursor2.execute("update note set length='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='breadth':
        new=input("Enter new breadth:")
        cursor2.execute("update note set breadth='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    elif col.lower()=='watermark':
        new=input("Enter new watermark:")
        cursor2.execute("update note set watermark='{}' where country='{}' and denomination={}".format(new,c.lower(),v))
    else:
        print("No such field found.")
        global A
        A=False
    mycon2.commit()
########################################################################################################
def addc(c):
    print("\nNOTE: If any field is unknown then please enter 'na'.")
    n=input("Enter your name: ")
    v=int(input("Denomination:"))
    cu2=str(input("Currency name: "))                           #adding coin details
    y=str(input("Year of issue: "))
    f=input("Design on front side:")
    b=input("Design on back side: ")
    e=input("Material: ")
    print("Dimensions↴")
    l=input("Diameter: ")
    s=input("Thickness: ")
    ti=str(time.strftime('%d-%m-%y'))
    V=[n,v,cu2,y,f,b,e,l,s]
    for i in V:
        if i=='na' or i=='NA' or i=='Na' or i=='nA':
            i=None
    mycon=my.connect(host='localhost',user='root',passwd='tejas123',database='numis')
    cursor=mycon.cursor()
    q3="insert into coin values('{}',{},'{}','{}','{}','{}','{}','{}','{}','{}')".format(c,v,y,f,b,e,l,s,n,ti)
    cursor.execute(q3)
    mycon.commit()
    print("Thanks for helping!! :D")
    mycon.close()
    q5="insert into currency values('{}','{}')".format(c,cu2)
    cursor2.execute(q5)
    mycon2.commit()
    print(104*"=")
#########################################################################################################

def addn(c):
    print("\nNOTE: If any field is unknown then please enter 'na'.")
    n=input("Enter your name: ")
    v=int(input("Denomination: "))
    cu2=input("Currency name: ")
    y=str(input("Year of issue: "))                                #adding note details
    f=input("Design on front side: ")
    b=input("Design on back side: ")
    e=input("Material: ")
    print("Dimensions↴")
    l=input("Length: ")
    s=input("Breadth: ")
    w=input("Watermark: ")
    ti=str(time.strftime('%d-%m-%y'))
    V=[n,v,cu2,y,f,b,e,l,s,w]
    for i in V:
        if i=='na' or i=='NA' or i=='Na' or i=='nA':
            i=None
    mycon=my.connect(host='localhost',user='root',passwd='tejas123',database='numis')
    cursor=mycon.cursor()
    q4="insert into note values('{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(c,v,y,f,b,e,l,s,w,n,ti)
    cursor.execute(q4)
    mycon.commit()
    print("Thanks for helping!! :D")
    mycon.close()
    q5="insert into currency values('{}','{}')".format(c,cu2)
    cursor2.execute(q5)
    mycon2.commit()
    print(104*"=")
#########################################################################################################
         
def country(c):
    mycon=my.connect(host='localhost',user='root',passwd='tejas123',database='numis')
    cursor=mycon.cursor()
    t=input("Do you want to know about coin or note? (c/n):")
    if t.lower()=="c":
        q="select denomination from coin where country='{}' order by denomination".format(c,)
        cursor.execute(q)
        data=cursor.fetchall()
        if len(data)!=0:
            print("The available coins of",c.title(),"are:")                #if type= coin
            for i in range(0,len(data)):
                print(data[i][0])
            print("NOTE: If you want to add information about a coin which is not mentioned above,\n    then enter that denomination.")
            v=int(input("Choose the denomination: "))
            print("\n")
            q2="select * from coin where country='{}' and denomination={}".format(c.lower(),v)
            cursor.execute(q2)
            data1=cursor.fetchone()
            if data1!=None:
                print(5*"\t","   DESCRIPTION")
                for i in range(len(data1)):
                    if i==6:
                        print("Dimensions↴")
                    print(C[i],str(data1[i]).capitalize())
            else:
                print("Sorry! We don't have any information about this country. :(")
                a=input("Would you like to help us know about it? (y/n):")
                if a.lower()=="n":
                    print("No problem! :)")
                elif a.lower()!="y":
                    print("Invalid reply! >:(")
                else:
                    addc(c)
        else:
            print("Sorry! We don't have any information about this country. :(")
            a=input("Would you like to help us know about it? (y/n):")
            if a.lower()=="n":
                print("No problem! :)")
            elif a.lower()!="y":
                print("Invalid reply! >:(")
            else:
                addc(c)
               
    elif t.lower()=='n':
        q="select denomination from note where country='{}' order by denomination".format(c,)
        cursor.execute(q)
        data=cursor.fetchall()
        if len(data)!=0:
            print("The available notes of",c.title(),"are:")                 #if type= note
            for i in range(len(data)):
                print(data[i][0])
            print("NOTE: If you want to add information about a note which is not mentioned above,\n    then enter that denomination.")
            v=int(input("Choose the denomination:"))
            print("\n")
            q2="select * from note where country='{}' and denomination={}".format(c,v)
            cursor.execute(q2)
            data1=cursor.fetchone()
            if data1!=None:
                print(5*"\t","   DESCRIPTION")
                for i in range(len(data1)):
                    if i==6:
                        print("Dimensions↴")
                    print(N[i],str(data1[i]).capitalize())
            else:
                print("Sorry! We don't have any information about this country. :(")
                a=input("Would you like to help us know about it? (y/n):")
                if a.lower()=="n":
                    print("No problem! :)")
                elif a.lower()!="y":
                    print("Invalid reply! >:(")
                else:
                    addn(c)
        else:
            print("Sorry! We don't have any information about this country. :(")
            a=input("Would you like to help us know about it? (y/n):")
            if a.lower()=="n":
                print("No problem! :)")
            elif a.lower()!="y":
                print("Invalid reply! >:(")
            else:
                addn(c)  
           
    else:
        print("Invalid reply! >:(")
    mycon.close()
    print(104*"=")
   
########################################################################################################    
string=run1()
print(104*"=","\n",31*" ","✬  WELCOME TO NUMISMATIC GALLERY! ✬",3*"\t","EST. 12-06-2020\n" )
print('''\tNumismatic Gallery is an interface to facilitate the posting and fetching of information of
  currency which is part of our collection. This program will allow viewers of the collection to look
  for the currency they are interested in by entering the country it belongs to. In case the collector
  does not have any currency of that country, it will allow the user to add information about it from
  his side by filling details in fields like year, description, country, denomination and composition.\n''')
print("No. of runs since 13-05-2022:",string,96*" ","-Tejas")
print(104*"=")
choice="y"
z=0                                                                             #pwd
run2(string)
while choice.lower()=="y":
    mycon2=my.connect(host='localhost',user='root',passwd='tejas123',database='numis')
    print(5*"\t","   ✬  MENU  ✬ \n\n",3*"\t","1. Display details",2*"\t","2. Add details\n",3*"\t","3. Update details",2*"\t","4. Delete details\n",3*"\t","5. View catalogue",2*"\t","6. Admin Mode\n",3*"\t","7. Random Search",2*"\t","8. Exit")
    print(104*"=")
    o=int(input("Enter your choice:"))
    if o==1:                                                                    #DISPLAY information
        c=str(input("Enter the name of country:"))
        if c.lower() in ["usa","us","united states"]:
            c="america"
        mycon2=my.connect(host='localhost',user='root',passwd='tejas123',database='numis')
        cursor2=mycon2.cursor()
        cursor2.execute("select cu from currency where country='%s'"%(c.lower().strip(),))
        cu=cursor2.fetchone()
        if cu==None:
            print("Sorry! We don't have any information about this country. :(")
            a=input("Would you like to help us know about it? (y/n):")
            if a.lower()=="n":
                print("No problem! :)")
            elif a.lower()!="y":
                print("Invalid reply! >:(")
            else:
                ty=input("Do you want to add information about coin or note? (c/n):")
                if ty.lower()=='c':
                    addc(c)
                elif ty.lower()=='n':
                    addn(c)
                else:
                    print("Invalid Reply! >:(")
        else:
            print("The currency of",c.title().strip(),"is:",cu[0].title())          
            country(c.lower().strip())

    elif o==2:                                                            #ADD information
        c=str(input("Enter the name of country:"))
        ty=input("Do you want to add information about coin or note? (c/n):")
        cursor2=mycon2.cursor()
        if ty=='c':
            addc(c)
        elif ty=='n':
            addn(c)                                                                              
        else:
            print("Invalid reply! >:(")
    elif o==3:                                                             #UPDATE information
        ty=input("Do you want to update details of coin or note? (c/n):")
        c=input("Enter the name of country:")
        v=int(input("Enter the denomination:"))
        cursor2=mycon2.cursor()
        if ty.lower()=='c':
            cursor2.execute("select * from coin where country='{}' and denomination={}".format(c,v))
            data=cursor2.fetchone()
            if data!=None:
                print(5*"\t","CURRENT DETAILS")
                for i in range(len(data)):
                    if i==6:
                        print("Dimensions↴")
                    print(C[i],str(data[i]).capitalize())
                col=input("Which field do you want to update?: ")
                A=True
                update_c(col,c,v)
                if A==True:
                    print("Details successfully updated.")
            else:
                print("No such information set found!")
           
        elif ty.lower()=='n':
            cursor2.execute("select * from note where country='{}' and denomination={}".format(c,v))
            data=cursor2.fetchone()
            if data!=None:
                print(5*"\t","CURRENT DETAILS")
                for i in range(len(data)):
                    if i==6:
                        print("Dimensions↴")
                    print(N[i],str(data[i]).capitalize())
                col=input("Which field do you want to update?: ")
                A=True
                update_n(col,c,v)
                if A==True:
                    print("Details successfully updated.")
            else:
                print("No such information set found!")
           
        else:
            print("Invalid Reply >:(")
    elif o==4:                                                         #DELETE information
        print(colorama.Back.GREEN+"Ignore the warning below.")
        p=getpass.getpass("Enter the password:")
        pwd=0
        for i in range(len(p)):
            pwd+=ord(p[i])
        if pwd==535:
            print("Hello Sir,")
            ty=input("Do you want to delete information about coin or note? (c/n):")
            c=input("Enter the name of country:")
            v=int(input("Enter the denomination:"))
            cursor2=mycon2.cursor()
            if ty.lower()=='c':
                q="delete from coin where country='{}' and denomination={}".format(c,v)
            elif ty.lower()=='n':
                q="delete from note where country='{}' and denomination={}".format(c,v)
            else:
                print("Invalid Reply!! >:(")
            cursor2.execute(q)
            mycon2.commit()
            count=cursor2.rowcount
            print(count,"information set deleted.")
        else:
            print("Incorrect Password >:(")
            z+=1
            if z>1:
                print(104*"=")
                print("There have been 2 failed login attempts, try again later.")
                print(104*"=")
                break
        print(104*"=")
    elif o==8:                                                                #EXIT
        print(104*"=")
        print("Thanks for visiting :)")
        print(104*"=")
        break
#########################################################################################################
    elif o==5:
        cursor2=mycon2.cursor()
        print(5*"\t","   ✬  MENU  ✬ \n",4*"\t","   1. Overall country catalogue\n",4*"\t","   2. Coin country catalogue\n",4*"\t","   3. Note country catalogue")            
        op=int(input("Enter your choice:"))
        print(104*"=")
        if op==1:
            data=[]
            data1=[]
            print("We have numismatic items from following countries↴:")
            q1="select distinct country from coin order by country"
            cursor2.execute(q1)
            d1=cursor2.fetchall()                                           #Displaying Catalogue
            q2='select distinct country from note order by country'
            cursor2.execute(q2)
            d2=cursor2.fetchall()
            data2=[]
            for i in range(len(d1)):
                data1.append(d1[i][0].lower())
            for i in range(len(d2)):
                data2.append(d2[i][0].lower())
            for i in range(len(d1)):
                data.append(data1[i])
            for i in range(len(data2)):
                if data2[i] not in data:
                    data.append(data2[i])
            data.sort()
            for i in range(len(data)):
                print(data[i].title())
        elif op==2:
            print("We have coins from following countries:↴")
            q="select distinct country from coin order by country"
            cursor2.execute(q)
        elif op==3:
            print("We have notes from following countries:↴")
            q="select distinct country from note order by country"
            cursor2.execute(q)
        else:
            print("Invalid choice!!")
        if op in (2,3):
            data=cursor2.fetchall()
            if data!=None:
                for i in range(len(data)):
                    print(data[i][0].title())
        print(104*"=")
    elif o==6:
        print(colorama.Back.GREEN+"Ignore the warning below.")
        p=getpass.getpass("Enter the password:")
        pwd=0
        for i in range(len(p)):                                             #admin mode
            pwd+=ord(p[i])
        if pwd==535:
            print("Welcome to NumismaticGallery-MySQL")
            q=""
            while q.lower()!="exit":
                q=input()
                if q.lower()!="exit":
                    cursor2=mycon2.cursor()
                    cursor2.execute(q)
                    c=cursor2.rowcount
                    data=cursor2.fetchall()
                    for i in data:
                        if len(i)>1:
                            print(i)
                        else:
                            print(i[0])
                    print(11*"\t",c,"rows affected")
        else:
            print("Incorrect Password >:(")
            z+=1
            if z>1:
                print(104*"=")
                print("There have been 2 failed login attempts, try again later.")
                print(104*"=")
                break
        print(104*"=")
    elif o==7:
        cursor=mycon2.cursor()
        s=input("Search item: ")
        l=s.strip().split(" ")
        t=''
        v=''
        c=''
        for i in l:
            if i=="coin":
                t="coin"
            elif i=="note":
                t="note"
            elif i[0] in "1234567890":
                v=int(i)
            else:
                c=i
        if t=="coin":
            q="select * from coin where country='{}' and denomination={}".format(c,v)
            cursor.execute(q)
            data=cursor.fetchone()
            if data!=None:
                print(5*"\t","   DESCRIPTION")
                for i in range(len(data)):
                    if i==6:
                        print("Dimensions↴")
                    print(C[i],str(data[i]).capitalize())
            else:
                print("Sorry! We don't have any information about this coin. :(")
                a=input("Would you like to help us know about it? (y/n):")
                if a.lower()=="n":
                    print("No problem! :)")
                elif a.lower()!="y":
                    print("Invalid reply! >:(")
                else:
                    addc(c)
        elif t=="note":
            q="select * from note where country='{}' and denomination={}".format(c,v)
            cursor.execute(q)
            data=cursor.fetchone()
            if data!=None:
                print(5*"\t","   DESCRIPTION")
                for i in range(len(data)):
                    if i==6:
                        print("Dimensions↴")
                    print(N[i],str(data[i]).capitalize())
            else:
                print("Sorry! We don't have any information about this note. :(")
                a=input("Would you like to help us know about it? (y/n):")
                if a.lower()=="n":
                    print("No problem! :)")
                elif a.lower()!="y":
                    print("Invalid reply! >:(")
                else:
                    addn(c)
        else:
            print("No results found!!")
    else:
        print("Invalid  choice! >:(")
    print(104*"=")
    choice=input("Do you want to continue? (y/n):")                          
    if choice.lower()=='n':
        print("Thanks for visiting :)")
    if choice.lower() not in ('y','n'):
        print("Invalid reply! >:(")
    mycon2.close()
    print(104*"=")
#########################################################################################################