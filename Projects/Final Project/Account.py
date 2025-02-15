import random

class Account:
    def __init__(self):
        # account number set using method
        self.acctNum = self.randomAcctNum()
        # variables for first and last name set up blank
        self.firstName = None
        self.lastName = None
        # blank variable for ssn
        self.socialSN = None
        # pin set using method
        self.PIN = self.randomPIN()
        # balance starting at 0
        self.balance = 0
    
    '''
    The below methods are the getters and setters for each function for
    the attributes I will want to set up
    '''
    # method to get account number
    def getAcctNum(self):
        return self.acctNum

    # method to set the account number
    def setAcctNum(self):
        self.acctNum = self.randomAcctNum()

    # method to get the first name of the account owner    
    def getFirstName(self):
        return self.firstName

    # method to set the first name of the account owner
    def setFirstName(self, new_firstName):
        self.firstName = new_firstName

    # method to get the last name of the account owner
    def getLastName(self):
        return self.lastName

    # method to set the last name of the account owner
    def setLastName(self, new_lastName):
        self.lastName = new_lastName

    # method to get the social security number
    def getSocialSN(self):
        return self.socialSN

    # method to set social security number and make sure it's 9 digits
    def setSocialSN(self):
        while True:
            ssn = input("Enter Account Owner's SSN (9 digits): ")
            if len(ssn) == 9:
                self.socialSN = ssn
                break
            else:
                print("SSN must be 9 digits")

    # method to get the account owner PIN
    def getPIN(self):
        return self.PIN

    # method to set the account owner PIN
    def setPIN(self):
        self.PIN = self.randomPIN()

    # method to get the account balance
    def getBalance(self):
        return self.balance

    # method to set the account balance
    def setBalance(self, balance):
        self.balance = balance
    
    '''
    This method is used to deposit an amount of money from the user into
    the account. It will then add that to the balance and show new balance
    '''
    def deposit(self, amount):
        self.balance += amount
        print(f"New Balance: ${self.balance}")
        return self.balance
    
    '''
    This method is used to withdraw an amount of money from the user from
    the account. It will make sure that the money is actually in the account
    and will let them know if not. Then it will remove from balance and show
    '''  
    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            print("Insufficient funds")
            return False
        else:
            self.balance -= amount
            print(f"New Balance: ${self.balance}")
            return True
            
    
    '''
    This method will be used to check if the pin entered by the user is valid
    by comparing it the one stored on the account; returning True or False
    '''
    def isValidPIN(self, pin):
        if self.PIN == pin:
            return True
        else:
            return False
    
    
    '''
    This method is meant to print out information to the user about their
    account. It uses f strings to insert correct materials
    '''
    def toString(self):
        info = ["===============================================",
                f"Account Number: {self.acctNum}",

                f"Owner First Name: {self.firstName}",

                f"Owner Last Name: {self.lastName}",

                f"Owner SSN: {self.socialSN}",

                f"PIN: {self.PIN}",

                f"Balance: ${self.balance}",

                "==============================================="]
        show = ""
        for i in info:
            show += i + "\n"
        return show

    # method to create a random account number
    def randomAcctNum(self):
        num = random.randint(10000000, 99999999)
        return num

    # method to create a random PIN
    def randomPIN(self):
        num = random.randint(1000, 9999)
        return str(num)

    # method for user to change PIN
    def changePIN(self):
        while True:
            userPIN = str(input("Enter new PIN: "))
            if len(userPIN) != 4:
                print("PIN must be 4 digits, try again.")

            else:
                checkPIN = str(input("Enter new PIN again to confirm: "))
                if checkPIN == userPIN:
                    self.PIN = userPIN
                    print("PIN has been updated")
                    break
                else:
                    print("PINs do not match, try again.")

    # method created for ATM withdrawal
    def ATM(self, amount):
        def getAmount(entry):
            atm = {}
            entries = ("Twenties", 20), ("Tens", 10), ("Fives", 5)
            for bill, cash in entries:
                atm[bill] = entry // cash
                entry %= cash
            print(f"Returning {int(atm['Twenties'])} 20s")
            print(f"Returning {int(atm['Tens'])} 10s")
            print(f"Returning {int(atm['Fives'])} 5s")
            return atm

        if amount < 5 or amount > 1000 or (amount % 5) != 0:
            print("Invalid, please enter a multiple of 5 that is less than 1000.")

        else:
            total = getAmount(amount)
            self.withdraw(amount)
        
