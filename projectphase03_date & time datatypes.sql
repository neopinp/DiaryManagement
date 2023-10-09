-- Date and Time types 
-- -- Comprehensive Example using all DATE and TIME data types
-- -- Also uses Fractional Seconds and Auto-initialization and Auto-updating

use project_phase_03;
create table DATEandTIME (
	CurrentDATE DATE,
    CurrentTIME TIME,
    CurrentTIME6 TIME(6),
    CurrentTIME5 TIME(5),
    CurrentTIME4 TIME(4),
    CurrentTIME3 TIME(3),
    CurrentTIME2 TIME(2),
    CurrentTIME1 TIME(1),
    CurrentTIME0 TIME(0),
    CurrentYEAR YEAR,
    CurrentDATETIME DATETIME NOT NULL ON UPDATE CURRENT_TIMESTAMP,
    CurrentTIMESTAMP TIMESTAMP NULL ON UPDATE CURRENT_TIMESTAMP
);    

-- Signed DATE example
insert into DATEandTIME (CurrentDate, CurrentTIME, CurrentTIME6, CurrentTIME5, CurrentTIME4, CurrentTIME3, CurrentTIME2, CurrentTIME1, CurrentTIME0, CurrentYEAR, CurrentDATETIME, CurrentTIMESTAMP)
	values ('2023-10-09', '16:39:143665', '16:39:143665', '16:39:143665', '16:39:143665', '16:39:143665', '16:39:143665', '16:39:143665', '16:39:143665', '16:39:143665', NOW(),NOW());
    
-- drop table DATEandTIME;