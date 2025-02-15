/* CSC6302 Database Principles
	Unit Three: Intermediate SQL
    Professor Minton
*/

-- As always, tell the database engine what database we are using
use VideoGameSystems;

-- Let's look at an outer join, and why its useful. My nephew has a birthday coming up, and I want to get him a video game. He's 6, so he
-- doesn't have a lot of games. But, I don't want to pick him out a game from a series. The last thing I need is him asking for every single 
-- Yoshi game ever made:
select *
from Game
where GameName like '%Yoshi%';

select * from Series

-- There are 19 games, and some of them are older then my brother in law. So, how do I pick a game that is not part of a series? Let's join
-- together the Game table and the Series table, and match them based on Series. And, let's go a step further, tell the database engine that
-- iif there is no match, just null out what is missing from the Game table. We know its the game table, because a right outer join always keeps
-- the data from the right table.
select *
from Game as g right outer join Series as s on g.Series=s.Id;

-- Which is actually just a silly rule to make things more readible, because this query does exactly the same thing. You could get through your 
-- career only writing right outer joins, or only writing left outer joins. And I'm fine with you picking whatever one makes the most sense to you
-- and sticking to it.
select *
from Series as s left outer join Game as g on g.Series=s.Id;

-- Just remember, this is not the same query! Run this query, and the two before, and make sure you see and understand the difference.
select *
from Game as g left outer join Series as s on g.Series=s.Id;

-- Let's go back to the original query, and its results. There are a lot of nulls. How can we use the nulls to solve the original question: what game does not have a series?
select *
from Game as g inner join Series as s on g.Series=s.Id
where g.GameName is not null;

-- Wait, that did not work. The result set is listing a bunch of games and their series. Animal Crossing is definitly a series! We want the games that don't have a series
select *
from Game as g right outer join Series as s on g.Series=s.Id
where s.SeriesName is null;

-- That did not return anything? What did we do wrong? Remember, this is right outer join, so there will always be data 
-- from the Series table. It will null out the columns from the Game table if there is no match. We want to be filtering based
-- on the Game table
select *
from Game as g right outer join Series as s on g.Series=s.Id
where g.Series is null;

-- Well, we got something, but we didn't get any games...only series. We want the games without a series! Wait a minute...we did the join backwards!
select *
from Game as g left outer join Series as s on g.Series=s.Id
where s.SeriesName is null;

-- Much better, but why are their Yoshi games? Apparently the Series field of the Yoshi games was never populated.
select *
from Game
where GameName like '%Yoshi%';

-- The Series table has the right data though!
select *
from Series;

/* I wonder what one of your homework questions will be :)

	This was a bit of an adventure, in terms of examples, as I led you astray a few times. Joins are pretty simple, once you understand them, so its important to play around with them
	see what can be done wrong. But let's stick to fully working examples now. */

-- What consoles do not have any Spryo games? Let's start by figuring out what consoles have a Spyro game:
select ConsoleName, GameName
from Game
where GameName like '%Spyro%';

-- I bet we could use the With Clause to help
With SpyroConsoles as
(
	select ConsoleName, GameName
	from Game
	where GameName like '%Spyro%'
)
select ConsoleName
from Console
where ConsoleName not in (select ConsoleName from SpyroConsoles);

-- That result set needs some work, let's order in reverse alphabetical order for fun:
With SpyroConsoles as
(
	select distinct ConsoleName
	from Game
	where GameName like '%Spyro%'
)
select distinct ConsoleName
from Console
where ConsoleName not in (select ConsoleName from SpyroConsoles)
order by ConsoleName desc;

-- Could we use a join instead of a nested subquery? Remember to use the information from the nulls!
With SpyroConsoles as
(
	select distinct ConsoleName, GameName
	from Game
	where GameName like '%Spyro%'
)
select distinct c.ConsoleName
from Console as c left outer join  SpyroConsoles s on c.ConsoleName=s.ConsoleName
where s.GameName is null
order by ConsoleName desc;