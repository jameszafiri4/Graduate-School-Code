'''
                JAMES ZAFIRI    WORKSHEET 1    CSC6013

- This is a function that will receive 3 paramaters (numbers) from the user when called
- The function, called zigzag, will look at these 3 paramaters as a, b, c
- It will compare the 3 numbers to make sure they are zigzag and then return True or False
- The numbers are zigzag if:  a < b > c  OR  a > b < c
- THIS PROGRAM WILL ASSUME THE ENTERED PARAMETERS ARE NUMBERS; NO ERROR HANDLING

'''

def zigzag(a, b, c):
    if (a < b and b > c) or (a > b and b < c):
        return True
    else:
        return False
