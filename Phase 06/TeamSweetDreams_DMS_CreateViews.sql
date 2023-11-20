

-- creates a view merging all diaries, all associated entries, the name of the associated organization, and a user_id with access to it.
CREATE OR REPLACE VIEW DiaryInfoPgVW AS (
SELECT D.*, E.*, O.org_name, UD.user_id FROM Diaries D
LEFT JOIN Entries E ON E.entryDiary_id = D.diary_id
LEFT JOIN UserDiaries UD ON UD.diary_id = D.diary_id
LEFT JOIN Organizations O ON O.org_id = D.diaryOrg_id
ORDER BY D.diary_id
);

SELECT * FROM diaryinfopgvw;

-- creates a view merging all entries, their locations, their associated diary titles, and the fullname of the entry owner.
CREATE OR REPLACE VIEW EntryInfoPgVW AS (
SELECT E.*, L.*, fullname, D.title AS diary_title FROM Entries E
LEFT JOIN Diaries D ON D.diary_id = E.EntryDiary_id
LEFT JOIN Users U ON U.user_id = E.entryOwner_id
LEFT JOIN Location L ON L.place_id = E.location_id
ORDER BY E.entry_id
);

SELECT * FROM EntryInfoPgVW;

SELECT entry_title, start_time FROM EntryInfoPgVW WHERE start_time LIKE '2023-11-10%';
SELECT entry_title, start_time FROM EntryInfoPgVW WHERE start_time LIKE '%01:23:45';
SELECT entry_title, start_time FROM EntryInfoPgVW WHERE entry_title LIKE 'Meeting with Connor%';
SELECT entry_title, start_time FROM EntryInfoPgVW WHERE CONCAT(address_ln_1, " ", address_ln2, " ", city, " ", state, " ", zip) LIKE '%01:23:45';

SELECT CONCAT(address_ln_1, " ", address_ln2, " ", city, " ", state, " ", zip) EntryInfoPgVW WHERE entry_id = 1;

SELECT diary_id, subject, owner_id FROM diaryinfopgvw WHERE title='Feedback' AND diaryOrg_id = 1;
INSERT INTO UserDiaries (user_id, diary_id) VALUES (1, (SELECT MAX(LAST_INSERT_ID()) FROM Diaries));
INSERT INTO Diaries (title, date_created, last_updated, owner_id, subject, diaryOrg_id)
            VALUES("Sample", "2023-11-20", "2023-11-20", 1, "bhjfbhjdfhf", 1);
