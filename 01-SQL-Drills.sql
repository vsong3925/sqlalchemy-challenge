-- SQL Drills

/* Question 01: Cartesian_Joins
- Part 1: What will be the number of rows in the output of the following query?
-select * from first_table, secound_table; */
-- Answer: 250 rows (25 x 10 = 250)

-- Part 2: What will the query Select * from table_one, table_two; look lik?
-- Answer: 
/* table_one.id will look like - 1, 1, 1; 2, 2, 2; 3, 3, 3; 4, 4, 4; 
   table_two.id will look like - 10, 11, 12; 10, 11, 12; 10, 11, 12; 10, 11, 12; */

/* Question 02: Foreign_Keys
- Based on the given table, reconstruct the table schema for employees and departments tables */
-- Answer
create table employees (
       employee_id serial,
	   first_name varchar,
	   last_name varchar,
       id integer);

create table departments (
       department_id serial,
	   dept_name);

/* Question 03: ACID
-- What are the ACID properties of SQL transactions? if possible, explain each property with an illustration of an example. */
/* Answer:
- Atomicity: Either all the operations (insert, update, delete) inside a transaction take place or none
- Consistency: the acid property will never leave the database in a hlaf-completed state
- Isolation: Every transaction is individual, and one transaction can't access the result of other transactions until the transaction completed
- Durability: once the transaction is successful completed, the changes will be permanent.
- Source and Examples: https://dotnettutorials.net/lesson/acid-properties-in-sql-server/ */

/* Question 04: Case
Change each animal's species to the correct species */
-- Answer:
create table animal_species (
       id serial,
       animal_name varchar,
       species varchar);

insert into animal_species (animal_name, species)
values
       ('Mickey Mouse', 'duck'),
	   ('Minnie Mouse', 'duck'),
	   ('Donald Duck', 'mouse');
	   
select * from animal_species

update animal_species
set species = 'mouse'
where animal_name like '%Mouse';

update animal_species
set species = 'duck'
where animal_name like '%Duck';

/* Qestion 05: Index
- Part 1: Explain an index in SQL
- Answer: An index can be used to efficiently find all rows matching some column in your query 
          and then walk through only that subset of the table to find exact matches. 
		  
- Part 2: What are the different types of index?
- Answer:
  - Clustered: alters the way that the rows are physically stored. 
               When you create a clustered index on a column (or a number of columns), 
			   the SQL server sorts the table’s rows by that column(s).
  - Non-clustered: creates a completely different object within the table, 
               that contains the column(s) selected for indexing and a pointer back to the table’s rows containing the data.
  - Source and Example: https://www.giantstride.gr/sql-indexing-part2/ */



