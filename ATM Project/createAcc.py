import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="nareshit")
cur = con.cursor()

def createAcc():
    while True:
        try:
            print("-"*50)
            print("\tC R E A T E A C C O U N T")
            print("-"*50)
            ac = input("Ente Account Number : ")
            if (len(ac)==11):
                ac = int(ac)
                name = input("Enter Your Name : ")
                mob = input("Enter Your Mobile Number : ")
                if (len(mob)==10):
                    mob = int(mob)
                    amt = int(input("Enter Amount to create Account : "))
                    if (amt>=500):
                        pin = input("Enter PIN Number : ")
                        if len(pin)==4:
                            pin = int(pin)
                            ins = "insert into atm values('%s','%s','%s',%d,'%s')"
                            cur.execute(ins %(ac, name, mob, amt, pin))
                            con.commit()
                            print("Account Created Successfully...")
                            break
                        else:
                            print("-"*50)
                            print("You Entered Invalid PIN...Enter 4 DIGIT PIN Number\nTRY AGAIN....")
                    else:
                        print("-"*50)
                        print("To Create New Account Maximum Amount 500 Required...\nTRY AGAIN....")
                else:
                    print("-"*50)
                    print("Invalid Mobile Number....\nTRY AGAIN.......")
            else:
                print("-"*50)
                print("Account Number Should Be 11 Numbers Only\nTRY AGAIN.......")
        except ValueError:
            print("-"*50)
            print("Don't Use Strings/Special Symbols/Alpha-Numerics...\nUse only Interger Numbers\nTRY AGAIN....")
        except mysql.connector.DatabaseError as e:
            print("Problem in : ", e)
