
# importing all of the files needed to use other classes

from Account import Account
from Bank import Bank
from BankUtility import BankUtility
from CoinCollector import CoinCollector

# calling BankUtility class on an object to use the methods
BU = BankUtility()

'''
On the BankManager class I am creating a class object for the menu that will keep
printing out to be displayed for the user. The constructor will have no parameters
and there will only be a main method as well as one to ask the user for the
account number and pin
'''
class BankManager:
    menu = '''
        ========================================================

        What do you want to do?

        1. Open an account

        2. Get account information and balance

        3. Change PIN

        4. Deposit money in account

        5. Transfer money between accounts

        6. Withdraw money from account

        7. ATM withdrawal

        8. Deposit change

        9. Close an account

        10. Add monthly interest to all accounts

        11. End Program

        ========================================================

        '''
    
    def __init__(self):
        pass

    '''
    This method is meant for prompting the user to enter their account number
    and their pin. It will check to see if the account is in the bank array, then
    if so it will make sure that the pin the user entered matches up with the
    pin associated with the account that it pulls from the array. It will also
    let the user know if the account entered is not found/ pin is invalid
    '''    
    def promptForAccountNumberAndPIN(self, Bank):
        accNum = int(input("Please enter your account number: "))
        userPIN = str(input("Please enter your PIN: "))

        if Bank.findAccount(accNum) != None:
            acct = Bank.findAccount(accNum)
            if acct.getPIN() == userPIN:
                return acct
            else:
                print("Invalid PIN")
        else:
            print(f"Account was not found for {accNum}")
            return None
        
    '''
    The main method is where everything will tie together. This is where the program
    will keep looping through and displaying the menu of options for the user. Depending
    on what the user enters, it will call the correct method for what it is the user wants.
    If the user input is not valid it will let them know and tell them to try again
    '''
    def main(self):
        # instantiating a bank object as well as one for bankmanager
        bank = Bank()
        selection = BankManager()
        # keeps displaying the menu to user
        while True:
            print(selection.menu)

            try:
                option = int(input("Choose what transaction you want: "))
                # makes sure user enters the right selection
                if option < 1 or option > 11:
                    raise ValueError
                
                # this method is meant to create an account; instantiates object and then calls setters
                if option == 1:
                    newAcct = Account()
                    firstName = BU.promptUserForString("Enter Account Owner's First Name: ")
                    lastName = BU.promptUserForString("Enter Account Owner's Last Name: ")
                    newAcct.setSocialSN()
                    newAcct.setFirstName(firstName)
                    newAcct.setLastName(lastName)
                    print(newAcct.toString())
                    bank.addAccountToBank(newAcct)
           
                # this method looks for an account then displays the info to user    
                elif option == 2:
                    acct = self.promptForAccountNumberAndPIN(bank)
                    if acct != None:
                        print(acct.toString())
                    else:
                        print("Invalid option, choose another transaction.")

                # this method allows the user to change their pin if entered correctly
                elif option == 3:
                    acct = self.promptForAccountNumberAndPIN(bank)
                    if acct != None:
                        acct.changePIN()
                    else:
                        print("Invalid option, choose another transaction.")

                # this method allows the user to deposit money into an account
                elif option == 4:
                    acct = self.promptForAccountNumberAndPIN(bank)
                    if acct != None:
                        depoAMT = BU.promptUserForPositiveNumber("Enter amount to deposit in dollars and cents (e.g. 2.57): ")
                        acct.deposit(depoAMT)
                    else:
                        print("Invalid option, choose another transaction.")

                # this method allows the user to transfer money between accounts
                elif option == 5:
                    print("Account to transfer from: ")
                    acct = self.promptForAccountNumberAndPIN(bank)
                    print("Account to transfer to: ")
                    acct2 = self.promptForAccountNumberAndPIN(bank)
                    
                    if acct != None and acct2 != None:
                        transferAMT = BU.promptUserForPositiveNumber("Enter amount to transfer in dollars and cents (e.g. 2.57): ")

                        if acct.withdraw(transferAMT):
                            acct2.deposit(transferAMT)
                            print("Transfer complete")
                    else:
                        print("Invalid option, choose another transaction.")

                # this method allows the user to withdraw money from an account
                elif option == 6:
                    acct = self.promptForAccountNumberAndPIN(bank)
                    if acct != None:
                        witAMT = BU.promptUserForPositiveNumber("Enter amount to withdraw in dollars and cents (e.g. 2.57): ")
                        acct.withdraw(witAMT)
                    else:
                        print("Invalid option, choose another transaction.")

                # this method will allow the user to perform ATM style withdrawal
                elif option == 7:
                    acct = self.promptForAccountNumberAndPIN(bank)
                    if acct != None:
                        withdrawal = BU.promptUserForPositiveNumber("Enter amount to withdraw in dollars (no cents) in multiples of 5 (limit $1000): ")
                        acct.ATM(withdrawal)
                    else:
                        print("Invalid option, choose another transaction.")

                # this method allows the user to deposit change into their account
                elif option == 8:
                    acct = self.promptForAccountNumberAndPIN(bank)
                    if acct != None:
                        print("P = penny, N = nickel, D = dime, Q = quarter, H = half-dollar, W = whole dollar")
                        change = BU.promptUserForString("Using the key above, please deposit coins: ")
                        collector = CoinCollector()
                        collector.parseChange(change)
                        acct.deposit(collector.totalChange)
                    else:
                        print("Invalid option, choose another transaction.")

                # this method allows the user to close their account
                elif option == 9:
                    acct = self.promptForAccountNumberAndPIN(bank)
                    if acct != None:
                        bank.removeAccountFromBank(acct)
                    else:
                        print("Invalid option, choose another transaction.")

                # this method adds monthly interest to all of the accounts in the array
                elif option == 10:
                    intRate = BU.promptUserForPositiveNumber("Enter annual interest rate percentage (e.g. 2.75 for 2.75%): ")
                    bank.addMonthlyInterest(intRate)

                # this method lets the user leave the program
                elif option == 11:
                    break
                    
            except ValueError:
                print("Invalid input. Please try again")

