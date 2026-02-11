import error_handling


class Bank_account:
    def __init__(self,initialAmount,AccountNumber):
        self.balance = initialAmount
        self.AccountNumber = AccountNumber
        print(f"Account {self.AccountNumber} created with balance ${self.balance:.2f}")
    

    def get_balance(self):
        
        print(f"Your Account {self.AccountNumber} Has a balance of ${self.balance:.2f}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} to Account {self.AccountNumber}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds in Account {self.AccountNumber}. Withdrawal amount: ${amount:.2f}, Available balance: ${self.balance:.2f}")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from Account {self.AccountNumber}. New balance: ${self.balance:.2f}")           
                 

    def viableTranstraction(self,amount):
        if amount > self.balance:
            raise error_handling.BalanceException(f"Insufficient funds in Account {self.AccountNumber}. Transaction amount: ${amount:.2f}, Available balance: ${self.balance:.2f}")
        elif amount <= 0:
            raise error_handling.BalanceException("Transaction amount must be positive.")
        else:
            print(f"Transaction of ${amount:.2f} is viable for Account {self.AccountNumber}.")


    def withdraw(self,amount):
        try:
            self.viableTranstraction(amount)
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from Account {self.AccountNumber}. New balance: ${self.balance:.2f}")
            self.get_balance()
        except error_handling.BalanceException as e:
            print(f"withdrawal failed: {e}")              

    def transfer(self, amount, target_account):
        try:
            print("*" * 20)
            print("Initiating transfer...")
            self.viableTranstraction(amount)
            self.withdraw(amount)
            target_account.deposit(amount)      
            print(f"Transferred ${amount:.2f} from Account {self.AccountNumber} to Account {target_account.AccountNumber}.")    

            print("transfer successful !")
            print("*" * 20)
        except error_handling.BalanceException as e:
            print(f"Transfer failed: {e}")

    def InterestReward(self):

        interest_rate = 0.05
        interest = self.balance * interest_rate
        self.balance += interest
        print(f"Interest of ${interest:.2f} added to Account {self.AccountNumber}. New balance: ${self.balance:.2f}")
        self.get_balance()
        