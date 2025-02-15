/* CSC6302 Database Principles
	Unit One: Database System Design
    Professor Minton
*/
    
/* This SQL script creates a new database, the MealPlanning database, and inserts some data into the database.
	This will be another example database we will be using in this course. */

-- First, lets add a database to work with, and let's use the MealPlanning set of relations. We can do this with the UI, using the "Add Schema" button, or we can write the SQL

-- Its good practice to check if the database exists before adding it, especially in a database script like this one. That way, you can run it multiple times!
DROP DATABASE IF EXISTS MealPlanning;

-- Create the database MealPlanning. Note this is the SQL Create Statement that is written for you when you use the UI to create a new schema
-- Also note that create schema is synonomous to create database in MySql. 
-- This is not true in Sql Server. It is a decision that the database engine creators decided to make.
CREATE DATABASE MealPlanning;

-- Because we are using a script, and because a script let's us execute against different databases, even in the same script, we have to tell it what database we want to use. If we want to use a different 
-- database later on, we would use another "Use" statement to indicate that. But we are going to stick to the Meal Planning Database.
USE  MealPlanning;

-- Now, we need to create the tables, which are how SQL internally stores a relation, and all the information about that relation. Notice that these create table SQL statements are very
-- similiar to our relation's schemas. Again, its a good practice to check if a table exists before creating it. We can drop tables if they currently exist. I'll show both ways in this script. The rest of the table definition should be familiar.
-- We see out relation/table name, its attributes in a comma seperated list, the domains of each attribute, and we define a primary key
--  The domain has more information then we've seen before: it talks about if an attribute can be null.

-- When I went to create the Cookbook relation, I noticed that our attribute Cookbook.Name was a poor choice, as Name is a MySql keyword.
-- Its good practice to not use keywords as attribute or table names. Also not that we are paying attention not only to our attribute domains, but if we allow nulls.
CREATE TABLE IF NOT EXISTS Cookbook (
CookbookName varchar(200)  not null,
IsBook bool not null,
Website varchar(200),
PRIMARY KEY ( CookbookName)
);

-- Let's see how we'd drop a table if its exists. I'll have to create it again, but since I know it doesn't exist at that point in the script, no need to check for existance before creating it. 
DROP TABLE IF EXISTS Cookbook;

CREATE TABLE Cookbook (
CookbookName varchar(200)  not null,
IsBook bool not null,
Website varchar(200),
PRIMARY KEY ( CookbookName)
);

-- We can also just drop the table althogther, because we know it exists. It would return an error if this was not true! And we'll have to create it one more time.
DROP TABLE Cookbook;

CREATE TABLE Cookbook (
CookbookName varchar(200)  not null,
IsBook bool not null,
Website varchar(200),
PRIMARY KEY ( CookbookName)
);

-- When i created the Recipe relation as a table, again I decided to rename some of my attrbutes. Name and Source are MySql keywords we want to avoid.
-- I also know that Cookbook.Name is referenced by Recipe.CookbookName, so let's make sure the domains/IngredientTypes match!
-- Also not that any attributes identified as a primary key or a foreign key when we designed the relations is not null! 
-- We haven't added any SQL to define those constraints, but when we do, these attributes/column must be not null!
CREATE TABLE IF NOT EXISTS Recipe (
RecipeName varchar(100) not null,
CookbookName varchar (200) not null,
TotalServings int,
PRIMARY KEY (RecipeName),
FOREIGN KEY (CookbookName) REFERENCES Cookbook (CookbookName) on update cascade on delete cascade
);

-- We had to rename some columns again, Name and IngredientType are SQL Keywords and we want to avoid that!
-- Also note the keyword auto_increment. This means that when we insert into the table, we dont have to give a value for Id, the database engine
-- will just do that for us, and our Ids will be in numerical order. This is a good practice for ensuring the values of a primary key column are unique. 
CREATE TABLE IF NOT EXISTS Ingredients (
Id int not null auto_increment,
IngredientName varchar(100) not null,
IngredientType varchar (100),
PRIMARY KEY (Id)
);

-- Two things of note here. I made sure that RecipeName had the same domain/IngredientType as Recipe.RecipeName, and our primary key can have multiple attrbutes, just like in relation algrebra
CREATE TABLE IF NOT EXISTS Meal (
RecipeName varchar(100) not null,
IngredientId int not null,
PRIMARY KEY (RecipeName, IngredientId),
FOREIGN KEY (RecipeName) REFERENCES Recipe (RecipeName) on update cascade on delete cascade,
FOREIGN KEY (IngredientId) REFERENCES Ingredients (Id) on update cascade on delete cascade
);

-- In order to query these tables, they need some data in them!

-- For our nullable columns, meaning the attributes whose domains allow nulls, we don't even need them in the insert staement, unless they have a value. The null is added for us by the database engine
INSERT INTO Cookbook (CookbookName, IsBook) VALUES ("Dude Diet", true);
INSERT INTO Cookbook (CookbookName, IsBook) VALUES ("Dude Diet Dinner", true);
INSERT INTO Cookbook (CookbookName, IsBook, Website) VALUES ("Domesticate Me", false, "http://domesticate-me.com");

INSERT INTO Recipe (RecipeName, CookbookName, TotalServings) VALUES ("Fajitas", "Dude Diet", 6);
INSERT INTO Recipe (RecipeName, CookbookName, TotalServings) VALUES ("Stir Fry", "Dude Diet Dinner", 3);
INSERT INTO Recipe (RecipeName, CookbookName, TotalServings) VALUES ("Stuffing", "Domesticate Me", 8);
INSERT INTO Recipe (RecipeName, CookbookName, TotalServings) VALUES ("Chicken Stew", "Dude Diet", 4);

INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Red Pepper", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Green Pepper", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Yellow Onion", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Chicken", "meat");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Enchillada Sauce", "pantry");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Shredded Cheese", "dairy");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Garlic", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Soy Sauce", "condiment");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Butter", "dairy");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Sausage", "meat");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Golden Delicious Apple", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Tyme", "spice");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Chicken broth", "pantry");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Stale bread crumbs", "pantry");

-- Because I am entering this data from our practive problem relation, I know the IngredientIds. If I didn't have those tables to work from, I'd just do a select on the Ingredient table, so I could
-- see the values addded by the database engine.
-- How would I do a select? Its the same concept as in relation alegrba, we use an operation on the relation to generate a relation instance. But the syntax is better for programmers to work with. Let's add one into the script! 
-- You can always highlight part of the script, and execute just that part, clicking the lighting bolt button.
SELECT * FROM INGREDIENTS;

INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 1);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 2);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 3);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 4);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 5);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 6);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 1);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 2);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 3);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 4);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 7);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 8);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 9);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing",3 );
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing", 10);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing", 11);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing", 12);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing", 13);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing", 14);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Chicken Stew", 1);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Chicken Stew", 4);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Chicken Stew", 14);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Chicken Stew", 13);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Chicken Stew", 3);

-- At this point, let's end with select statements, so we can see the current relation instances of all our four relations/tables:
-- Note that you will see the ingredient table twice, because we did a select earlier. You should get a tab opening for each table instance that looks similiar to the grids we've seen in class
SELECT * FROM Cookbook;
SELECT * FROM Recipe;
SELECT * FROM Ingredients;
SELECT * FROM Meal;

-- Project 3 starts here

-- 1.) Function that determines if an ingredient is in the Ingredient table
DROP FUNCTION IF EXISTS IsIngredient;
delimiter $$
CREATE FUNCTION IsIngredient(ingredientName varchar(100))
RETURNS BOOLEAN DETERMINISTIC
BEGIN
    DECLARE doesExist bool;    
    SET doesExist = EXISTS 
		(SELECT IngredientName  
		FROM Ingredients
		WHERE IngredientName = ingredientName);

    RETURN doesExist;
END $$
delimiter ;
        
-- checking that it works below
select IsIngredient ('Chicken');

-- 2.a) Insert your favorite recipe into the MealPlanning database.

-- first using the stored procedure from the in class exercise as well as functions that go with it
DROP FUNCTION IF EXISTS doesCookbookExist;
delimiter $$
CREATE FUNCTION doesCookbookExist(myCookBookName VARCHAR(200))
RETURNS BOOLEAN DETERMINISTIC
BEGIN
    DECLARE doesExist bool;    
    SET doesExist = EXISTS 
		(SELECT CookbookName  
		FROM Cookbook
		WHERE CookbookName = myCookBookName);
    RETURN doesExist;
END $$
DELIMITER ;

DROP FUNCTION IF EXISTS doesRecipeExist;
delimiter $$
CREATE FUNCTION doesRecipeExist(myRecipeName VARCHAR(200))
RETURNS BOOLEAN DETERMINISTIC
BEGIN
 declare result varchar(200);
  SET result = (SELECT RecipeName FROM Recipe WHERE RecipeName = myRecipeName);
    RETURN (result IS NOT NULL);
END $$
DELIMITER ;

DROP PROCEDURE IF EXISTS InsertNewRecipe;

delimiter $$
    CREATE PROCEDURE InsertNewRecipe (
		myRecipeName varchar(100),
        myCookBookName varchar(200),
        myTotalServings int,
        myIsBook bool,
        myWebsite varchar(200))
    BEGIN

if (select doesCookbookExist(myCookBookName) = false ) then
insert into Cookbook  (cookbookName, isBook, Website) values (myCookBookName, myIsBook, myWebsite);
end if;

if (select doesRecipeExist(myRecipeName) = false) then
insert into Recipe (RecipeName, CookbookName, TotalServings) values (myRecipeName, myCookBookName, myTotalServings);
end if;

    END $$
    delimiter ;

-- inserting recipe using procedure
CALL InsertNewRecipe('Scrambled Eggs', 'James CookBook', 1, true, 'https://www.loveandlemons.com/scrambled-eggs-recipe/');

-- making sure it worked corectly
select *
from Recipe;

select *
from CookBook;

-- 2.b) New stored procedure that will update the ingredient and meal table
DROP PROCEDURE IF EXISTS InsertFavoriteRecipeIngredients;

delimiter $$
    CREATE PROCEDURE InsertFavoriteRecipeIngredients (
		myRecipeName varchar(100),
        myCookBookName varchar(200),
        myIngredientName varchar(100),
        myIngredientType varchar(100),
        myTotalServings int,
        myIsBook bool,
        myWebsite varchar(200))
    BEGIN

if (select doesCookbookExist(myCookBookName) = false ) then
insert into Cookbook  (cookbookName, isBook, Website) values (myCookBookName, myIsBook, myWebsite);
end if;

if (select doesRecipeExist(myRecipeName) = false) then
insert into Recipe (RecipeName, CookbookName, TotalServings) values (myRecipeName, myCookBookName, myTotalServings);
end if;

if (select IsIngredient(myIngredientName) = false) then
insert into Ingredients (IngredientName, IngredientType) values (myIngredientName, myIngredientType);
end if;

if (doesRecipeExist(myRecipeName) = false) then
insert into Meal (RecipeName) values (myRecipeName);
end if;

    END $$
    delimiter ;

-- double checking functionality
CALL InsertFavoriteRecipeIngredients('Scrambled Eggs', 'James CookBook', 'Eggs', 'animal product', 1, true, 'https://www.loveandlemons.com/scrambled-eggs-recipe/');

-- 3.) Procedure that takes an input a recipe name, and returns all the ingredients used in that recipe, in alphabetical order.
DROP PROCEDURE IF EXISTS GetIngredientsForRecipe;

DELIMITER $$
CREATE PROCEDURE GetIngredientsForRecipe(
    myRecipeName VARCHAR(100))
    
BEGIN
    DECLARE recipeExists BOOLEAN;
    
    SELECT doesRecipeExist(myRecipeName) INTO recipeExists;
    
    IF recipeExists THEN
        SELECT i.IngredientName
        FROM Ingredients as i JOIN Meal as m ON i.Id = m.IngredientId
        WHERE m.RecipeName = myRecipeName
        ORDER BY i.IngredientName;
    ELSE
        SELECT NULL AS IngredientName;
    END IF;
END $$
DELIMITER ;

-- checking functionality
CALL GetIngredientsForRecipe('Fajitas');

-- 4.) View that displays all required information
DROP VIEW IF EXISTS RecipeDetails;
CREATE VIEW RecipeDetails AS
SELECT r.CookbookName, r.RecipeName, i.IngredientName
FROM Recipe as r JOIN Meal as m ON r.RecipeName = m.RecipeName JOIN Ingredients as i ON m.IngredientId = i.Id
ORDER BY r.CookbookName, r.RecipeName, i.IngredientName;

select *
from RecipeDetails;

-- 5.) Query to determine number of ingredients in each recipe and in specified order
SELECT r.RecipeName, COUNT(m.IngredientId) AS NumberOfIngredients
FROM Recipe as r JOIN Meal as m ON r.RecipeName = m.RecipeName
GROUP BY r.RecipeName
ORDER BY NumberOfIngredients DESC;

-- 6.) Query for what ingredients are not contained within your favorite recipe
SELECT r.RecipeName, i.IngredientName
FROM Recipe as r JOIN Meal as m ON r.RecipeName = m.RecipeName JOIN Ingredients as i ON m.IngredientId != i.Id
WHERE r.RecipeName = 'Scrambled Eggs'
ORDER BY i.IngredientName;


