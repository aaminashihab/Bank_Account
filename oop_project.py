from bank_account import *
# Create two bank accounts
account1 = Bank_account(1000, "123456")
account2 = Bank_account(500, "654321")
# Display initial balances
account1.get_balance()
account2.get_balance()
# Perform some transactions
account1.deposit(200)
account1.withdraw(150)
account1.withdraw(2000)  # This should trigger an error
account1.withdraw(-50)   # This should also trigger an error
account1.transfer(300, account2)  # This should be successful
account1.transfer(2000, account2)  # This should trigger an error
account1.transfer(-100, account2)  # This should also trigger an error
