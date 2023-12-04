-- -----------------------------------------------------
--  teamSweetDreams_DMS
-- -----------------------------------------------------

-- This file creates the views used by the TSW Diary Management System


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

-- creates a view merging all entries, their locations, their associated diary titles, and the fullname of the entry owner.
-- This view merges multiple tables using a left Join, and is nonupdatable as a result.
CREATE OR REPLACE VIEW EntryInfoPgVW AS (
SELECT E.*, L.*, fullname, D.title AS diary_title FROM Entries E
LEFT JOIN Diaries D ON D.diary_id = E.EntryDiary_id
LEFT JOIN Users U ON U.user_id = E.entryOwner_id
LEFT JOIN Location L ON L.place_id = E.location_id
ORDER BY E.entry_id
);