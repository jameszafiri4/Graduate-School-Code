/* CSC6302 Database Principles
	Unit Two: Basic SQL
    Professor Minton
*/

USE VideoGameSystems;

/* Deleting Tuples
The DELETE command works very much like the SELECT command. It is the last part of a query that is processed, 
so you are free to make your deletes as complicated or as simple as you want. You can delete all the rows in a single
table. You can delete some, by specifying a predicate in WHERE clause. Or you can even use a nested subquery to
create a more complicated delete predicate. Note that you do not specify columns. Delete always deletes an entire row */

-- Note you might get an error if run this, because the database engine has "safe mode" which is meant to prevent you from
-- deleting without a where clause. Follow the directions in MySQL Workbench's error message to fix this configuration issue if needed.
DELETE
FROM Console;

DELETE 
FROM Console
WHERE ReleaseDate > '2005-11-02';

/* Updating rows
Often, our data has incorrect data. Perhaps there is a typo, or maybe there is a column that accepts null, and I now have the valid data. How
do we update the data? The UPDATE command allows us to query a table and apply predicates to make this process very simple. */

UPDATE Console
SET ConsoleName = 'DS'
WHERE ConsoleName = 'Nintendo DS';

/* Notice ConsoleName is used as a foreign key! Why did this pass! If you look back at the table definition file, you will notice this
	foreign key is configured to cascade update and cascade delete. Which means when we update ConsoleName in Console, the database
	engine knows to go and update the Game table as well, all with a single SQL command!


/* WITH Clause 
A view is a great way to save a query that is used a lot, to help speed up performance. It caches the query and anyone can use it. With allows us to just 
name a query something, to clean up our immediate code. No need to worry about others using this query, we just are going for readability. 
Here's a simple example, but keep in mind this temporary relation can be used exactly like any other table...but only until you go out scope. 
It's not available to the whole database like a view: its just available to the next query */

WITH Yoshi AS (SELECT * FROM GAME WHERE GameName like "%Yoshi%")
SELECT * FROM Yoshi ;