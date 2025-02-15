'''
James Zafiri CSC6302 Project 4 11/27/2023
This file contains a simple holiday meal planning application that allows a user to plan their holiday party menu. 
This application will be using the meal planning database. The program will be split up into a presentation layer
which is going to be the main function interacting with the user, a business logic layer that will contain a class
for the holiday party menu, and finally a DAL which is the class meant for interacting with the database.
'''

import mysql.connector
from mysql.connector import errorcode

class MealPlanningDAL:
    '''
    This class is the DAL. This is how we are actually interacting with
    the MealPlanning database to get the required information.
    '''
    def __init__(self, username, password):
        '''
        This is the constructor method of the class, and will take in two
        parameters: username & password. This will be given by the user so
        that we do not hardcode this information into the program.
        '''
        self.cnx = mysql.connector.connect(
            user=username,
            password=password,
            host='127.0.0.1',
            database='MealPlanning'
        )
        self.cursor = self.cnx.cursor()
    
    def get_cookbook(self):
        '''
        This method is to obtain a cookbook given by the user from a list
        of cookbooks in the database.
        '''
        self.cursor.execute("SELECT CookbookName FROM Cookbook")
        return [row[0] for row in self.cursor.fetchall()]

    def get_recipe_from_cookbook(self, cookbook_name):
        '''
        This method is to obtain the recipes from any given cookbook
        in the database that was chosen by the user.
        '''
        self.cursor.execute("SELECT RecipeName FROM Recipe WHERE CookbookName =%s", (cookbook_name,))
        return [row[0] for row in self.cursor.fetchall()]

    def get_recipe_ingredients(self, recipe_name):
        '''
        This method is to obtain all of the ingredients of any given
        recipe in the database that is specified by the user.
        '''
        self.cursor.execute(
            "SELECT IngredientName FROM Ingredients AS i " \
            "JOIN Meal AS m ON i.Id = m.IngredientId " \
            "WHERE m.RecipeName = %s", (recipe_name,)
        )
        return [row[0] for row in self.cursor.fetchall()]

class HolidayPartyMenu:
    '''
    This class is the business logic layer. It will contain the actual menu for
    the holiday party. It will be able to add a recipe and it's required info,
    generate a shopping list, and display the menu for the user.
    '''
    def __init__(self):
        '''
        This is the constructor method of the class. It will take in no
        parameters, and initialize a menu object as an empty array.
        '''
        self.menu = []

    def add_recipe(self, recipe_name, cookbook_name, ingredients, course):
        '''
        This method is meant to actually add recipes and all of their
        required information into the menu object that was created, based on user.
        '''
        self.menu.append({
            "RecipeName": recipe_name,
            "CookbookName": cookbook_name,
            "Ingredients": ingredients,
            "Course": course
        })

    def create_shopping_list(self):
        '''
        This method is meant to create a shopping list for the
        user containing all of the ingredients that are needed based
        on the menu.
        '''
        shopping_list = []
        for item in self.menu:
            shopping_list.extend(item["Ingredients"])
        return shopping_list
    
    def display_menu(self):
        '''
        This method is for the menu and all of its contents
        to be displayed for the user to see.
        '''
        for item in self.menu:
            print(f"{item['RecipeName']} from {item['CookbookName']} ({item['Course']})")
    
def main():
    '''
    This is our main function which will act as the presentation
    layer and where we interact with the user. This is where we
    connect our DAL and Holiday Menu and implement what we wanted
    our program to do
    '''
    username = str(input("Enter your MySQL username: "))
    password = str(input("Enter your MySQL password: "))

    try:
        dal = MealPlanningDAL(username, password)
        holiday_menu = HolidayPartyMenu()

        print("\nHello! Welcome to the Holiday Meal Planning Application.")

        # this allows the user to select a cookbook
        cookbooks = dal.get_cookbook()
        print("\nPlease select a cookbook: ")
        for i, cookbook in enumerate(cookbooks, start=1):
            print(f"{i}. {cookbook}")

        cookbook_index = int(input("\nEnter the number of the cookbook you want: ")) - 1
        my_cookbook = cookbooks[cookbook_index]

        # this allows the user to select a recipe from a cookbook
        recipes = dal.get_recipe_from_cookbook(my_cookbook)
        print(f"\nSelect a recipe from {my_cookbook}: ")
        for i, recipe in enumerate(recipes, start=1):
            print(f"{i}. {recipe}")

        recipe_index = int(input("\nEnter the number of the recipe you want: ")) - 1
        my_recipe = recipes[recipe_index]

        # this allows the user to get the ingredients for a given recipe
        recipe_ingredients = dal.get_recipe_ingredients(my_recipe)
        print(f"\nIngredients for {my_recipe}: ")
        for ingredient in recipe_ingredients:
            print(ingredient)

        # this allows the user to save a recipe to the holiday party menu
        course = str(input("\nEnter the course of this recipe (for example: lunch or dinner): "))
        holiday_menu.add_recipe(my_recipe, my_cookbook, recipe_ingredients, course)

        # this creates and displays a shopping list for the menu
        shopping_list = holiday_menu.create_shopping_list()
        print("\nShopping List: ")
        for item in shopping_list:
            print(item)

        # this displays the menu
        print("\nHoliday Party Menu: ")
        holiday_menu.display_menu()


    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    # this is meant to close out of the cursor once we are all set
    else:
        dal.cnx.close()

if __name__ == "__main__":
    main()
