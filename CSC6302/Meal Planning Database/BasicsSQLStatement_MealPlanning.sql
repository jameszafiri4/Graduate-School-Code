/* CSC6302 Database Principles
	Unit Two: Basic SQL
    Professor Minton
*/

-- Let's do some examples with Sql's SELECT statement. But first, we need to tell the script what Database we are using:
USE MealPlanning;

-- We can select every tuple in a table. Notice how every SQL statement ends with a semi-colon. This was true in the database creation files, and its true now.
SELECT *
FROM Meal;

-- We can select only certain column values:
SELECT RecipeName
FROM Meal;

-- If you run just the query above, you get lots of duplicates. We need to tell SQL we want our resulting relation to have no duplicates:
SELECT DISTINCT RecipeName
FROM Meal;

-- We can also use a predicate to filter our query results, using the Where clause.
SELECT *
FROM Ingredients
WHERE IngredientType="produce";

-- Do we need all the attributes? No? Let's not use the * operator, and instead tell the query what attributes we want to see. While the * is very convienent, especially when debugging issues in your database,
-- when we start interacting with our database from an application, we are going to want to be explicit about the column names we want in our relation. This will protect us from version skew, meaning
-- if a new feature was added that needed, say the needed weight of each ingredient, if we were using * everywhere, a lot of our other applications would know nothing about the new weight column
-- and we would get exception and bugs. That is something we want to avoid. So let's be explicit in what we want!
SELECT IngredientName
FROM Ingredients
WHERE IngredientType="produce";

-- I mentioned we could add a new column for ingredient weight. How would I do that?
-- This is commented out, because it can cause issues if run multiple times. This isn't something that we can check for existance before running.
-- Just highlight the statement, and run it on its own, for the purposes of this demo.
-- ALTER TABLE Ingredients ADD Weight double not null;

-- Note that my new column is full of nulls! This is actually a good practice, well having our new column be nullable is a good practice. This way, as customers upgrade their systems, they can choose to define weight or not. Not
-- all cutomers use all the features of a product. We could also provide a default value for this column, say 0, if we didn't want to allow nulls, or, more importantly, if we didnt want our customer to have to populate this new column to
-- use our new feature. But for this case, weights of ingredients vary, and the weight of red peppers vary, so its best to keep it null.
Select * 
From Ingredients;

-- We can do predicates with greater then, less then, equals, and does not equal as well. We can even combine predicates with and/or.
SELECT RecipeName, CookbookName
FROM Recipe
WHERE TotalServings > 4;

SELECT RecipeName, CookbookName
FROM Recipe
WHERE TotalServings > 4 and TotalServings < 8;

-- We can also do cartesian poroducts and joins (more on this later). The operator syntax is a comma. For today, let's stick with cartesian products, and let's use the where claus to filter things to something reasonable
SELECT *
FROM Meal, Recipe
WHERE Meal.RecipeName = Recipe.RecipeName and Recipe.TotalServings > 4;

select * from meal, ingredients;



