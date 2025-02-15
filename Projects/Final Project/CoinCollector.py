
class CoinCollector:
    def __init__(self):
        self.totalChange = 0

    '''
    This method is meant to loop through a string and count the characters
    to store as coins, with each letter having a value
    '''
    def parseChange(self, coins):
        # setting change total equal to zero
        purse = 0
        # looping through each character in the string and adding to total
        for char in coins:
            if char == "P":
                purse += .01
            elif char == "N":
                purse += .05
            elif char == "D":
                purse += .1
            elif char == "Q":
                purse += .25
            elif char == "H":
                purse += .50
            elif char == "W":
                purse += 1
            # lets user know if they entered an invalid character
            else:
                print("Invalid coin:", char)
            
        self.totalChange = round(purse, 2)

