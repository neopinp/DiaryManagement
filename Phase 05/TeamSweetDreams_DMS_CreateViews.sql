-- The following document creates the required views for our pages

-- Create few for Main Page
-- get: full name, activity status, user role, user permissions, all organization info, organization members, and diaries.
DROP VIEW MainPageVW;
CREATE VIEW MainPageVW AS (
SELECT fullname, A.name AS 'Activity Status', perm_name, R.name AS Role, O.*, D.title FROM Users U
JOIN UserPermissions UP ON UP.user_id = U.user_id
JOIN Permissions P ON P.perm_id = UP.perm_id
JOIN RolePermissions RP ON RP.perm_id = P.perm_id
JOIN Roles R ON R.role_id=RP.role_id
JOIN organizationMembers OM ON OM.user_id=U.user_id
JOIN Organizations O ON O.org_id=OM.org_id
JOIN Diaries D ON D.diaryOrg_id=O.org_id
ORDER BY U.user_id
);
SELECT * from MainPageVw;

-- Create few for Diaries Page
-- get: full name, user role, user permissions, activity status, all organization info, organization members, diaries, entries, entry types, and locations.
DROP VIEW DiariesPageVW;
CREATE VIEW DiariesPageVW AS (
SELECT fullname, A.name AS 'Activity Status', perm_name, R.name AS Role, O.org_name, D.*, E.*, L.* FROM Users U
JOIN UserPermissions UP ON UP.user_id = U.user_id
JOIN Permissions P ON P.perm_id = UP.perm_id
JOIN RolePermissions RP ON RP.perm_id = P.perm_id
JOIN Roles R ON R.role_id=RP.role_id
JOIN organizationMembers OM ON OM.user_id=U.user_id
JOIN Organizations O ON O.org_id=OM.org_id
JOIN Diaries D ON D.diaryOrg_id=O.org_id
JOIN Entries E ON E.entryDiary_id=D.diary_id
JOIN EntryTypes ET ON ET.entryType_id=E.entryType_id
JOIN Location L ON L.place_id=E.location_id
JOIN ActivityStatus A ON A.activity_id=U.activity_id
ORDER BY U.user_id
);
SELECT * from DiariesPageVW;

-- Create few for Settings Page
-- get: full name, user role, user permissions, activity status, Organization names, and organization members.
DROP VIEW SettingsPageVW;
CREATE VIEW SettingsPageVW AS (
SELECT fullname, A.name AS 'Activity Status', perm_name, R.name AS 'Role', O.org_name FROM Users U
JOIN UserPermissions UP ON UP.user_id = U.user_id
JOIN Permissions P ON P.perm_id = UP.perm_id
JOIN RolePermissions RP ON RP.perm_id = P.perm_id
JOIN Roles R ON R.role_id=RP.role_id
JOIN organizationMembers OM ON OM.user_id=U.user_id
JOIN Organizations O ON O.org_id=OM.org_id
JOIN ActivityStatus A ON A.activity_id=U.activity_id
ORDER BY U.user_id
);
SELECT * from SettingsPageVW;

-- Create few for EditRoles Page
-- get: full name, user role, user permissions
DROP VIEW EditRolesVW;
CREATE VIEW EditRolesVW AS (
SELECT fullname, perm_name, R.name AS 'Role' FROM Users U
JOIN UserPermissions UP ON UP.user_id = U.user_id
JOIN Permissions P ON P.perm_id = UP.perm_id
JOIN RolePermissions RP ON RP.perm_id = P.perm_id
JOIN Roles R ON R.role_id=RP.role_id
ORDER BY R.role_id
);
SELECT * from EditRolesVW;


