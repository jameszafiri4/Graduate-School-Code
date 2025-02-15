/* CSC6302 Database Principles
	Unit Three: Intermediate SQL
    Professor Minton
*/

-- Tell the database engine what database we are going to use   
    USE VideoGameSystems;
    
  /* A s you would expect from a programming language, SQL has built in functions that you can call in your queries. 
	There are a lot of options out there, and you can check the MySql documentation to see what's available,
    but let's take a look at a few */  
    
-- There are a number of functions related to formatting your output. Note that these are not aggregate functions, but apply to every result!

SELECT LOWER(ConsoleName)
FROM Console;

SELECT UPPER(ConsoleName)
FROM Console;

SELECT REVERSE(ConsoleName)
FROM Console;

-- A really useful collection of functions exists for dates and datetimes

SELECT CURRENT_TIME;

SELECT CURRENT_DATE;

SELECT CURRENT_TIMESTAMP;

SELECT MONTH(ReleaseDate), ConsoleName
FROM Console;

SELECT YEAR(ReleaseDate), ConsoleName
FROM Console;

SELECT DAY(ReleaseDate), ConsoleName
FROM Console;

SELECT TIME(ReleaseDate) 
FROM Console;

SELECT WEEK(ReleaseDate)
FROM Console;

SELECT Date_Add(ReleaseDate, INTERVAL 10 DAY)
FROM Console;

/* But, the truly useful thing about functions is that we can define our own */

-- All flavors of SQL have different syntax, let check ours:
  -- https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html
-- The syntax for Create Function is:
/* CREATE
    [DEFINER = user]
    FUNCTION [IF NOT EXISTS] sp_name ([func_parameter[,...]])
    RETURNS type
    [characteristic ...] routine_body */
    
delimiter $$
DROP FUNCTION IF EXISTS GetSeriesId$$
CREATE FUNCTION GetSeriesId (desiredSeriesName varchar(200)) RETURNS INT deterministic
BEGIN
	declare desiredId int;
	select distinct ID into desiredId
	FROM Series
	WHERE SeriesName = desiredSeriesName;
    return desiredId;
END$$

SELECT *
FROM Game
where Series = GetSeriesId("Animal Crossing");

-- But, what is delimiter? This is a keyword that tells the database engine that you would like to treat the next set of lines as an
 -- an entire statement. Generally, developers will pick $$ or // as their delimiter, as MySQL allows you define the characters used.
	-- Normally, when we are writing SQL code, we end each line with a semicolon. The semicolon is a delimter. We can change what
     -- delimiter we use, with the delimiter keyword. So, with stored procedures and functions, we want the engine to know that the whole definition is one
     -- thing, so we need to use a delimiter (same logic as why we always end in a semicolon) but we need to take into account the lines
     -- themselves use the ; delimiter. So we have to use something else.
     
     -- Let's write another one! We used the same delimiter, because why not
     delimiter $$
DROP FUNCTION IF EXISTS GetSeriesName$$
CREATE FUNCTION GetSeriesName (desiredSeriesId int) RETURNS VARCHAR(20) deterministic
BEGIN
	declare desiredSeriesName varchar(20);
	select distinct SeriesName into desiredSeriesName
	FROM Series
	WHERE Id = desiredSeriesId;
    return desiredSeriesName;
END$$
 
-- Notice that we cannot retun a whole set of data, only a particular value, which is why we needed to declare a variable in our function. But, what
-- if we wanted to return a whole set of data? Or nothing at all (maybe we just want to insert data or update it). That's where a stored procedure 
-- comes in!

-- Again, all flavors of SQL have their own syntax. Notice its very similar to functions
/* CREATE
    [DEFINER = user]
    PROCEDURE [IF NOT EXISTS] sp_name ([proc_parameter[,...]])
    [characteristic ...] routine_body */
    
    /* Batches, statements and delimiters: notice that I used the $$ to end the drop statement. We need to make sure that us done before we tried tio readd.
    We get issues if we use ;, because we haven't ended the statement yet, */
    
    delimiter $$
	DROP PROCEDURE IF EXISTS GetAllGames $$
    CREATE PROCEDURE GetAllGames (desiredConsoleName varchar(200))
    BEGIN
		SELECT * 
        FROM Game
        WHERE ConsoleName = desiredConsoleName;
    END; 
    $$
    delimiter ;
    
    call GetAllGames("Wii");
    
    
    /* Let's back up, as we have suddenly starting using variables, and we haven't talked about how they are defined and used. There
		are three types of variables:
			1. User Defined Variables. You can initialize them with the select or set commands, and there scope is the current session! */
            
            -- We can acess variables that are not defined, and we get null:
            SELECT @notDefined;
            
            -- We can actually declare and initialize:
            set @start=1;
			set @end=10;
            select @start;
			select @end;            
            select * from Series where Id between @start and @end;S
            select @middle := 5;
            select * from Series where Id between @start and @middle;
            
/*  2. Local variables, used in the scope of a function or stored procedure (so in a begin-end block). They need to be delcared. Recall our function did this: */

DROP FUNCTION IF EXISTS GetSeriesId;
delimiter $$
CREATE FUNCTION GetSeriesId (desiredSeriesName varchar(200)) RETURNS INT deterministic
BEGIN
	declare desiredId int;
	select distinct ID into desiredId
	FROM Series
	WHERE SeriesName = desiredSeriesName;
    return desiredId;
END$$
delimiter ;

    /* 3. System Variables are prefaced with @@. Their scope can be either global or session, or both. This is generaly not something you should be
      using, unless you are doing system admin type stuff. You can see all the system variables defined in the system using the command below: */
    show variables;
    
    /* Notice that we are starting to see SQL as a more expressive language. We have more and more tools to interact with our data:
     -- Views, which provide a way to cache a commonly requested query, and also a way to present to the user only what they care about
     -- With statement allows us to delcare a temporary relation, which is especially helpful at keeping nested subqueries from looking overwhelming
     -- We now have functions, allowing us to get a single piece of data quickly (and also caching the logic that did that for the engine to optimize)
     -- We can define our own functions, or use the built in ones that SQL has to offer. Great for string formatting and manipulating dates.
     -- We can declare variables, both as the input to a function and as a tool to use within the body of the expression (exactly like in Java)
     -- We can request an action from the database using a stored procedure. This is a great way to define exactly how your code interacts
		-- with your database, as you can pass in values and get tables of data back. This works great with program/SQL interfaces like JDBC and ADO */
        
	-- And one more thing! Its possible to ask the database engine what stored procedures and functions exist. This is the power of the system database,
    -- that stores all the needed metadata about all the other databases. We can query it like any other database:
    
    DELIMITER $$

DROP FUNCTION IF EXISTS doesProcedureExist;$$
CREATE FUNCTION doesProcedureExist(dbName VARCHAR(255), procedureName VARCHAR(255))
RETURNS BIT DETERMINISTIC
BEGIN
    SELECT COUNT(1) INTO @result
    FROM information_schema.ROUTINES as info
    WHERE info.ROUTINE_SCHEMA = dbName 
    AND info.ROUTINE_TYPE = 'PROCEDURE' 
    AND info.ROUTINE_NAME = procedureName;

    RETURN @result;

END;$$
