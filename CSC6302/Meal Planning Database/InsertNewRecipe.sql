USE mealplanning;

-- Let's check and see if the procedure exists, and drop it, before we change the delimiter
-- This is really a single statement we want to run right now. We don't need to group it 
-- with the create procedure statements. And actually, if we did that, we might run into issues when
-- we run this query file. 
DROP PROCEDURE IF EXISTS InsertNewRecipe;

delimiter $$
    CREATE PROCEDURE InsertNewRecipe (
		myRecipeName varchar(100),  -- Note the size I chose for the parameter matches the Recipe tables column size!
        myCookBookName varchar(200), -- Also note my parameters have names that are distinct!
        myTotalServings int,
        myIsBook bool,
        myWebsite varchar(200))
    BEGIN
    
-- Declare two varchar variables, whose sizes match the sizes of the cookbook name and recipe name
DECLARE existingCookbookName varchar(200);
DECLARE existingRecipeName varchar(100);

/* Do we already have a cookbook entry?
 Notice that I am selecting into the variable existingCookBookName whatevber my query happens to return. Also remeber that
 queries return a set, so my query could be trying to insert several cookbook names into my variable, one after another. I don't really 
 care. I just care that something was inserted into my variable, because that means we already have a cookbook with that name..
 
 And also...we actually do know my query will only ever return one result: cookbook name is a primary key, and must be unique! 
 */
SELECT CookbookName INTO existingCookbookName 
FROM Cookbook
WHERE CookbookName = myCookBookName;

-- Do we already have a recipe entry? This is very similar to what we just did.
select RecipeName into existingRecipeName 
from Recipe
where RecipeName = myRecipeName;

-- Check and see if we actually inserted anything into the cookbook variable. If there was no existing cookbook with that name, it will
-- not have any value stored in it, so it will be null. We can check for nulls!
if (existingCookbookName is null) then
insert into Cookbook  (cookbookName, isBook, Website) values (myCookBookName, myIsBook, myWebsite);
end if;

-- More of the same
if (existingRecipeName is null) then
insert into Recipe (RecipeName, CookbookName, TotalServings) values (myRecipeName, myCookBookName, myTotalServings);
end if;

    END $$
    delimiter ;