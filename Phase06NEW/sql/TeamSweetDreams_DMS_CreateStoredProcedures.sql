-- The following defines procedures to be used for the TSW Diary Management System

-- The following procedure takes a plaintext username and password as parameters
-- and then checks to see if the credentials exist (hashed) in the database
-- If yes, select the user id. If not, return NULL
DELIMITER //
CREATE PROCEDURE verifyCredentials(in uname VARCHAR(45), in pwd VARCHAR(45))
BEGIN
	DECLARE hashpwd VARCHAR(40);
    SELECT password INTO hashpwd FROM teamsweetdreams_dms.Users WHERE password=SHA1(pwd) and username=uname;
    SELECT CASE WHEN hashpwd IS NOT NULL THEN (SELECT user_id FROM teamsweetdreams_dms.Users WHERE password=hashpwd and username=uname) ELSE NULL END AS uID;
END //

DELIMITER ;