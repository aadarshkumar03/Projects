import mysql.connector
try:
    con=mysql.connector.connect(host="localhost", user="root", passwd="root", database="NareshIT")
    cur=con.cursor()
    ct="create table atm(Account_Number varchar(12) primary key, Name varchar(20) not null, Mobile_No varchar(11) not null, Balance int(20) not null, PIN varchar(5) not null)"
    cur.execute(ct)
    print("Table Created Successfully....Verify...")
except mysql.connector.DatabaseError as db:
    print("Problem in : ",db)
