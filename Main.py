CORRECT_PIN = 1128
attempts = 3

# -------------------- LOGIN SECTION -------------------- #
while attempts > 0:
    PIN = int(input("Enter your ATM PIN: "))

    if PIN == CORRECT_PIN:
        print("Login Successful!")
        break
    else:
        attempts -= 1
        print("Wrong PIN")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Account has been blocked due to frequent wrong PIN attempts!")

# -------------------- MENU SECTION -------------------- #
if attempts > 0:
    run = 1
    Balance = 100000  

    while run == 1:
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Current Balance:", Balance)

        elif choice == 2:
            print("DEPOSIT")
            DEPOSIT = int(input("Enter amount to deposit: "))

            if DEPOSIT > 0:
                Balance = Balance + DEPOSIT
                print("Deposit Successful!")
                print("Current Balance:", Balance)
            else:
                print("Invalid deposit amount")

        elif choice == 3:
            print("WITHDRAW")
            WITHDRAWL = int(input("Enter withdrawing amount: "))

            if WITHDRAWL > 0 and WITHDRAWL <= Balance:
                Balance = Balance - WITHDRAWL
                print("Please collect your cash")
                print("Remaining Balance:", Balance)
            else:
                print("Insufficient balance or invalid amount")

        elif choice == 4:
            print("Thank you for using ATM")
            run = 0

        else:
            print("Invalid choice! Please try again.")
