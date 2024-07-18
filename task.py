import time

print('Hello! Welcome to APU Bank.')
time.sleep(1)
print('This is Admin account.')
time.sleep(1)
print("Please Insert Your CARD")
time.sleep(5)
password = 1234

pin = int(input("Enter Your 4 Digit Pin: "))

Balance = 5000

if pin == password:
    choice = int(input('Enter 0 to proceed, 1 to terminate:'))
    while True:
        if(choice == 0):
            print("""
            1 == Balance
            2 == Withdraw Balance
            3 == Deposit Balance
            4 == Change pin
            5 == Transaction history
            6 == Exit
            """)
            
            option = int(input("Please Enter Your Choice: "))
            if option == 1: 
             print(f"Your Current Balance is {Balance}")
            
            elif option == 2:
             Withdraw_amount = int(input("Enter Youur withdraw_amunt: "))
             Balance = Balance - Withdraw_amount
             if Withdraw_amount <= Balance:
                print(f"{Withdraw_amount} is debited from your account")
                print(f"Your Updated Balance is {Balance}")
             else:
                Withdraw_amount != Balance
                print ("Cannot be done. You have insufficient amount.")
                
            elif option == 3:
             Deposit_amounteposit_amount = int(input("Enter Your Deposit Amount: "))
             Balance = Balance + Deposit_amounteposit_amount
             print(f"{Deposit_amounteposit_amount} is Credited to Your Account")
             print(f"Your Updated Balance is {Balance}") 
            
                    
            elif option == 4:
                old_pin = int(input("Enter Your Old Pin: "))
                if old_pin == password:
                    new_pin = int(input("Enter Your New Pin: "))
                    password = new_pin
                    print("Your Pin is Updated Successfully")
                else:
                    print("Enter a Valid Pin")
            
            elif option == 5:
             username = input('Enter username that you would like to view:')
             transactionfilename = username +'_transactionhistory.txt'
             transactionfile = open(transactionfilename,'a')
             with open (transactionfilename,'r') as f:
              f.seek(0)
              if f.read(1):
               print(f.read())
               break
              else:
                print('There is no transaction history for this customer')
                break
            elif option == 6:
                print("Good Bye")
                break
        elif (choice == 1):
            print("Thank You! ")
            break
else:
    print("Wrong PIN, Please Try Again! ")