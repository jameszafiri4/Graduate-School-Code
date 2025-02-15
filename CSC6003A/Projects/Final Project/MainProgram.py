'''
This program is able to perform many different bank transactions for the user

These transactions can be performed on one or more accounts that the user creates

The program uses multiple classes that contain the methods needed to work properly

When ran, the menu will show the different transactions available for the user

'''

from BankManager import BankManager


if __name__ == "__main__":
    bank = BankManager().main()
