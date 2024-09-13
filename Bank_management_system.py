import sqlite3

# Connect to the database
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS accounts (
    account_number INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    amount INTEGER NOT NULL
)
''')
conn.commit()

class Account:
    def __init__(self):
        self.account_number = 0
        self.name = ''
        self.amount = 0

    def createAccount(self):
        try:
            self.account_number = int(input("Enter the account no (at least 7 digits): "))
            if len(str(self.account_number)) < 7:
                raise ValueError("Account number must be at least 7 digits long.")
            self.name = input("Enter the account holder name: ")
            self.amount = int(input("Enter The Initial amount (>=500): "))

            # Ensure the amount is valid
            if self.amount < 500:
                raise ValueError("Initial amount should be 500 or more.")

            # Insert the new account into the database
            cursor.execute("INSERT INTO accounts (account_number, name, amount) VALUES (?, ?, ?)",
                           (self.account_number, self.name, self.amount))
            conn.commit()
            print("\n\nAccount created successfully!")
        except sqlite3.IntegrityError:
            print("Error: Account number already exists.")
        except ValueError as ve:
            print(f"Invalid input: {ve}")

    def showAccount(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.name}")
        print(f"Balance: {self.amount}")

    def modifyAccount(self):
        try:
            print(f"Account Number: {self.account_number}")
            old_name = self.name
            new_name = input("Modify Account Holder Name: ")

            # Check if the new name is different from the old name
            if new_name == old_name:
                raise ValueError("New name is the same as the old name. Please try a different name.")

            # Update the name in the database
            self.name = new_name
            cursor.execute("UPDATE accounts SET name = ? WHERE account_number = ?",
                           (self.name, self.account_number))
            conn.commit()
            print("Account updated successfully!")
        except ValueError as ve:
            print(ve)

    def depositAmount(self, amount):
        self.amount += amount

        # Update the balance in the database
        cursor.execute("UPDATE accounts SET amount = ? WHERE account_number = ?",
                       (self.amount, self.account_number))
        conn.commit()

    def withdrawAmount(self, amount):
        if amount <= self.amount:
            self.amount -= amount

            # Update the balance in the database
            cursor.execute("UPDATE accounts SET amount = ? WHERE account_number = ?",
                           (self.amount, self.account_number))
            conn.commit()
            print("Amount withdrawn successfully!")
        else:
            print("Error: Insufficient balance.")


def writeAccount():
    account = Account()
    account.createAccount()


def displayAll():
    cursor.execute("SELECT * FROM accounts")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"\n\nAccount Number: {row[0]}\nAccount Holder Name: {row[1]}\nBalance: {row[2]}")
    else:
        print("No records to display.")


def displaySp(num):
    cursor.execute("SELECT * FROM accounts WHERE account_number = ?", (num,))
    row = cursor.fetchone()
    if row:
        print(f"Your account Balance is = {row[2]}")
    else:
        print("No existing record with this number.")


def depositAndWithdraw(num1, num2):
    cursor.execute("SELECT * FROM accounts WHERE account_number = ?", (num1,))
    row = cursor.fetchone()
    if row:
        account = Account()
        account.account_number = row[0]
        account.name = row[1]
        account.amount = row[2]

        if num2 == 1:
            amount = int(input("Enter the amount to deposit: "))
            account.depositAmount(amount)
            print("Your account is updated.")
        elif num2 == 2:
            amount = int(input("Enter the amount to withdraw: "))
            account.withdrawAmount(amount)
    else:
        print("No existing record with this account number.")


def deleteAccount(num):
    cursor.execute("SELECT * FROM accounts WHERE account_number = ?", (num,))
    row = cursor.fetchone()
    if row:
        cursor.execute("DELETE FROM accounts WHERE account_number = ?", (num,))
        conn.commit()
        print("Your account has been deleted.")
    else:
        print("Error: Account does not exist.")


def modifyAccount(num):
    cursor.execute("SELECT * FROM accounts WHERE account_number = ?", (num,))
    row = cursor.fetchone()
    if row:
        account = Account()
        account.account_number = row[0]
        account.name = row[1]
        account.amount = row[2]
        account.modifyAccount()
    else:
        print("No existing record with this account number.")


def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")
    input("Press Enter to continue.")


# Start of the program
ch = ''
num = 0
intro()

while ch != '8':
    print("\t\n\nMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. CLOSE AN ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    ch = input("\n\nEnter your choice:")
    try:
        if ch == '1':
            writeAccount()
        elif ch == '2':
            num = int(input("\tEnter The account No: "))
            depositAndWithdraw(num, 1)
        elif ch == '3':
            num = int(input("\tEnter The account No: "))
            depositAndWithdraw(num, 2)
        elif ch == '4':
            num = int(input("\tEnter The account No: "))
            displaySp(num)
        elif ch == '5':
            displayAll()
        elif ch == '6':
            num = int(input("\tEnter The account No: "))
            deleteAccount(num)
        elif ch == '7':
            num = int(input("\tEnter The account No: "))
            modifyAccount(num)
        elif ch == '8':
            print("\tThanks for using the bank management system.")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Close the database connection and cursor when done
cursor.close()
conn.close()
