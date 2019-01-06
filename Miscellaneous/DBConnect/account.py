class Account:

    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())

    def withdraw(self,amount):
        self.balance=self.balance - amount


    def deposit(self,amount):
        self.balance=self.balance+amount


    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))



# 1) Simple Test
# account=Account("balance.txt")
# print(account.balance)
# account.withdraw(100)
# print(account.balance)
# account.deposit(200)
# print(account.balance)
# account.commit()


# 2) Creating subclass
class Checking(Account):
    """"" Generates CHecking account"""""
    type="checking"   ## Class Variable
    def __init__(self,filepath,fee):     ## Constructor
        Account.__init__(self,filepath)
        self.fee=fee


    def transfer(self,amount):   ##  Class Method
        self.balance=self.balance - amount - self.fee


# checking = Checking("balance.txt",1)
# checking.deposit(100)
# print(checking.balance)
# checking.transfer(50)
# print(checking.balance)
# checking.commit()

jack_checking = Checking("jackBalance.txt",1)
jack_checking.deposit(100)
print(jack_checking.balance)
jack_checking.transfer(50)
print(jack_checking.balance)
print(jack_checking.type)
print(jack_checking.__doc__)
jack_checking.commit()

