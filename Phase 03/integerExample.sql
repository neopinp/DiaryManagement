
-- Integer types example using TINYINT

CREATE TABLE TinyIntExample (
	tinyIntsSigned TINYINT,
    tinyIntsUnsigned TINYINT UNSIGNED
);
-- Signed TINYINT Example
INSERT INTO TinyIntExample (tinyIntsSigned) VALUES (0), (127), (-128); -- max values within range limits
INSERT INTO TinyIntExample (tinyIntsSigned) VALUES (128); -- Out of Range Value
INSERT INTO TinyIntExample (tinyIntsSigned) VALUES (-129); -- Out of Range Value
SELECT tinyIntsSigned FROM TinyIntExample WHERE tinyIntsSigned IS NOT NULL;

-- Unsigned TINYINT Example
INSERT INTO TinyIntExample (tinyIntsUnsigned) VALUES (0), (255); -- max values within range limits
INSERT INTO TinyIntExample (tinyIntsUnsigned) VALUES (-1); -- Out of Range Value
INSERT INTO TinyIntExample (tinyIntsUnsigned) VALUES (256); -- Out of Range Value
SELECT tinyIntsUnsigned FROM TinyIntExample WHERE tinyIntsUnsigned IS NOT NULL;

 DROP TABLE TinyIntExample;




-- Comprehensive Example using all integer data types
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

INSERT INTO IntegerExample (tinyIntsSigned, tinyIntsUnsigned, smallIntsSigned, smallIntsUnsigned, mediumIntsSigned, mediumIntsUnsigned, intsSigned, intsUnsigned, bigIntsSigned, bigIntsUnsigned) 
    VALUES (127,255,32767,65535,8388607,16777215,2147483647,4294967295,9223372036854775807,18446744073709551615);
INSERT INTO IntegerExample (tinyIntsSigned, tinyIntsUnsigned, smallIntsSigned, smallIntsUnsigned, mediumIntsSigned, mediumIntsUnsigned, intsSigned, intsUnsigned, bigIntsSigned, bigIntsUnsigned) 
    VALUES (0,0,0,0,0,0,0,0,0,0);
INSERT INTO IntegerExample (tinyIntsSigned, smallIntsSigned, mediumIntsSigned, intsSigned, bigIntsSigned) 
    VALUES (-128,-32768,-8388608,-2147483648,-9223372036854775808);
    
SELECT * FROM IntegerExample;

 DROP TABLE IntegerExample;