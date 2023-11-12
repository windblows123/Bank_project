class Customer:
    __slots__ = ('first_name', 'last_name', 'passport_number')
    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self,
                     first_name,
                     last_name,
                     passport_number):
        self.customers[passport_number] = Customer(
            first_name,
            last_name,
            passport_number)

    def get_customer(self, number):
        customer = self.customers.get(number)
        if customer == None:
            raise KeyError("Customer not found")
        return customer

    def add_account(self, account, customer):
        self.accounts[customer] = account

    def get_customer_account(self, passport_number):
        if passport_number not in self.customers:
            raise KeyError('Account not found')
        customer = self.customers[passport_number]
        return self.accounts[customer]

    def deposit(self, passport_number, amount):
        account = self.get_customer_account(passport_number)
        account.deposit(amount)

    def withdraw(self, passport_number, amount):
        account = self.get_customer_account(passport_number)
        account.withdraw(amount)


class BankAccount:
    def __init__(self, number, currency):
        self.number = number
        self.currency = currency
        self.amount = 0

    def deposit(self, sum_of_money):
        self.amount += sum_of_money

    def withdraw(self, sum_of_money):
        self.amount -= sum_of_money


