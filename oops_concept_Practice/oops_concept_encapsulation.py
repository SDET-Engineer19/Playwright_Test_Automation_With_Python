class Atm:

    def __init__(self):

        self.__pin = " "
        self.__balance = 0

        self.menu()

    def menu(self):

        user_input = input("""
                                    Hello, how would you like to proceed?
                                     1. Enter 1 to create pin
                                     2. Enter 2 to deposit
                                     3. Enter 3 to withdraw
                                     4. Enter 4 to check balance
                                     5. Enter 5 to exit
 """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            self.exit()

    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("Pin Set Successfully")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            self.__balance = self.__balance + amount
            print("Deposit Successfully")
        else:
            print("Invalid Pin")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter your amount: "))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("Operation Successful")
            else:
                print("Insufficient Funds")
        else:
            print("Invalid Pin")

    def check_balance(self):
        temp = input("Enter your Pin: ")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid Pin")

    def exit(self):
        print("please take your card")


sbi = Atm()
sbi.__balance = "@(#(#(#)@"  # here __ ( Double Underscore Acts as a Private Access Modifier, we can do it for
# methods also . Adding String value to the integer variable )
sbi.deposit()
sbi.check_balance()
