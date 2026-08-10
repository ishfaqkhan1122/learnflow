# 🏧 ATM Machine — Python Beginner Project

```python
# ==========================================
#          ATM MACHINE PROJECT
#          Project #6
# ==========================================

# Account information
correct_pin = "1234"
balance = 50000

# -------------------------------
# PIN LOGIN
# -------------------------------

print("================================")
print("       WELCOME TO ATM")
print("================================")

attempts = 3

while attempts > 0:

    pin = input("Enter your 4-digit PIN: ")

    if pin == correct_pin:
        print("\nLogin Successful!")
        break
    else:
        attempts -= 1
        print("Incorrect PIN!")
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("\nYour account is locked.")
else:

    # -------------------------------
    # ATM MENU
    # -------------------------------

    while True:

        print("\n================================")
        print("          ATM MENU")
        print("================================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        # -------------------------------
        # CHECK BALANCE
        # -------------------------------

        if choice == "1":

            print("\nYour current balance is:", balance, "PKR")

        # -------------------------------
        # DEPOSIT MONEY
        # -------------------------------

        elif choice == "2":

            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                balance += amount

                print("\nDeposit successful!")
                print("Deposited:", amount, "PKR")
                print("New balance:", balance, "PKR")

            else:
                print("\nInvalid amount!")

        # -------------------------------
        # WITHDRAW MONEY
        # -------------------------------

        elif choice == "3":

            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("\nInvalid amount!")

            elif amount > balance:
                print("\nInsufficient balance!")

            else:
                balance -= amount

                print("\nWithdrawal successful!")
                print("Withdrawn:", amount, "PKR")
                print("Remaining balance:", balance, "PKR")

        # -------------------------------
        # CHANGE PIN
        # -------------------------------

        elif choice == "4":

            old_pin = input("Enter your current PIN: ")

            if old_pin == correct_pin:

                new_pin = input("Enter your new 4-digit PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():

                    correct_pin = new_pin

                    print("\nPIN changed successfully!")

                else:
                    print("\nPIN must contain exactly 4 digits.")

            else:
                print("\nIncorrect current PIN!")

        # -------------------------------
        # EXIT
        # -------------------------------

        elif choice == "5":

            print("\nThank you for using our ATM!")
            print("Have a nice day!")
            break

        # -------------------------------
        # INVALID CHOICE
        # -------------------------------

        else:

            print("\nInvalid choice!")
            print("Please select a number from 1 to 5.")
```

### 🔑 Test Details

```text
PIN: 1234
Initial Balance: 50,000 PKR
```

### Example

```text
================================
       WELCOME TO ATM
================================
Enter your 4-digit PIN: 1234

Login Successful!

================================
          ATM MENU
================================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Change PIN
5. Exit

Enter your choice: 3

Enter amount to withdraw: 5000

Withdrawal successful!
Withdrawn: 5000 PKR
Remaining balance: 45000 PKR
```

### 🧠 Python concepts used

```text
Variables
input()
print()
if / elif / else
while loop
break
float()
len()
isdigit()
Arithmetic operators
```

This is a good **Project #6** because it combines several basic Python concepts into one practical program.
