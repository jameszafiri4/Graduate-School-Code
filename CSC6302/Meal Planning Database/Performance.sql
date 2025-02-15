/* CSC6302 Database Principles
	Unit Eight: Query Processing and Optimization
    Professor Minton
*/

/* Let's look at a simple example of a MySql execution plan. You may have noticed, but whenever you execuute a query, 
there is a list of options on the right side of our result window. We've been using the ResultGrid to see what the query
returned. But MySQL gives us lot of other views
r*/

select * from Recipe, Meal;

-- and the explain anlayze
explain analyze
select * from Recipe, Meal;

-- Let's look at something a bit more complicated
explain analyze	
select * 
from Recipe as r inner join Meal as m on r.RecipeName = m.RecipeName 
where IngredientId > 12;

-- What if we use projection?
explain analyze
select r.RecipeName, i.IngredientName
from Recipe as r inner join Meal as m on r.RecipeName = m.RecipeName inner join Ingredients as i on i.Id=m.IngredientId
where IngredientId > 2
order by r.RecipeName, i.IngredientName;

-- Let's look at a common mistake people make
explain analyze
Select *
from Meal inner join Recipe
where meal.recipeName = Recipe.RecipeName;

explain analyze
Select *
from Meal inner join Recipe on meal.recipeName = Recipe.RecipeName;



