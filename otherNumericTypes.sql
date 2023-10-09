-- The follwing code demonstrates the BIT, DECIMAL, FLOAT, DOUBLE, and REAL data types 
DROP TABLE IF EXISTS other_numeric_types;

-- create table
CREATE TABLE other_numeric_types
	( bit_type BIT,
	  decimal_type DECIMAL(10,2), #can also write DEC or FIXED
	  float_type FLOAT,
	  double_type DOUBLE,
      real_type REAL);

-- add values to each field 
INSERT INTO other_numeric_types (bit_type, decimal_type, float_type, double_type, real_type)
VALUES
    (0, 12345678.90, 3.141592, 1234567890123456.789, 2.7182818),
    (1, 0.01, 0.000001, 0.0000000000000001, 0.1234567);  

-- display table
SELECT * FROM other_numeric_types;
