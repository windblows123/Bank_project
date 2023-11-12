from resourses import BankAccount, Bank, Customer

bank = Bank()
account1 = BankAccount('0000 0000 0000 0000', 'USD')
account2 = BankAccount('0000 0000 0000 0001', 'USD')
bank.add_customer('Tyler', 'Derden', '3519000000')
bank.add_customer('Jack', 'Palanic', '3519000001')
customer1 = bank.get_customer('3519000000')
customer2 = bank.get_customer('3519000001')
bank.add_account(account1, customer1)
bank.add_account(account2, customer2)
bank.deposit('3519000001', 100)
customer_account1 = bank.get_customer_account('3519000000')
customer_account2 = bank.get_customer_account('3519000001')

print(customer_account1.amount)
bank.deposit('3519000000', 100)
print(customer_account1.amount)
print(customer_account2.amount)