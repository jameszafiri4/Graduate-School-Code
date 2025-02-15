# This program will allow the user to input a value for the radius of a circle/sphere
# It will then return the values of the circumference, area, and volume of the circle/sphere based on that radius

import math # calls the math module to use pi

def circle_sphere_calc():
    R = eval(input("Enter the radius: \n")) # takes the user's input for the radius and then it evaluates the string to store it as a number within the variable
    
    C = 2 * math.pi * R # formula for circumference, using the variable for radius we created earlier
    A = math.pi * (R ** 2) # formula for area, using the variable for radius we created earlier
    V = (4 / 3) * math.pi * (R ** 3) # formula for volume, using the variable for radius we created earlier

    print("The circumference of a circle with a radius of", R, "is", C) 
    print("The area of a circle with a radius of", R, "is", A)
    print("The volume of a sphere with a radius of", R, "is", V)

circle_sphere_calc() # calls the function so it can execute
