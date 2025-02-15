-- full table scan
select * from Recipe;

-- Equality on a nonkey column
-- just a table scan
select * from Ingredients where ingredienttype = 'dairy';

-- Equality on a nonclustered index column
-- covering index scan
explain analyze
select RecipeName from Meal where RecipeName like "%F%";

-- Equality on a clustered  index column
-- covering index scan
explain analyze
select RecipeName from Recipe where RecipeName like "%F%";

-- Inner Join
-- nested loop with a non-unique key lookup and a full table scan
-- So , for every row in table r, we do a key lookup in table m
select *
from Recipe as r inner join Meal as m on r.RecipeName=m.RecipeName;

-- Same execution plan...it was smart enough not to do a full table scan on the meal table, which
-- has a lot more rows then the recipe table
select *
from Meal as m inner join Recipe as r on r.RecipeName=m.RecipeName;

-- Now let's join all three tables together and see what happens
-- We still have a full table scan for recipe
-- There is a non unique key lookup for Meal, because RecipeName and IngredientName on their own, are not unique in the table
		-- A recipe has several ingredients
        -- Particular Ingredients are used in many recipes 
explain analyze
select * 
from  Meal as m inner join Recipe as r on r.RecipeName=m.RecipeName inner join Ingredients as i on i.id=m.ingredientId
where r.Recipename like "fajitas";

explain analyze
With fajitas as(
select r.recipeName, m.ingredientId
from Meal as m inner join Recipe as r on r.RecipeName=m.RecipeName
where r.recipename like "fajitas")
select * 
from  fajitas as f inner join Ingredients as i on i.id=f.ingredientId;

explain analyze
select doesCookbookExist("Dude Diet Dinner Time");

 select * 
from  Meal as m inner join Ingredients as i on i.id=m.ingredientId inner join Recipe as r on r.RecipeName = m.recipeName;

-- Let's look at a subquery and compare it to an outer join. Note we have the same execution plan, and in both cases
-- the execution plan has decided the join is the most efficient solution 
select * 
From Recipe
where RecipeName not in (select RecipeName from Meal);

select * 
from recipe as r left outer join meal as m on r.RecipeName = m.RecipeName
where m.recipeName is null;