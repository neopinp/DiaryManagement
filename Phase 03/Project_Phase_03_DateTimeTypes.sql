-- Date and Time types and Auto-initialization/Auto-updating

-- Creates a table showing the given date, time, year, as well as the current DATETIME and TIMESTAMP
use project_phase_03;
create table DATEandTIME (
	CurrentDATE DATE,
    CurrentTIME TIME,
    CurrentYEAR YEAR,
    CurrentDATETIME DATETIME NOT NULL ON UPDATE CURRENT_TIMESTAMP,
    CurrentTIMESTAMP TIMESTAMP NULL ON UPDATE CURRENT_TIMESTAMP
);    

-- Inserts data into the generated table with each piece of data coresponding to its respective column
insert into DATEandTIME (CurrentDate, CurrentTIME, CurrentYEAR, CurrentDATETIME, CurrentTIMESTAMP)
	values ('2023-10-09', '16:39:55.143665', '2023', NOW(),NOW());

-- Shows the table
select * from DATEandTIME;

-- Removes the table (for reuseability)
-- drop table DATEandTIME;