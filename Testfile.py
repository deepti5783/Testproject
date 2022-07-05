import mysql.connector

d = mysql.connector.connect(host="localhost", user="root",password=" ", database="SDB")
if d.is_connected():
    print("Data base connected")

else:
    print("DB is not connected")

c = d.cursor()
c.execute("delete from studentdetails")
#c.execute("CREATE DATABASE SDB")

#c.execute("create table studentdetails(name char(20),age int(4),class int(4), grade char(1))")


#inserting data
c.execute("insert into studentdetails values('vishakha',10,5,'B')")
c.execute("insert into studentdetails values('kartik',9,4,'A')")
c.execute("insert into studentdetails values('krishna',16,11,'B')")
c.execute("insert into studentdetails values('raj',15,10,'B')")
c.execute("insert into studentdetails values('ram',17,12,'A')")

#update data
c.execute("update studentdetails set grade='A' where name='krishna'")

#delete data
c.execute("delete from studentdetails where name='krishna'")
d.commit()

c.execute("select * from studentdetails")
for x in c:
    print(x)