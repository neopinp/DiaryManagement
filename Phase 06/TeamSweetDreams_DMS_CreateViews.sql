

-- creates a view merging all diaries, all associated entries, the name of the associated organization, and a user_id with access to it.
CREATE OR REPLACE VIEW DiaryInfoPgVW AS (
SELECT D.*, E.*, O.org_name, UD.user_id FROM Diaries D
LEFT JOIN Entries E ON E.entryDiary_id = D.diary_id
LEFT JOIN UserDiaries UD ON UD.diary_id = D.diary_id
LEFT JOIN Organizations O ON O.org_id = D.diaryOrg_id
ORDER BY D.diary_id
);

SELECT * FROM diaryinfopgvw;

-- creates a view merging all entries, their associated diary titles, and the fullname of the entry owner.
CREATE OR REPLACE VIEW EntryInfoPgVW AS (
SELECT E.*, fullname, D.title AS diary_title FROM Entries E
LEFT JOIN Diaries D ON D.diary_id = E.EntryDiary_id
LEFT JOIN Users U ON U.user_id = E.entryOwner_id
ORDER BY E.entry_id
);

SELECT * FROM EntryInfoPgVW;