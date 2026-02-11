

# 💳 Bank Account Management System (Python OOP)

## 📌 Overview

This project is a simple **Bank Account Management System** built using Python and Object-Oriented Programming concepts.

It demonstrates:

* Classes & Objects
* Encapsulation
* Custom Exception Handling
* Method Design
* Transaction Validation Logic

The system supports basic banking operations such as deposits, withdrawals, transfers, and interest rewards.

---

## 🚀 Features

* ✅ Create a Bank Account
* 💰 Deposit money
* 💸 Withdraw money (with validation)
* 🔁 Transfer money between accounts
* 📈 Add interest rewards
* ⚠ Custom exception handling for insufficient balance

---

## 🧠 Concepts Used

* Object-Oriented Programming (OOP)
* Custom Exception Classes
* Try & Except Blocks
* Method Reusability
* Transaction Validation Logic

---

## 🏗 Project Structure

```
├── bank_account.py
├── error_handling.py
└── README.md
```

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/bank-account-system.git
```

### 2️⃣ Navigate to project folder

```bash
cd bank-account-system
```

### 3️⃣ Run the program

```bash
python bank_account.py
```

---

## 🛠 Example Usage

```python
from bank_account import BankAccount

account1 = BankAccount(1000, 101)
account2 = BankAccount(500, 102)

account1.deposit(200)
account1.withdraw(300)
account1.transfer(400, account2)
account1.interestReward()
```

---

## ⚠️ Custom Exception

The project uses a custom `BalanceException` defined in `error_handling.py` to handle:

* Insufficient balance
* Invalid transaction amounts

Example:

```python
class BalanceException(Exception):
    pass
```

---

## 🎯 Learning Outcome

This project helps beginners understand:

* How real-world banking logic works in code
* How to structure validation logic
* How to use exception handling properly
* How to design cleaner and reusable methods

---

## 🔮 Future Improvements

* Add transaction history tracking
* Add savings and checking account types
* Convert into a CLI-based banking application
* Add persistent storage (SQLite / JSON)
* Add unit tests

---
