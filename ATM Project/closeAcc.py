import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="nareshit")
cur = con.cursor()

def closeAcc():
    try:
        print("="*50)
        ac = input("Enter Your Account Number : ")
        pin = input("Enter Your PIN Number : ")
        data1 = "delete from atm where account_number=%s and pin=%s"
        cur.execute(data1 %(ac,pin))
        con.commit()
        print("Your Account Deleted Successfully...")
        print("-"*50)
        print("\tTHANK YOU!!!  VISIT AGAIN!!!")
        print("="*50)
    except TypeError:
        print("Enter Correct Account Number / PIN")
