# main program
from createAcc import createAcc
from deposit import deposit
from withdraw import withdraw
from balenq import balenq
from disp import disp
from closeAcc import closeAcc
from exceptions import *


def demo():
    while True:
        try:
            print("-"*50)
            print("\t\tW E L C O M E ")
            print("-"*50)
            print("\t1.Create New Account\n\t2.Deposit Amount\n\t3.Withdraw Amount\n\t4.Balance Enquiry\n\t5.Display Customer Details\n\t6.Close Account\n\t7.Exit")
            print("-"*50)
            ch = int(input("Select Option : "))
            if (ch==1):
                createAcc()
                break
            elif (ch==2): 
                try:
                    deposit() 
                    break
                except DepositeError:
                    print("-"*50)
                    print("Don't try to Deposite Negative Amount")
            elif (ch==3):
                try:
                    withdraw()
                    break
                except WithdrawError:
                    print("-"*50)
                    print("Don't Try Negative Amount for Withdraw.")
                except InsufficientBalanceError:
                    print("-"*50)
                    print("You Don't have Sufficient Balance in Your Account")
            elif (ch==4):
                balenq()
                break
            elif (ch==5):
                disp()
                break
            elif (ch==6):
                closeAcc()
                break
            elif (ch==7):
                print("-"*50)
                print("You are exited from this program Successfully.....")
                print("\tT H A N K Y O U ! ! !")
                print("-"*50)
                exit()
            else:
                print("-"*50)
                print("\tPlease Choose Correct Option")
                print("-"*50)
        except ValueError:
            print("-"*50)
            print("Don't Use strings / special symbols / space \nor any other invalid Literals...Try again")
demo()
