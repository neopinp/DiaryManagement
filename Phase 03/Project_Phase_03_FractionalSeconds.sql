-- Fractional Seconds 

-- This bit of code stops MySQL from truncating the fractional part of time
SET @@sql_mode = sys.list_add(
@@sql_mode, 'TIME_TRUNCATE_FRACTIONAL'
);

-- Creates a table showing a given time and rounding that time to a specified length
use project_phase_03;
Create table FractionalSeconds (
	CurrentTIME TIME,
    CurrentTIME6 TIME(6),
    CurrentTIME5 TIME(5),
    CurrentTIME4 TIME(4),
    CurrentTIME3 TIME(3),
    CurrentTIME2 TIME(2),
    CurrentTIME1 TIME(1),
    CurrentTIME0 TIME(0)
);

-- Inserts data into the generated table with each piece of data coresponding to its respective column
insert into FractionalSeconds (CurrentTIME, CurrentTIME6, CurrentTIME5, CurrentTIME4, CurrentTIME3, CurrentTIME2, CurrentTIME1, CurrentTIME0)
	values('16:39.143665', '16:39:55.143665', '16:39:55.143665', '16:39:55.143665', '16:39:55.143665', '16:39:55.143665', '16:39:55.143665', '16:39:55.143665');
    
-- Shows the table
select * from FractionalSeconds;

-- Removes the table (for reuseability)
-- drop table FractionalSeconds;
