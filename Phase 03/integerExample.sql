-- Comprehensive Example using all integer data types
-- -- The following code creates a table of all integer types, both signed and unsigned
-- -- in order to demonstrate the value ranges of each type.
CREATE TABLE IntegerExample (
	tinyIntsSigned TINYINT,
    tinyIntsUnsigned TINYINT UNSIGNED,
    smallIntsSigned SMALLINT,
    smallIntsUnsigned SMALLINT UNSIGNED,
    mediumIntsSigned MEDIUMINT,
    mediumIntsUnsigned MEDIUMINT UNSIGNED,
    intsSigned INT,
    intsUnsigned INT UNSIGNED,
    bigIntsSigned BIGINT,
    bigIntsUnsigned BIGINT UNSIGNED
);

-- insert upper bound values for each field.
INSERT INTO IntegerExample (tinyIntsSigned, tinyIntsUnsigned, smallIntsSigned, smallIntsUnsigned, 
mediumIntsSigned, mediumIntsUnsigned, intsSigned, intsUnsigned, bigIntsSigned, bigIntsUnsigned) 
    VALUES (127,255,32767,65535,8388607,16777215,2147483647,4294967295,9223372036854775807,18446744073709551615);
-- insert zero, a lower bound value for unsigned types and middle bound for signed types.
INSERT INTO IntegerExample (tinyIntsSigned, tinyIntsUnsigned, smallIntsSigned, smallIntsUnsigned, 
mediumIntsSigned, mediumIntsUnsigned, intsSigned, intsUnsigned, bigIntsSigned, bigIntsUnsigned) 
    VALUES (0,0,0,0,0,0,0,0,0,0);
-- insert lower bound values for signed types only (because negative values are out of range for unsigned types)
INSERT INTO IntegerExample (tinyIntsSigned, smallIntsSigned, mediumIntsSigned, intsSigned, bigIntsSigned) 
    VALUES (-128,-32768,-8388608,-2147483648,-9223372036854775808);
-- display all data in the IntegerExample table for a full list of value ranges per integer data type    
SELECT * FROM IntegerExample;

 DROP TABLE IntegerExample; -- used to delete the table if necessary for starting over
