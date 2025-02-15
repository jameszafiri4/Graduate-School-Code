/* CSC6302 Database Principles
	Unit Three: Intermediate SQL
    Professor Minton
*/

use mealplanning;

-- Let's start thinking about joins, and get the names of all the recipes, and the cookbooks they were published in:
select r.RecipeName, c.CookbookName
from recipe as r inner join cookbook as c on r.CookbookName = c.CookbookName;

-- Or, we could not waste the database engines time, and use a simple select statement to get the same information. This may seem a silly example, but its always good to know
-- that a query can be written more then one way, and that some ways are better. Why is this way better? The database engine has to retrieve a lot less data! 
select RecipeName, CookbookName from recipe;

-- But, sometimes we do need to join. For example, what if I asked you to get the names of all the recipes that were published online? That information is not in the recipe table, it
-- can only be found in the cookbook table. We need to join!
select r.RecipeName, c.CookbookName
from recipe as r inner join cookbook as c on r.CookbookName = c.CookbookName
where c.IsBook = false;

-- The Meal table is something that database engineers and designers refer to as a mapping table. For our purposes, it solves the problem that a single recipe has multiple ingredients,
-- and we do not want to have to write out the name of the ingredients all the time. Why would we? It just takes up more hardrive space. Sure, maybe its only a few characters more, but
-- as this database gets larger, those unneeded characters add up. We could have designed this table to not store the recipe names over and over as well, that would have been a best practice,
-- but I wanted to show you that a string can be a primary key. 
select * from Meal;

-- To get the ingredient name when needed, we have to join to the Ingredient table. Note that the names of the ids that we are joining on do not have the same name. They do not need to!
select *
from meal as m inner join ingredients as i on m.IngredientId=i.Id;

-- That result set is a bit all over the place, let's order things so they look nicer, and think about only the relevent columns!
select m.RecipeName, i.IngredientName, i.IngredientType
from meal as m inner join ingredients as i on m.IngredientId=i.Id
order by m.RecipeName, i.IngredientName;

-- Just like a regular query, we can filter to only see the pantry items. We don't need the IngredientType column in our result set anymore, it will always be pantry.
select m.RecipeName, i.IngredientName
from meal as m inner join ingredients as i on m.IngredientId=i.Id
where IngredientType='pantry'
order by m.RecipeName, i.IngredientName;

-- Now let's filter our result set and get all the recipes that can be found in an actiual book. I don't know, maybe we want to make dinner and our internet connection is out.
select m.RecipeName, i.IngredientName
from meal as m inner join ingredients as i on m.IngredientId=i.Id inner join recipe r on r.RecipeName = m.RecipeName inner join Cookbook c on r.CookbookName=c.CookbookName
where IngredientType='pantry' and IsBook = true
order by m.RecipeName, i.IngredientName;

-- Ok, hold on that is a mess, what are we trying to do? We want to know if a recipe is in a physical book. But meal doesnt know anything about that. Cookbook does. 
-- But meal and cookbook have no direct relation. But they both have a relation with Recipe. At this point, get out your database diagram. It will help you follow along! 
-- So, let's think, how do we know a recipe is in a physical book?
select RecipeName, c.CookbookName
from recipe as r inner join cookbook c on r.CookbookName=c.CookbookName
where c.IsBook=true;

-- That is better. Much more readible, and we have all the information I asked for. Almost. Were'nt we looking to see what recipes used what ingredients, and then wanted to 
-- filter that based on what recipes where in a physical book? Yes, that was it. So, how do we do that? We could use the With clause, and make a temporary relation to clean
-- up that complicated mess we wrote earlier. Complicated messes need to be avoided, and not because we are learning and I confused you. No one wants to look at a query
-- like that. Its not readable, and if its not readable, its not maintainable and if its not maintainable, it will cause bugs. So, simplier. More readible. We could do this:

WITH RecipesInPhysicalBook AS
(
select RecipeName, c.CookbookName
from recipe as r inner join cookbook c on r.CookbookName=c.CookbookName
where c.IsBook=true
)
select m.RecipeName, i.IngredientName
from meal as m inner join ingredients as i on m.IngredientId=i.Id inner join RecipesInPhysicalBook as book on book.RecipeName=m.RecipeName
order by m.RecipeName, i.IngredientName; 

-- That's much more readible, our join is shorter, and its clearer what we are doing. But, can we do better? What if we used a nested subquery, instead of making the join longer?
WITH RecipesInPhysicalBook AS
(
select RecipeName, c.CookbookName
from recipe as r inner join cookbook c on r.CookbookName=c.CookbookName
where c.IsBook=true
)
select m.RecipeName, i.IngredientName
from meal as m inner join ingredients as i on m.IngredientId=i.Id
where RecipeName in (select RecipeName from RecipesInPhysicalBook)
order by m.RecipeName, i.IngredientName; 

-- And technically, we don't even need the With clause. Using the With clause is a personal preference
select m.RecipeName, i.IngredientName
from meal as m inner join ingredients as i on m.IngredientId=i.Id
where RecipeName in (select RecipeName
										from recipe as r inner join cookbook c on r.CookbookName=c.CookbookName
										where c.IsBook=true)
order by m.RecipeName, i.IngredientName; 

-- Let's go back to the mess approach. We could clarify things with parenthesis to help with readability It's a little better. 
-- But honestly, the subquery approach made things much easier. And I find that a building block approach really
-- helps with all forms of code writing. If you find youself constantly writing the same subquery, or same With clause, there are tools
-- we will learn next class to help streamline your code writing. After all, programmers are lazy, and only want to write something once!
select m.RecipeName, i.IngredientName
from (((meal as m inner join ingredients as i on m.IngredientId=i.Id) 
				inner join recipe r on r.RecipeName = m.RecipeName)
                inner join Cookbook c on r.CookbookName=c.CookbookName)
where IngredientType='pantry' and IsBook = true
order by m.RecipeName, i.IngredientName;


