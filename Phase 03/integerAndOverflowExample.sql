-- Integer types and overflow example using TINYINT
-- The following code will create a table with two TINYINT fields, one signed and the other unsigned.
-- This example demonstrates the range of values that the TINYINT data type can hold
-- and MYSQL's way of dealing with results of out-of-range values.

CREATE TABLE TinyIntExample (
	tinyIntsSigned TINYINT,
    tinyIntsUnsigned TINYINT UNSIGNED
);
-- Signed TINYINT Example
INSERT INTO TinyIntExample (tinyIntsSigned) VALUES (0), (127), (-128); -- max values within range limits
-- These next two lines will throw errors, becasue the values being inserted are out of range.
INSERT INTO TinyIntExample (tinyIntsSigned) VALUES (128); -- Out of Range Value
INSERT INTO TinyIntExample (tinyIntsSigned) VALUES (-129); -- Out of Range Value

-- show all signed tinyint data in the table
SELECT tinyIntsSigned FROM TinyIntExample WHERE tinyIntsSigned IS NOT NULL;

-- Unsigned TINYINT Example
INSERT INTO TinyIntExample (tinyIntsUnsigned) VALUES (0), (255); -- max values within range limits
-- These next two lines will throw errors, becasue the values being inserted are out of range.
INSERT INTO TinyIntExample (tinyIntsUnsigned) VALUES (-1); -- Out of Range Value
INSERT INTO TinyIntExample (tinyIntsUnsigned) VALUES (256); -- Out of Range Value

-- show all unsigned tinyint data in the table
SELECT tinyIntsUnsigned FROM TinyIntExample WHERE tinyIntsUnsigned IS NOT NULL;

SET sql_mode = 'TRADITIONAL'; -- this line will enable Strict SQL mode
SET sql_mode = ''; -- this line will change the sql mode to unrestricted
SET sql_mode = 'NO_UNSIGNED_SUBTRACTION'; -- this line will change the sql mode to NO_UNSIGNED_SUBTRACTION

-- The result of the following line will be different depending on what mode is enabled.
-- Subtraction between signed and unsigned numbers is unsigned by default.
SELECT CAST(2 AS UNSIGNED) - 5; -- an unsigned value subtracted by a signed value with a negative result

 DROP TABLE TinyIntExample; -- used to delete the table if necessary for starting over
