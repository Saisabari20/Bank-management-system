class Account:
    account_number = 0
    name = ''
    amount = 0

    def createAccount(self):
        self.account_number = int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.amount = int(input("Enter The Initial amount(>=500):"))

    def showAccount(self):
        print("Account Number : ", self.account_number)
        print("Account Holder Name : ", self.name)
        print("Balance : ", self.amount)

    def modifyAccount(self):
        print("Account Number : ", self.account_number)
        self.name = input("Modify Account Holder Name :")
        self.amount = int(input("Modify Balance :"))

    def depositAmount(self, amount):
        self.amount += amount

    def withdrawAmount(self, amount):
        self.amount -= amount


def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")

    input("Press Enter To Contiune: ")


def writeAccount(account_list):
    account = Account()
    account.createAccount()
    for existing_account in account_list:
        if existing_account.account_number == account.account_number:
            print("Account number already exists. Please choose a different account number.")
            return
    account_list.append(account)


def displayAll(account_list):
    if len(account_list) > 0:
        for account in account_list:
            account.showAccount()
    else:
        print("No records to display")


def displaySp(account_list, num):
    found = False
    for account in account_list:
        if account.account_number == num:
            print("Your account Balance is = ", account.amount)
            found = True
            break
    if not found:
        print("No existing record with this number")


def depositAndWithdraw(account_list, num1, num2):
    found = False
    for account in account_list:
        if account.account_number == num1:
            found = True
            if num2 == 1:
                amount = int(input("Enter the amount to deposit : "))
                account.depositAmount(amount)
                print("Your account is updated")
            elif num2 == 2:
                amount = int(input("Enter the amount to withdraw : "))
                if amount <= account.amount:
                    account.withdrawAmount(amount)
                else:
                    print("You cannot withdraw a larger amount")
            break
    if not found:
        print("No existing record with this account number")


def deleteAccount(account_list, num):
    account_list[:] = [account for account in account_list if account.account_number != num]
    print("Your account is Deleted")


def modifyAccount(account_list, num):
    for account in account_list:
        if account.account_number == num:
            account.modifyAccount()
        else:
            print("No existing record with this account number")


# start of the program
ch = ''
num = 0
intro()
account_list = []

while ch != '8':
    print("\tMAIN MENU")
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
    if ch == '1':
        writeAccount(account_list)
    elif ch == '2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(account_list, num, 1)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(account_list, num, 2)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        displaySp(account_list, num)
    elif ch == '5':
        displayAll(account_list)
    elif ch == '6':
        num = int(input("\tEnter The account No. : "))
        deleteAccount(account_list, num)
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        modifyAccount(account_list, num)
    elif ch == '8':
        print("\tThanks for using bank management system")
        break
    else:
        print("Invalid choice")