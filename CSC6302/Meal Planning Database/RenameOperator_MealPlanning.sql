/* CSC6302 Database Principles
	Unit Two: Basic SQL
	Professor Minton
*/

-- As always, we need to tell the database engine what database we are going to use. Let's keep using the MealPlanning database for now
USE MealPlanning;

-- On Monday, we talked about how to select data from relations, how to filter the columns (using select), how to compute the Cartesian Product,
-- and how to filter the results of a Cartesian Prouct so we only get the relevent data (similiar to how we used the Cartsesian Product in Relational
-- Algebra to join two tables together). We also touched briefly on Rename. So let's write some review queries:


-- What are the names of all the pantry items? Scroll down to see the answer once you have it figured out.



















-- Notice that I used the rename operator here, so my resulting relation makes more sense
-- to whever asked me for the names of all the pantry items. This is a nice way to use the rename operator to make your SQL more readable.
SELECT IngredientName AS PantryIngredient
FROM Ingredients
WHERE IngredientType="pantry";

-- I could also ask you for all the ingredients that are not pantry items:
SELECT IngredientName
FROM Ingredients
WHERE IngredientType!="pantry";

-- Or, for all the product and dairy items:
SELECT IngredientName as PantryIngredient
FROM ingredients
WHERE IngredientType="produce" OR IngredientType ="dairy";

-- We can use "and" in our predicate as well as equals, does not equal and or. Let's get all the produce needed for fajitas:
SELECT *
FROM Meal, Ingredients
WHERE id=ingredientId AND RecipeName="Fajitas";










-- We can also be a bit more vague in our predicates, while at the same time enhancing their readability. For example:
SELECT *
FROM Recipe
WHERE TotalServings BETWEEN 4 AND 6;

-- Instead of writing 
SELECT *
FROM Recipe
WHERE TotalServings  >= 4 AND TotalServings <= 6;

-- The BETWEEN operator is especially useful for any attribute that could easily be tied to a range. Services between 4 and 6. A log entry that was made between 
-- the first of the year and yesterday.  This is a useful operation that you can use in your predicates!

-- Remeber that I told you * is great for writing queries and practicing, but really when your sending your result sets back to a program,
-- its best to specifically mention the columns by name in the select clause. That is still true, but here's another lazy piece of syntactic sugar
-- you could use:

SELECT Meal.*, Ingredients.*
FROM Meal, Ingredients
WHERE id=ingredientId AND RecipeName="Fajitas";

-- When we rename, we aren't limited to doing that in the select clause. We can do it in the from as well:
-- You can rename to something sensible, like we did in the select claue, and that's really important as the name you use
-- will show up in your resulting relation. With the from clause, its really just a way to be a lazy programmer and save yourself
-- some typing. Try to still be relevent (I used the relations initials), because you don't want to make your code unreadable or unmaintainble
-- by introducing confusing abbreviations. And remember that you are assiging an alias to the table. So m and i are refered to as table aliases.
-- More formally, they are known as correlation names.
SELECT *
FROM Meal AS m, Ingredients AS i
WHERE i.id=m.ingredientId AND m.RecipeName="Fajitas";

-- We don't always know the exact values in a table that we want to search for. This isn't really a big deal for us, our tables are small and have very little data. 
-- And sometimes, we have a lot of very similiar values. For example, we have two cookbooks with similar names: "Dude Diet" and "Dude Diet Dinner". Is there
-- an easier way to find both these cookbooks without writing two predicates? Yes.
SELECT *
FROM Cookbook
WHERE CookbookName LIKE "Dude Diet%";

-- We can the % approach for strings that end similar, like Red Pepper and Green Pepper:
SELECT *
FROM Ingredients
WHERE IngredientName LIKE "%Pepper";

-- And of course we could also use the % at the beginning and end of our predicate. We don't really have a good example, so let's make one:

INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Hot Pepper: Jalapeno", "produce");
SELECT *
FROM Ingredients
WHERE IngredientName LIKE "%Pepper%";

-- Let's talk about another operator. Maybe, in the query above, I want to return all my peppers in alphabetical order. We know relations/tables are sets,
-- so they don't have an order. Anytime you query the database, you aren't not gaurenteed to get your results in any particular order. But you might want to 
-- impose an order.

SELECT *
FROM Ingredients
WHERE IngredientName LIKE "%Pepper%"
ORDER BY IngredientName;

-- You can even be more specific and tell the query if you want to order in ascending or descending order. By default, its ascending
SELECT *
FROM Ingredients
WHERE IngredientName LIKE "%Pepper%"
ORDER BY IngredientName DESC;

-- We can play around with order even more, and order our results by multiple columns, and we can even mix ascending and descending orders.
-- Remeber that while relational algebra does not return duplciates, SQL does, and we are doing just a Cartesian Product here, so we want to filter out
-- duplicates.
SELECT DISTINCT *
FROM Meal, Ingredients
ORDER BY RecipeName ASC, IngredientName DESC;

-- Let's pause and do some practice, in SQL and Relational Algebra

-- 1. What are the names of all the recipes, and all their ingredients, with both the recipes and their ingredients presented in ascending order?
SELECT RecipeName, IngredientName
FROM meal AS m, ingredients AS i
WHERE m.ingredientid=i.id
ORDER BY RecipeName, IngredientName;

-- 2. What recipes can be found in a book? Order the results so the books and recipes are in ascending order
SELECT c.CookBookName, r.RecipeName
FROM Cookbook AS c, Recipe AS r 
WHERE c.CookBookName = r.CookbookName AND c.IsBook=true
ORDER BY c.CookBookName, r.RecipeName;

-- 3. What are the names of all the recipes that use some kind of pepper? Give me the recipe results in descending order and the pepper results in ascending.
SELECT m.RecipeName, i.IngredientName
FROM Meal AS m, Ingredients AS i
WHERE m.IngredientId=i.Id AND i.IngredientName like "%Pepper%"
ORDER BY m.RecipeName DESC, i.IngredientName ASC;
























-- Practice Answers

SELECT *
FROM Meal as m, Ingredients as i
WHERE m.IngredientId = i.Id
ORDER BY RecipeName ASC, IngredientName ASC;

SELECT c.CookBookName, r.RecipeName
FROM Cookbook AS c, Recipe AS r
WHERE c.CookBookName = r.CookBookName AND IsBook = true
ORDER BY c.CookBookName ASC, r.RecipeName ASC;

SELECT *
FROM Meal as m, Ingredients as i
WHERE m.IngredientId = i.Id AND IngredientName LIKE "%Pepper%"
ORDER BY RecipeName DESC, IngredientName ASC;


/* Set Operation! 
 Notice this is how we do multiline comments in MySQL */

-- The set operations that we talked about in relational algrebra also exist in SQL. Union. Intersect. Set Difference. And as you can imagine, the concept is the same,
-- we are just going to see what syntax SQL uses:

-- UNION EXAMPLE: Find all the recipes in Domesticate Me and Dude Diet Dinner cookbooks
SELECT *
FROM Cookbook as c, Recipe as r
WHERE c.CookbookName = r.CookbookName and c.CookbookName = "Domesticate Me"
UNION
SELECT *
FROM Cookbook as c, Recipe as r
WHERE c.CookbookName = r.CookbookName and c.CookbookName = "Dude Diet Dinner";

-- INTERSECT Example: Find the ingredients  that are in Fajitas and Stuffing. Note that MySQL does not support the Intersect operator, but you
-- can simulate it, and we will return to it when we talked about subqueries and nested subqueries.alter.
--  Its always importat to know where your specific langauge deviates from the SQL standars! But here's what you would write, if
-- your flavor of SQL followed this stadard and included the operator:


/*SELECT IngredientName
 FROM Ingredients, Meal
 WHERE Id=IngredientId AND RecipeName="Fajitas"
 INTERSECT
 SELECT IngredientName
 FROM Ingredients, Meal
 WHERE Id=IngredientId AND RecipeName="Stuffing"
*/

-- We are also going to run into this issue with Set Difference (Or Except). Mq SQL doesn't support that operator, but the SQL standard does, Let's see how we
-- would handle the following example, and see how we can get around our lack of Except.

-- EXCEPT Example: My dinner guest is lactose intolerant. What recipe can I make for them. It cannot contain dairy.
-- Here's a quick solution. Is it correct? Hint: it is not. Why?

SELECT *
FROM Ingredients, Meal
WHERE Id=IngredientId and IngredientType != "dairy";

-- The problem here is that this query doesn't take into account that a recipe has multiple ingredients. Its only returning me the recipes
-- that have at least one ingredient that is not dairy. They definitly might have dairy as another ingredient. So this is not going to work!

-- Here's how we can use the idea of the EXCEPT operator in MYSQL to filter down what we need in simple way. This is an example of a subquery.
(SELECT RecipeName, IngredientName
FROM Ingredients, Meal
WHERE Id=IngredientId AND Id NOT IN  (SELECT ID FROM Ingredients WHERE IngredientType="dairy");


