# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Python Banking Program

def return_balance():
    print(f"Your balance is the following: ${balance}")

def deposit():
    amount=int(input("Enter an amount to be deposited: "))
    if amount<0:
        print("That is not a valid amount")
        return 0
    else:
        return amount
def withdrawal():
    amount=float(input("Enter the amount to be withdrawn: "))
    if amount>balance:
        print("The funds are not sufficient: ")
        return 0
    elif amount<0:
        print("amount must be greater than zero")
        return 0
    else:
        return amount


balance=0
is_running=True

while is_running:
    print("Banking program")
    print("1:Show Balance")
    print("2: Deposit")
    print("3:Withdrawal")
    print("4:Exit")

    choice=input("Enter your choice (1-4): ")
    if choice=='1':
        return_balance()
    elif choice=='2':
        balance+=deposit()
    elif choice=='3':
        balance-=withdrawal()
    elif choice=='4':
        is_running=False
    else:

        print("That is not a valid choice.")

print("Thank you have a nice day")



