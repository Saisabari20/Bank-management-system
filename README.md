# Bank Management System

This is a simple Python-based Bank Management System that allows users to create accounts, deposit, withdraw, view account balances, and modify account information. The system uses SQLite as its database to store and manage account data.

## Features

- Create a new account with an initial deposit (minimum of 500 units).
- Deposit and withdraw money from an account.
- Check account balance.
- View all account holders.
- Modify account information.
- Delete an account.

## Requirements

- Python 3.6+
- SQLite (comes built-in with Python)

## Setup and Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Saisabari20/Bank-Management-System.git

## How to Use

1. **Create an Account**:
   - Enter a 7-digit account number, name, and an initial deposit (minimum of 500 units).
   
2. **Deposit**:
   - Enter your account number and the amount you want to deposit.

3. **Withdraw**:
   - Enter your account number and the amount you want to withdraw (only if your balance allows).

4. **Check Account Balance**:
   - Enter your account number to view the current balance.

5. **View All Accounts**:
   - See the list of all account holders.

6. **Modify Account**:
   - Update account 

## Database

The project uses an SQLite database named `bank.db` which stores the account details in the `accounts` table. The table schema includes:

- `account_number` (INTEGER, Primary Key)
- `name` (TEXT)
- `amount` (INTEGER)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.





