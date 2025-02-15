/* CSC6302 Database Principles
	Unit Three: Intermediate SQL
    Professor Minton
*/

-- Just like with every new file/tab in MySql, we need to tell the database what engine what database we are using
USE ArcadeGames;

/* Null is a wierd case that we have mentioned, but let's actually see what it does 
   -- In arithmatic operators, if one of the operands is a null, the result is null
   -- For boolean comparisons, things get weird. SQL actually has three states defined for its
      boolean type: True. False. Unknown.
        -- As you'd expect, if you compare unknown to anything, the result is unknown
        -- When you are filtering a column, and its possible some data is null, remeber that only values that
           evaluate to true will be returned. Unknown and False values will not           
*/

-- Notice the Player table has some nulls in the FavoriteGame column
SELECT *
FROM Player;

-- So let's use the column with nulls and do some math and see what happens:
-- Notice we have no nulls!
SELECT *
FROM Player
WHERE (FavoriteGame + 1) > 0;

-- We can do math in the select statement too, that will show us some nulls!
SELECT (FavoriteGame + 1)
FROM Player;

-- SQL has some more intuitive ways to deal with nulls. For example, get me all the user names  that don't have a favorite game:
SELECT UserName
FROM Player
WHERE FavoriteGame IS NULL;

-- And we could also do it this way (note that all flavors of SQL support this, but MySql does):
SELECT UserName
FROM Player
WHERE FavoriteGame IS UNKNOWN;

-- And we can do the reverse, and find all the players who have a favorite game
SELECT UserName
FROM Player
WHERE FavoriteGame IS NOT NULL;

-- And, we can use not unknown as well
SELECT UserName
FROM Player
WHERE FavoriteGame IS NOT UNKNOWN;

/* The key thing to remember here is that some columns allow nulls, and some don't. If you want to allow for nulls, you
   and allowing for the data to sometimes be unknown, and you need to think about that when writing any query with a predicate,
   or a math expression. A lot of subtle bugs are written by programmers who don't consider the ramifications of allowing, and
   working with, null values. 
   
   This is a concept that is not unique to SQL. Some programming languages allow the concept of a nullable type. C# has this notion.
   In C#, the type bool? considers a boolean whose value could be true, false or unknown, and the logic works much the same way. In the real
   world, unknown data is fairly common!
   */
   
   -- SQL queries can do math. Maybe we want to get fancy, and instead of doing a predicate against each tuple in the set, 
   -- we want to perform a mathematical operation on each value in a particular column in the result. That is also possible, because when we 
   -- execute the select, we are just tweaking the relation we requested.
   
   -- What are all the pac-man scores?
   SELECT Score
   FROM Score AS s, Game AS g
   WHERE s.GameId=g.Id AND G.GameName = "Pac-man";
   
   
	-- What is the average pac-man score?
   SELECT AVG(Score)
   FROM Score AS s, Game AS g
   WHERE s.GameId=g.Id AND G.GameName = "Pac-man";
   
   -- What is the worst pac-man scores?
   SELECT MIN(Score)
   FROM Score AS s, Game AS g
   WHERE s.GameId=g.Id AND G.GameName = "Pac-man";
   
   -- What is the best the pac-man scores?
   SELECT MAX(Score)
   FROM Score AS s, Game AS g
   WHERE s.GameId=g.Id AND G.GameName = "Pac-man";
   
   -- How many players have played pac-man?
   SELECT Count(Score)
   FROM Score AS s, Game AS g
   WHERE s.GameId=g.Id AND G.GameName = "Pac-man";
   
   -- How many points were scored in pac-man total?
   SELECT Sum(Score)
   FROM Score AS s, Game AS g
   WHERE s.GameId=g.Id AND G.GameName = "Pac-man";
   
   -- Instead of returning one particular relation, you can return a group of relations. 
   -- Tuples where the attributes are all the same are placed into a single group
   
   -- Let's use our meal planning database to do that, because we have some better examples.
   -- And this will show us that we can switch between different database in the same script.
   
   USE MealPlanning;
   
   -- Let's take a look at the meal table. Note that each meal has a good number of ingredents:
   SELECT *
   FROM Meal;
   
   -- We could use group by to group together all the tuples that have the same meal name. Notice that it just selects
   -- the first IngredientId associated with that meal for the value of the IngredientId table. That's pretty useless, right?
   SELECT RecipeName
   FROM Meal
   GROUP BY RecipeName;
   
   -- But, we can compute some math expression over a set of tuples, and we can definitly compute over each set in a group!
   -- So, we can, for example, find out how many ingredients are in each meal. 
   SELECT RecipeName, count(IngredientId)
   FROM Meal
   GROUP BY RecipeName;
   
   -- Now that makes more sense why we would group, and how aggregate functions can be used. But that column name is confusing, so let's rename it to somemthing sensible.
   SELECT RecipeName, count(IngredientId) as NumberOfIngredients
   FROM Meal
   GROUP BY RecipeName;
   
   USE ArcadeGames;
   
   -- Going back to our arcade database, let's find out the high score for each arcade game using group by and max:
   SELECT GameId, Max(Score)
   from Score
   GROUP BY GameId;
   
   -- I'd prefer the name of the games and a more sensible column name for the max score. Let's fix this:
   SELECT GameName, Max(Score) AS HighScore
   From Score, Game
   WHERE Score.GameId=Game.Id
   GROUP BY GameId;
   
   -- The above query is dangerous. If there are two games with the same name, but different id's, we could get unexpected results. In our example, this
   -- won't happen, game name is unique, and every game as a unique associated with it. But, it breaks a rule you want to stick to. If a column is in the
   -- select statement, and it is not part of an aggregate, you need to have that column in the group by clause. This allows the engine to have a definite value
   -- to put in the resulting relation. Some flavors of SQL would give you an error for the query above, but MySql is letting us set ourselves up for subtle bugs.
   -- The correct query to write is:
   SELECT GameName, Max(Score) AS HighScore
   From Score, Game
   WHERE Score.GameId=Game.Id
   GROUP BY GameName;
   
   -- Let's add another layer of complexity to group by: you can not only group a set of tuples with common attributes into a single row and perform some math
   -- on them to quickly get some needed information (like a high score), you can filter out what groups we end up seeing. Let's take Street Fighter's high score
   -- and see what games have a higher max score:
   SELECT GameName, Max(Score) AS HighScore
   From Score, Game
   WHERE Score.GameId=Game.Id
   GROUP BY GameName
   Having Max(Score) > 13456767;
   
   Select *
   From Score Join Game on Score.GameId=Game.Id
   
   /* Let's step through what in the world the query above just did:
   1. We always evaluate the from claus first. This is what we did in relational algebra as well!
   2. If there is a where claus, we filter the relation from step one
   3. Now, we worry about groups. If there is no group by clause, we have one group. If there is a group by clause,
      the tuples are grouped by the specified column, in this case GameName. Each GameName gets ONE tuple
   4. Is there a having clause? Yes, get rid of every group/tuple where the max score is less then or equal to 13456767
   5. Execute the select part, including the aggregates. Note that the select will either have columns from the groupby, or will have aggregate
      values. Aggregate values help you decide what value from the group gets put into the tuple! */
      
      