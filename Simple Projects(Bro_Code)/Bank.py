#banking

def show_balance(balance):
    print(f"Your Balance: ${balance:.2f} ")

def deposit(balance):
    amount=float(input("Enter the amount: "))
    if amount <= 0:
        print("Deposit amount should be greater than 0")
        return 0
    else:
        return amount

def withdraw(balance):
    amount=float(input("Enter the withdraw amount: "))

    if amount > balance:
        print("Insufficient Balance!")
        print(f"Your balance is ${balance:.2f}")
        return 0
    elif amount<=0:
        print("Withdraw should be greater than 0")
        return 0
    else:
        return amount

def main():
    balance=0
    is_running=True


    while is_running:
        print()
        print("*** BANKING PROJECT ***")
        print("     1. Check Balance")
        print("     2. Deposit")
        print("     3. Withdraw")
        print("     4. Exit")
        print("***********************")
        choice = input(print("Enter your Choice: "))
        print("***********************")

        if choice == '1':
            print("***********************")
            show_balance(balance)
            print("***********************")

        elif choice == '2':
            balance+=deposit(balance)
            print("***********************")

        elif choice == '3':
            balance-=withdraw(balance)
            print("***********************")

        elif choice == '4':
            is_running=False
        else:
            print("Invalid! Please Try Later...")

    print("      Thank You!!      ")
    print("***********************")

if __name__ == "__main__":
    main()