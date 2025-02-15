
class Bank:

    '''
    Within the constructor it will initialize an empty array of bank accounts
    and it will also set a number of accounts the bank can support
    '''
    def __init__(self):
        self.accts = []
        self.limit = 100

    '''
    This method is meant to add bank accounts to the array. It will go through
    all of the accounts until it finds an empty spot, which is where the
    account will get added. Also, it makes sure there is no duplicate
    It will return true if the account is added successfully
    If there is no room it will let the user know and also return false
    '''
    def addAccountToBank(self, account):
        if len(self.accts) < self.limit:
            
            for spot in self.accts:
                if spot.acctNum == account.acctNum:
                    print("This account number is already in use.")
                    account.setAcctNum()
                    print(f"New account number is:{account.acctNum}")
            self.accts.append(account)
            return True

        else:
            print("There are no more account spots available.")
            return False
        
    '''
    This method is meant to remove bank accounts from an array. It will go
    through all of the accounts until it finds the given number, which then the
    account will be removed. It will also let the user know if the account
    is not there (item is not in array)
    '''
    def removeAccountFromBank(self, account):
        for x in self.accts:
            if x.acctNum == account.acctNum:
                self.accts.remove(account)
                print("Account has been found and removed.")
            else:
                print("This account number was not found.")

    '''
    This method is meant to search for an account number in the array. It will go
    through all of the accounts until it finds the given number, which then the
    account will be returned. It will also return null if the number is not found
    '''
    def findAccount(self, accountNumber):
        for i in self.accts:
            if i.getAcctNum() == accountNumber:
                return i
        else:
            return None
            
    '''
    This method is for going through the array of accounts and adding a monthly interest
    amount to it based on a percent that the user will enter
    '''    
    def addMonthlyInterest(self, percent):
        for i in self.accts:
            interest = (i.balance * (percent / 100)) / 12
            total = round((i.balance + interest), 2)
            i.setBalance(total)
            print(f"Deposited {round(interest, 2)} into {i.getAcctNum()}. New balance is {i.balance}")
