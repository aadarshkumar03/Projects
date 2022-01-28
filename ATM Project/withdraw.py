from exceptions import InsufficientBalanceError,WithdrawError
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="nareshit")
cur = con.cursor()

def withdraw():
    try:
        print("="*50)
        ac = input("Enter Your Account Number : ")
        pin = input("Enter Your PIN Number : ") 
        amt1 = int(input("Enter withdraw Amount : "))
        data1 = "select balance from atm where account_number=%s and pin=%s"
        cur.execute(data1 %(ac,pin))
        res = cur.fetchone()
        if amt1<0:
            raise WithdrawError
        if amt1+500<=res[0]:
            amt2 = res[0] - amt1
            data2 = "update atm set balance=%d where account_number=%s"
            cur.execute(data2 %(amt2, ac))
            con.commit()
            print("="*50)
            print(f"Rs.{amt1} Withdraw from Your A/C {ac}")
            data3 = "select Account_Number,Name,Balance from atm where account_number=%s"
            cur.execute(data3 %ac)
            print("="*50)
            for i in [j[0] for j in cur.description]:
                print(f"{i}\t", end="\t")
            print()
            print("-"*50)
            for k in cur.fetchall():
                for l in k:
                    print(f"{l}\t", end="\t")
                print()
            print("="*50)
        else:
            raise InsufficientBalanceError
    except TypeError:
        print("="*50)
        print("Enter Correct Account Number / PIN")
        print("="*50)
    except mysql.connector.DatabaseError as db:
        print("Problem in : ",db)
    
