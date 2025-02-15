import random

class BankUtility:
    
    def __init(self):
        pass
    
    '''
    This method prompts the user to enter a string and receives
    input from keyboard. It then returns the string
    '''
    def promptUserForString(self, prompt):
        x = str(input(prompt))
        return x
    
    '''
    This method prompts the user to enter a positive number input
    from keyboard. It makes sure that it isn't negative then returns it
    '''
    def promptUserForPositiveNumber(self, prompt):
        while True:
            y = float(input(prompt))
            if y <= 0.0:
                print("Amount cannot be negative. Try again.")
            else:
                break
            
        return y

    '''
    This method takes two integer paramaters that are a min and max
    and then generates a random number inbetween those values
    '''    
    def generateRandomInteger(self, min, max):
        n = random.randint(min, max)     
        return n

    '''
    This method takes a float and converts it to an integer
    AKA, dollar and cent amount to only cents
    '''
    def convertFromDollarsToCents(self, amount):        
        cents = int(float(amount) * 100) 
        return cents 
    
    '''
      Checks if a given string is a number (long)
      This does NOT handle decimals.
      
      @param numberToCheck String to check
      @return true if the String is a number, false otherwise
     '''
    def isNumeric(self, numberToCheck):
        try:
            if numberToCheck.isdigit():
                return True
            else:
                return False
        except ValueError:
            return False
