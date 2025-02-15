
import unittest
from Account import Account
from Bank import Bank
from BankUtility import BankUtility
from CoinCollector import CoinCollector

class BankTest(unittest.TestCase):
    '''
    The next 3 methods are to test the CoinCollector class
    and make sure the parseChange method works correctly
    '''
    # making sure this equals 27 cents
    def testCoinCollector(self):
        change = "PPDND"
        collector = CoinCollector()
        collector.parseChange(change)
        self.assertEqual(collector.totalChange, .27)
        
    # making sure this equals 1 dollar 66 cents
    def testCoinCollector2(self):
        change = "pNqDHJnPW"
        collector = CoinCollector()
        collector.parseChange(change)
        self.assertEqual(collector.totalChange, 1.66)

    # making sure this equals 0 dollars/cents
    def testCoinCollector3(self):
        change = "ZerumOI"
        collector = CoinCollector()
        collector.parseChange(change)
        self.assertEqual(collector.totalChange, 0)

    '''
    The next 6 methods are to test the Account class
    and make sure the deposit, withdraw, and isValidPIN
    methods are working correctly
    '''
    # creating account and making sure the deposit works
    def testDeposit(self):
        account = Account()
        bank = Bank()
        firstName = "Monkey D"
        lastName = "Luffy"
        account.socialSN = 123456789
        account.setFirstName(firstName)
        account.setLastName(lastName)
        bank.addAccountToBank(account)
        amount = 100
        account.deposit(amount)
        self.assertEqual(account.balance, 100)

    # creating account and making sure the deposit works
    def testDeposit2(self):
        account = Account()
        bank = Bank()
        firstName = "Monkey D"
        lastName = "Luffy"
        account.socialSN = 123456789
        account.setFirstName(firstName)
        account.setLastName(lastName)
        bank.addAccountToBank(account)
        amount = 50.25
        account.deposit(amount)
        self.assertEqual(account.balance, 50.25)

    # creating account and making sure the withdraw works
    def testWithdraw(self):
        account = Account()
        bank = Bank()
        firstName = "Roronoa"
        lastName = "Zoro"
        account.socialSN = 123456789
        account.setFirstName(firstName)
        account.setLastName(lastName)
        bank.addAccountToBank(account)
        amount = 100
        account.deposit(amount)
        account.withdraw(20)
        self.assertEqual(account.balance, 80)

    # creating account and making sure the withdraw works
    def testWithdraw2(self):
        account = Account()
        bank = Bank()
        firstName = "Roronoa"
        lastName = "Zoro"
        account.socialSN = 123456789
        account.setFirstName(firstName)
        account.setLastName(lastName)
        bank.addAccountToBank(account)
        amount = 100.75
        account.deposit(amount)
        account.withdraw(20.50)
        self.assertEqual(account.balance, 80.25)

    # creating account and making sure pin validity works
    def testValidPIN(self):
        account = Account()
        bank = Bank()
        firstName = "Vinsmoke"
        lastName = "Sanji"
        account.socialSN = 123456789
        account.setFirstName(firstName)
        account.setLastName(lastName)
        account.PIN = 1234
        bank.addAccountToBank(account)
        self.assertEqual(account.PIN, 1234)

    # creating account and making sure pin validity works
    def testValidPIN2(self):
        account = Account()
        bank = Bank()
        firstName = "Vinsmoke"
        lastName = "Sanji"
        account.socialSN = 123456789
        account.setFirstName(firstName)
        account.setLastName(lastName)
        account.PIN = 9876
        bank.addAccountToBank(account)
        self.assertEqual(account.PIN, 9876)

    '''
    The next 8 methods are to test the Bank class and make
    sure the addAccountToBank, removeAccountFromBank, findAccount,
    and addMonthlyInterest methods are working correctly
    '''
    # creating account and making sure it gets added to the array
    def testAddAccountToBank(self):
        account = Account()
        bank = Bank()
        firstName = "Trafalgar D"
        lastName = "Water Law"
        account.socialSN = 123456789
        account.setFirstName(firstName)
        account.setLastName(lastName)
        account.PIN = 1234
        bank.addAccountToBank(account)
        self.assertEqual(len(bank.accts), 1)

    # creating account and making sure it gets added to the array
    def testAddAccountToBank2(self):
        account = Account()
        bank = Bank()
        firstName = "Trafalgar D"
        lastName = "Water Law"
        account.socialSN = 123456789
        account.setFirstName(firstName)
        account.setLastName(lastName)
        account.PIN = 1234
        bank.addAccountToBank(account)
        account2 = Account()
        firstName2 = "Trafalgar D"
        lastName2 = "Water Law"
        account2.socialSN = 123456789
        account2.setFirstName(firstName2)
        account2.setLastName(lastName2)
        account2.PIN = 1234
        bank.addAccountToBank(account2)
        self.assertEqual(len(bank.accts), 2)

    # creating account and making sure it gets removed from the array
    def testRemoveAccountFromBank(self):
        account = Account()
        bank = Bank()
        firstName = "Portgas D"
        lastName = "Ace"
        account.socialSN = 123456789
        account.setFirstName(firstName)
        account.setLastName(lastName)
        account.PIN = 1234
        bank.addAccountToBank(account)
        bank.removeAccountFromBank(account)
        self.assertEqual(len(bank.accts), 0)

    # creating account and making sure it gets removed from the array
    def testRemoveAccountFromBank2(self):
        account = Account()
        bank = Bank()
        firstName = "Portgas D"
        lastName = "Ace"
        account.socialSN = 123456789
        account.setFirstName(firstName)
        account.setLastName(lastName)
        account.PIN = 1234
        bank.addAccountToBank(account)
        account2 = Account()
        firstName2 = "Portgas D"
        lastName2 = "Ace"
        account2.socialSN = 123456789
        account2.setFirstName(firstName2)
        account2.setLastName(lastName2)
        account2.PIN = 1234
        bank.addAccountToBank(account2)
        bank.removeAccountFromBank(account)
        self.assertEqual(len(bank.accts), 1)

    # creating account to add to array and making sure it can be found
    def findAccount(self):
        account = Account()
        bank = Bank()
        firstName = "Flame Emperor"
        lastName = "Sabo"
        account.socialSN = 123456789
        account.setFirstName(firstName)
        account.setLastName(lastName)
        account.PIN = 1234
        bank.addAccountToBank(account)
        bank.findAccount(account.acctNum)
        self.assertEqual(account, type(Account()))

    # creating account to add to array and making sure it can be found
    def findAccount2(self):
        account = Account()
        bank = Bank()
        firstName = "Dragon Claw"
        lastName = "Sabo"
        account.socialSN = 987654321
        account.setFirstName(firstName)
        account.setLastName(lastName)
        account.PIN = 9876
        bank.addAccountToBank(account)
        bank.findAccount(account.acctNum)
        self.assertEqual(account, type(Account()))

    # creating account and making sure the right interest is applied
    def testAddMonthlyInterest(self):
        account = Account()
        bank = Bank()
        firstName = "Red Haired"
        lastName = "Shanks"
        account.socialSN = 123456789
        account.setFirstName(firstName)
        account.setLastName(lastName)
        account.PIN = 1234
        bank.addAccountToBank(account)
        amount = 100
        account.deposit(amount)
        bank.addMonthlyInterest(5.5)
        self.assertEqual(account.balance, 100.46)

    # creating account and making sure the right interest is applied
    def testAddMonthlyInterest2(self):
        account = Account()
        bank = Bank()
        firstName = "Red Haired"
        lastName = "Shanks"
        account.socialSN = 123456789
        account.setFirstName(firstName)
        account.setLastName(lastName)
        account.PIN = 1234
        bank.addAccountToBank(account)
        amount = 100
        account.deposit(amount)
        bank.addMonthlyInterest(3.5)
        self.assertEqual(account.balance, 100.29)

    '''
    The next 6 methods are to test the BankUtility class and
    make sure the isNumeric, convertFromDollarsToCents and
    generateRandomInteger methods are working correctly
    '''
    # checks to see if an input is actually a number (int)
    def testIsNumeric(self):
        BU = BankUtility()
        self.assertEqual(BU.isNumeric("5"), True)

    # checks to see if an input is actually a number (int)
    def testIsNumeric2(self):
        BU = BankUtility()
        self.assertEqual(BU.isNumeric("a"), False)

    # checks to see if a float is converted to int (e.g. $2.57 -> 257 cents)
    def testConvertFromDollarsToCents(self):
        BU = BankUtility()
        amount = BU.convertFromDollarsToCents(3.25)
        self.assertEqual(amount, 325)

    # checks to see if a float is converted to int (e.g. $2.57 -> 257 cents)
    def testConvertFromDollarsToCents2(self):
        BU = BankUtility()
        amount = BU.convertFromDollarsToCents(.73)
        self.assertEqual(amount, 73)

    # checks to see if random int is generated correctly
    def testGenerateRandomInteger(self):
        BU = BankUtility()
        n = BU.generateRandomInteger(1, 10)
        self.assertTrue(1 <= n <=10)

    # checks to see if random int is generated correctly
    def testGenerateRandomInteger2(self):
        BU = BankUtility()
        n = BU.generateRandomInteger(250, 3000)
        self.assertTrue(250 <= n <= 3000)


if __name__ == "__main__":
    unittest.main()
