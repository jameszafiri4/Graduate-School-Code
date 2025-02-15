import mysql.connector
from mysql.connector import errorcode

username = str(input("Please enter username: "))
password = str(input("Please enter password: "))

try:
    cnx = mysql.connector.connect(user=username, password=password,
                                 host='127.0.0.1',
                                 database='MealPlanning')

    cursor = cnx.cursor()
    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(x)

    cursor.execute("SELECT * FROM Ingredients;")
    for x in cursor:
        print(x)

    cursor.execute("SELECT isIngredient('Green Pepper');") #should return 1 as true
    for x in cursor:
        print(x)

    cursor.execute("SELECT isIngredient('Yogurt');") #should return 0 as false
    for x in cursor:
        print(x)

    cursor.execute("CALL InsertNewRecipe('Chicken Tortilla Soup', 'Gandalfs Cookbook', 4, true, null);")

    cursor.execute("SELECT * FROM Recipe")
    for x in cursor: 
        print(x)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
    
else:
    cnx.close()