#Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality. 
class BankAccount:
    def __init__(self, ac_no, ac_holder, initial_bal=0.0):
        self.__ac_no = ac_no
        self.__ac_holder = ac_holder
        self.__ac_bal = initial_bal

    def deposit(self, amt):
        if amt > 0:
            self.__ac_bal += amt
            print("Deposited Rs.{}. New Balance: Rs.{}".format(amt, self.__ac_bal))
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amt):
        if amt > 0 and amt <= self.__ac_bal:
            self.__ac_bal -= amt
            print("Withdrew Rs.{}. New Balance: Rs.{}".format(amt, self.__ac_bal))
        else:
            print("Invalid withdrawal amount!")

    def balance(self):
        print("Account balance for {} (Account #{}): Rs.{}".format(
            self.__ac_holder, self.__ac_no, self.__ac_bal))

ac = BankAccount(ac_no="102030405", ac_holder="Nithyashree", initial_bal=5000.0)

ac.balance()
ac.deposit(500.0)
ac.withdraw(200.0)
ac.balance()
