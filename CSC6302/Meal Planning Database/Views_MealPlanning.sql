/* CSC6302 Database Principles
	Unit Three: Intermediate SQL
    Professor Minton
*/

-- Tell the database engine what database we are using
use mealplanning;

-- A View is a useful tool is SQL, as it allows you to define a relation, via query, that can be resused over and over (much like a table)
-- The relation itself is not stored by the databse engine. The query is. So, in a way, its like using the With command, and giving a 
-- name to a query to make your sql script more readible. But, unlike With, a View can be used in different scripts. Let's see what
-- I'm talking about.

-- I would like to know what recipes use pantry ingredients. You could see how this sort of query could be run often, especially if
-- you are lucky enough to grocery shop for your household. I know I like to find these sorts of recipes whenever I "have no food"
-- but also, my pantry is overflowing. What would that query look like?

select RecipeName
from meal;

-- Note that queries the meal table. The Meal table is a mapping table that maps the recipe table to the ingredient table, so its
-- a good place to start. And conviently, the foregin key that maps Recipe to Meal is recipename, so we don't need to do a join.
-- But, we should use the distinct keyword, because the Meal table has one row per ingredient for each recipe.

select distinct RecipeName
from meal;

-- But it's only tell me about the recipes. I want to make sure I plan meals for the week that use pantry items. Meal doesn't
-- know anything about ingredient types, so I need to join with the Ingredients table to get that information.
select distinct RecipeName
from meal as m inner join Ingredients as i on m.IngredientId=i.Id
where i.IngredientType = 'pantry';

-- The recipe name doesn't really help me much. Cool, I can make chicken stew with pantry ingredients. But I have no idea what ingredients that needs,
-- or if those ingredients are actually in my pantry. So, let's get the ingredient names

select distinct RecipeName, IngredientName
from meal as m inner join Ingredients as i on m.IngredientId=i.Id
where i.IngredientType = 'pantry';

-- Ok that is a query that I can work with. It gives me exactly what I want. I know there are no duplicate rows. The column names make sense. This
-- is a maintable and reusable query. So, let's tell the database about it, so the query is stored within the database engine, and can be used just
-- like any other relation!

CREATE VIEW RecipesToEmptyMyPantry AS
select distinct RecipeName, IngredientName
from meal as m inner join Ingredients as i on m.IngredientId=i.Id
where i.IngredientType = 'pantry';

-- And know we can use this like any other relation!
select * from RecipesToEmptyMyPantry;

-- You can even open a new query window and run that select statement, and I encourage you to try it. 
-- If you take a look at the Scema window in MySQL Workbench, you will notice under MealPlanning there is 
-- a section for views, and our new view is listed under that section (you may need to refresh the window to see this)