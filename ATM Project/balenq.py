import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="nareshit")
cur = con.cursor()

def balenq():
    try:
        print("="*50)
        ac = input("Enter Your Account Number : ")
        pin = input("Enter Your PIN Number : ") 
        data1 = "select Name from atm where account_number=%s and pin=%s"
        cur.execute(data1 %(ac, pin))
        res = cur.fetchone()
        print("-"*50)
        print(f"\tWelcome To Balance Enquiry {res[0]}")
        print("-"*50)
        data2 = "select Name, Account_Number, Balance from atm where account_number=%s"
        cur.execute(data2 %ac)
        for i in [j[0] for j in cur.description]:
            print(f"{i}\t", end="\t")
        print()
        for i in cur.fetchall():
            for j in i:
                print(f"{j}\t", end="\t")
            print()
        print("-"*50)
        data3 = "select balance from atm where account_Number=%s"
        cur.execute(data3 %ac)
        res = cur.fetchone()
        print(f"Your Account Balance is Rs.{res[0]}")
        print("-"*50)
    except TypeError:
        print("Enter Correct Account Number / PIN")
    except mysql.connector.DatabaseError as db:
        print("Problem in : ", db)
