'''
                JAMES ZAFIRI    WORKSHEET 1    CSC6013

This program will define a function that checks if it is cold in Canada today

- It will first ask the Canadian what the threshold for cold is in Celcius (input)
- Then, it will ask for today's temperature in Fahrenheit (input)
- Next, it will convert the Fahrenheit input to Celcius and compare the two
- After making the comparison, the program will say if the given temp is cold for a Canadian

'''

def coldInCanada():
    # loop using exception handling in case user doesn't enter a number
    while True:
        try:
            c = int(input("Hello Canadian, what do you consider as cold? Please enter a temp in C0: "))
            f = int(input("Now, please enter today's temp in F0: "))

            convert = (f - 32) * (5 / 9)

            if convert <= c:
                print("It is cold today!")
                break

            else:
                print("It is not cold today.")
                break
            
        except ValueError:
            print("Please try again with a valid integer for the temp.\n")
    
                  
coldInCanada()
