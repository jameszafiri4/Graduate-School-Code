/* CSC6302 Database Principles
	Unit Three: Intermediate SQL
    Professor Minton
*/

-- We wrote some stored procedures and functions, so let's now call them. I highly recommened that you call a stored procedure in a new database
-- session (or a new tab in a MySQL Workbench, as every tab is a new session). Using a new session will ensure that the database engine knows
-- about the stored procedure and/or function. Recall what we learned about transactions and sessions. Changes to the database are not committed
-- by the database engine (and those not avaialable to call) until the end of the session.

-- How do we call a function? It works very much like the build in SQL functions. Recall:
SELECT TIME(ReleaseDate) 
FROM Console;

-- And remember the crucial thing: FUNCTIONS RETURN A SINGLE VALUE! And in this case, the function is run AFTER the select statement executes,
-- and is used to format the results within each row's ReleaseDate column.

-- Let's use our function: GetSeriesId. Make sure you have run the sql script "FunctionsStoredProceduresAndVariables_VideoGames" before proceeding.

-- We saw a function used in the where clause already
SELECT *
FROM Game
where Series = GetSeriesId("Sonic");

-- But we can use it in the select clause too, with a column value as input
SELECT GetSeriesId(SeriesName)
FROM Series;

-- That was pretty silly, because we could have just done this:
SELECT Id
FROM Series;

-- So let's use the other function we wrote
SELECT GameName, GetSeriesName(Id)
FROM Game;

-- That second column needs a better name
SELECT GameName, GetSeriesName(Series) as SeriesName
FROM Game;

-- We have some nulls, but the where clause happens before the select clause (and before the rename in the select clause,
-- so we cannot do this:

/*
SELECT GameName, GetSeriesName(Id) as SeriesName
FROM Game
WHERE SeriesName is not null;
*/

-- We need to check for nulls in the Series column instead. Which also shows when you pass a null into GetSeriesName
-- it returns null
SELECT GameName, Series, GetSeriesName(Series) as SeriesName
FROM Game
WHERE Series is not null;

-- We've some more functions in play, and we all know now that functions return a single value. Let's call a stored procedure, which returns
-- an entire relation:

call GetAllGames("Switch");

-- And we can also ask the database engine if the stored procedure exists, by calling the function we previously defined.
select doesProcedureExist("VideoGameSystems", "GetAllGames");



