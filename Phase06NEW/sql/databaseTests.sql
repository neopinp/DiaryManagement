-- This file has been used for testing database queries, views, procedures, etc.

USE teamsweetdreams_dms;

-- creates a view merging all diaries, all associated entries, the name of the associated organization, and a user_id with access to it.
-- This view merges multiple tables using a left Join, and is nonupdatable as a result.
CREATE OR REPLACE VIEW DiaryInfoPgVW AS (
SELECT D.*, E.*, O.org_name, UD.user_id, U.fullname FROM Diaries D
LEFT JOIN Entries E ON E.entryDiary_id = D.diary_id
LEFT JOIN UserDiaries UD ON UD.diary_id = D.diary_id
LEFT JOIN Organizations O ON O.org_id = D.diaryOrg_id
LEFT JOIN Users U ON U.user_id = UD.user_id
ORDER BY D.diary_id
);

SELECT diary_id, title, user_id, fullname FROM DiaryInfoPgVW;

DELETE FROM diaries WHERE diary_id="32778";

SELECT * FROM Organizations order by org_name;
SELECT * FROM Diaries;


SELECT DISTINCT diary_id, title, user_id, fullname, org_name FROM diaryinfopgvw WHERE org_name="Public Relations" AND title!="Feedback";


SELECT DISTINCT DI.diary_id, DI.user_id, DI.org_name FROM diaryinfopgvw DI
RIGHT JOIN UserDiaries UD ON UD.diary_id=DI.diary_id
ORDER BY DI.org_name
;

SELECT * FROM UserDiaries;

-- creates a view merging all entries, their locations, their associated diary titles, and the fullname of the entry owner.
-- This view merges multiple tables using a left Join, and is nonupdatable as a result.
CREATE OR REPLACE VIEW EntryInfoPgVW AS (
SELECT E.*, L.*, fullname, D.title AS diary_title FROM Entries E
LEFT JOIN Diaries D ON D.diary_id = E.EntryDiary_id
LEFT JOIN Users U ON U.user_id = E.entryOwner_id
LEFT JOIN Location L ON L.place_id = E.location_id
ORDER BY E.entry_id
);

SELECT * FROM EntryInfoPgVW ORDER BY priority DESC;
alter view EntryInfoPgVW convert to character set utf8mb3 collate utf8mb3_unicode_ci;

DELETE FROM Entries WHERE entry_id=16;


SELECT location_id, address_ln_1, address_ln2, city, state, zip 
FROM EntryInfoPgVW WHERE address_ln_1 LIKE '%E%' OR address_ln2 LIKE '%E%' 
OR city LIKE '%E%' OR state LIKE '%E%' OR zip LIKE '%E%';

SELECT entry_title, start_time FROM EntryInfoPgVW WHERE start_time LIKE '2023-11-10%';
SELECT entry_title, start_time FROM EntryInfoPgVW WHERE start_time LIKE '%01:23:45';
SELECT entry_title, start_time FROM EntryInfoPgVW WHERE entry_title LIKE 'Meeting with Connor%';
SELECT entry_title, start_time address_ln_1, address_ln2 FROM EntryInfoPgVW 
	WHERE CONCAT(address_ln_1, " ", address_ln2, " ", city, " ", state, " ", zip) LIKE '%47%';

SELECT CONCAT(address_ln_1, " ", address_ln2, " ", city, " ", state, " ", zip) EntryInfoPgVW WHERE entry_id = 1;

SELECT diary_id, subject, owner_id FROM diaryinfopgvw WHERE title='Feedback' AND diaryOrg_id = 1;
INSERT INTO UserDiaries (user_id, diary_id) VALUES (1, (SELECT MAX(LAST_INSERT_ID()) FROM Diaries));
INSERT INTO Diaries (title, date_created, last_updated, owner_id, subject, diaryOrg_id)
            VALUES("Sample", "2023-11-20", "2023-11-20", 1, "bhjfbhjdfhf", 1);

DROP PROCEDURE hashPwd;

DELIMITER //
CREATE PROCEDURE hashPwd(in pwd VARCHAR(45))
BEGIN
	DECLARE newpwd VARCHAR(40);
    SELECT SHA1(password) INTO newpwd FROM teamsweetdreams_dms.Users WHERE password=pwd;
    SELECT newpwd;
END //

DELIMITER ;

CALL hashPwd('ToothFairy');            
            
DROP PROCEDURE verifyCredentials;

DELIMITER //
CREATE PROCEDURE verifyCredentials(in uname VARCHAR(45), in pwd VARCHAR(45))
BEGIN
	DECLARE hashpwd VARCHAR(40);
    SELECT password INTO hashpwd FROM teamsweetdreams_dms.Users WHERE password=SHA1(pwd) and username=uname;
    SELECT CASE WHEN hashpwd IS NOT NULL THEN (SELECT user_id FROM teamsweetdreams_dms.Users WHERE password=hashpwd and username=uname) ELSE NULL END AS uID;
END //

DELIMITER ;

UPDATE teamsweetdreams_dms.Users SET password=SHA1(password) WHERE user_id=1;
UPDATE teamsweetdreams_dms.Users SET password=SHA1(password) WHERE user_id=2;
UPDATE teamsweetdreams_dms.Users SET password=SHA1(password) WHERE user_id=3;
UPDATE teamsweetdreams_dms.Users SET password=SHA1(password) WHERE user_id=4;
UPDATE teamsweetdreams_dms.Users SET password=SHA1(password) WHERE user_id=5;
UPDATE teamsweetdreams_dms.Users SET password=SHA1(password) WHERE user_id=6;
UPDATE teamsweetdreams_dms.Users SET password=SHA1(password) WHERE user_id=7;
UPDATE teamsweetdreams_dms.Users SET password=SHA1(password) WHERE user_id=8;
UPDATE teamsweetdreams_dms.Users SET password=SHA1(password) WHERE user_id=9;
UPDATE teamsweetdreams_dms.Users SET password=SHA1(password) WHERE user_id=10;
SELECT * FROM Users;