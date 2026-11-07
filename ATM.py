correct_pin = int(input("Create pin"))
balance = 1000.00

pin = int(input("Enter your PIN: "))

if pin == correct_pin:
    while True:
        print("\nPIN correct!")
        print("ATM Menu")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")

        choice = input("Choose an option (1, 2, 3 or 4): ")

        if choice == "1":
           print("Your balance is $", balance)

        elif choice == "2":
           amount = float(input("Enter the amount to deposit: "))
           balance = balance + amount
           print("Deposit successful!")
           print("Your new balance is $", balance)

        elif choice == "3":
           amount = float(input("Enter the amount to withdraw: "))

           if amount <= balance:
               balance = balance - amount
               print("Withdrawal successful!")
               print("Your new balance is $", balance)
           else:
               print("Insufficient funds.")
        elif choice =="4":
           print("Thank you for using the ATM. Goodbye!")
           break

        else:
          print("Invalid option. Please choose 1, 2, or 3.")
else:
 print("Incorrect PIN. Access denied.")
