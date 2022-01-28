import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="nareshit")
cur = con.cursor()

def disp():
    try:
        print("="*50)
        ac = input("Enter Your Account Number : ")
        pin = input("Enter Your PIN Number : ") 
        data1 = "select Name,Mobile_no,account_number,balance from atm where account_number=%s and pin=%s"
        cur.execute(data1 %(ac, pin))
        res = cur.fetchone()
        print("-"*50)
        print("\tA C C O U N T  D E T A I L S")
        print("-"*50)
        print(f"\tAccount Number : {res[2]}")
        print("-"*50)
        print(f"Banking Name : {res[0]}\tMobile Number : {res[1]}")
        print("-"*50)
        print(f"\tAvailable Balance : {res[3]}")
        print("="*50)
    except TypeError:
        print("-"*50)
        print("Enter Correct Account Number / PIN")
        print("-"*50)
