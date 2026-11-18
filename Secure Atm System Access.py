Created using basic Python concepts
balance = 50000
maximum_attempts = 3

attempts = 0
valid_card = False

while attempts < maximum_attempts:
    card_number = input("Enter your card number: ").strip()

    if card_number.isdigit():
        valid_card = True
        print("Card accepted")
        break
    else:
        attempts += 1
        print("Invalid card number")
        print("Attempts remaining:", maximum_attempts - attempts)

if valid_card:

    attempts = 0
    password_valid = False

    while attempts < maximum_attempts:
        password = input("Enter your 4-digit PIN: ").strip()

        has_digit = True

        if len(password) == 4:
            for character in password:
                if not character.isdigit():
                    has_digit = False
                    break

            if has_digit:
                password_valid = True
                print("PIN accepted")
                break

        attempts += 1
        print("Invalid PIN")
        print("Attempts remaining:", maximum_attempts - attempts)

    if password_valid:

        print("\nWelcome to your account")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")

        transaction = input("Select a transaction (1-3): ").strip()

        if transaction == "1":
            print("Your balance is:", balance)

        elif transaction == "2":
            withdrawal = int(input("Enter withdrawal amount: "))

            if withdrawal <= balance and withdrawal > 0:
                balance -= withdrawal
                print("Withdrawal successful")
                print("New balance:", balance)
            else:
                print("Invalid amount or insufficient funds")

        elif transaction == "3":
            deposit = int(input("Enter deposit amount: "))

            if deposit > 0:
                balance += deposit
                print("Deposit successful")
                print("New balance:", balance)
            else:
                print("Invalid deposit amount")

        else:
            print("Invalid transaction")

    else:
        print("Account locked: PIN attempts exhausted")

else:
    print("Account locked: Invalid card number")