-- The following queries are used to test the database's structure.

-- show all colors' information whose hexcode has a 9 in it.
SELECT * FROM teamsweetdreams_dms.Colors wHERE hexcode LIKE '%9%';

-- show the name of each color and what activity status it is assigned to.
SELECT C.color_name, activity_id
FROM Colors C
LEFT JOIN ActivityStatus A ON A.color_id=C.color_id
ORDER BY C.color_id;

-- Show the address of all places with a specified city
SELECT address_ln_1, address_ln_2  FROM teamsweetdreams_dms.Location WHERE city IS NOT NULL OR '';

-- show the person who was the online most recently.
SELECT U.fullname, A.last_assigned
FROM Users U
LEFT JOIN ActivityStatus A ON A.activity_id=U.activity_id WHERE A.name='Online'
ORDER BY A.last_assigned DESC LIMIT 1;

-- show how many organizations each user has created
SELECT COUNT(org_id), fullname FROM teamsweetdreams_dms.Organizations O
RIGHT JOIN Users U ON U.user_id=O.creator_id
GROUP BY fullname;

-- show the name of any person whose password is 8 characters or less
SELECT fullname FROM teamsweetdreams_dms.users WHERE LENGTH(password) <= 8 ;

-- Select all entries that are of type 'Note'
SELECT entry_title, entryType_id FROM Entries WHERE entryType_id = (SELECT entryType_id FROM teamsweetdreams_dms.entrytypes WHERE name = 'Note');

-- Retreive the names of people in the company and the permissions they have assigned to them.
SELECT name, perm_name FROM Roles R
RIGHT JOIN RolePermissions RP ON RP.role_id = R.role_id
RIGHT JOIN Permissions P ON P.perm_id = RP.perm_id
ORDER BY R.role_id;

-- Retrieve the names of people in the company and the organizations they are a part of.
SELECT fullname, org_name FROM Users U
INNER JOIN organizationmembers OM ON OM.user_id = U.user_id
INNER JOIN Organizations O ON O.org_id = OM.org_id
ORDER BY U.user_id;

-- Retrieve the names of people in the company and the diaries they have access to.
SELECT fullname, title FROM Users U
JOIN UserDiaries UD ON UD.user_id = U.user_id
JOIN Diaries D ON D.diary_id = UD.diary_id
ORDER BY D.diary_id;

-- Retreive the names of people in the company and the permissions they have assigned to them.
SELECT fullname, perm_name FROM Users U
JOIN UserPermissions UP ON UP.user_id = U.user_id
JOIN Permissions P ON P.perm_id = UP.perm_id
ORDER BY U.user_id;
