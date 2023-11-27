
USE teamsweetdreams_dms;

-- populate the Colors table
INSERT INTO teamsweetdreams_dms.Colors(color_id, hexcode, color_name, description, inUse) 
	VALUES (1, 'ed5050', 'Red1', 'Used for upper management.', 1);
INSERT INTO teamsweetdreams_dms.Colors(color_id, hexcode, color_name, description, inUse) 
	VALUES (2, 'c18007', 'Orange1', 'Used for New Hires.', 1);
INSERT INTO teamsweetdreams_dms.Colors(color_id, hexcode, color_name, description, inUse) 
	VALUES (3, 'ead748', 'Yellow1', 'Used to denote Meetings.', 0);
INSERT INTO teamsweetdreams_dms.Colors(color_id, hexcode, color_name, description, inUse) 
	VALUES (4, 'c18007', 'Green1', NULL, 1);
INSERT INTO teamsweetdreams_dms.Colors(color_id, hexcode, color_name, description, inUse) 
	VALUES (5, '4285d1', 'Blueeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', 'Used for New Hires.', 1); -- a color name with 45 characters
INSERT INTO teamsweetdreams_dms.Colors(color_id, hexcode, color_name, description, inUse) 
	VALUES (6, '6514b7', 'Purple1', 'Used for notes.', 1);
INSERT INTO teamsweetdreams_dms.Colors(color_id, hexcode, color_name, description, inUse) 
	VALUES (7, 'b2b2b2', 'Marist Gray', 'Official Marist Gray.', 1);
INSERT INTO teamsweetdreams_dms.Colors(color_id, hexcode, color_name, description, inUse) 
	VALUES (8, '2d9999', 'Jeff', 'Used for Jeff.', 1);
INSERT INTO teamsweetdreams_dms.Colors(color_id, hexcode, color_name, description, inUse) 
	VALUES (10, '2d9943', 'Poughkeepsie', 'Used for events in Poughkeepsie. weeeeeeeeee!', 1); -- a description with 45 characters
INSERT INTO teamsweetdreams_dms.Colors(color_id, hexcode, color_name, description, inUse) 
	VALUES (255, 'c8102e', 'Marist', 'Official Marist Red', 1);
 

INSERT INTO teamsweetdreams_dms.ActivityStatus(activity_id, name, description, last_assigned, color_id) 
	VALUES (1, 'Online', 'User is Online', '2023-11-08 06:32:05', 4);
INSERT INTO teamsweetdreams_dms.ActivityStatus(activity_id, name, description, last_assigned, color_id) 
	VALUES (2, 'Offline', 'User is Offline', '9999-12-31 11:13:00', 255); -- maximum date
INSERT INTO teamsweetdreams_dms.ActivityStatus(activity_id, name, description, last_assigned, color_id)
	VALUES (3, 'Idle', 'User is idle', '2010-02-28 21:04:00', 3);
INSERT INTO teamsweetdreams_dms.ActivityStatus(activity_id, name, description, last_assigned, color_id) 
	VALUES (4, 'Meeting', 'User is in a meeting', '2020-02-29 23:12:31', 4); -- leap year date
INSERT INTO teamsweetdreams_dms.ActivityStatus(activity_id, name, description, last_assigned, color_id) 
	VALUES (5, 'Away', 'User is away', '2023-11-08 23:59:59', 5); -- maximum time
INSERT INTO teamsweetdreams_dms.ActivityStatus(activity_id, name, description, last_assigned, color_id) 
	VALUES (6, 'lunch', 'User is on lunch', '2022-12-30 00:00:00', 6); -- minimum time
INSERT INTO teamsweetdreams_dms.ActivityStatus(activity_id, name, description, last_assigned, color_id) 
	VALUES (7, 'user has 45 characters 1 1 1 1 1 1 1 1 ! ! !!', 'This user has 45 characters 1 1 1 1 1 1 1 1 !', '2023-11-08 00:00:00', 7); -- maximum varchar length
INSERT INTO teamsweetdreams_dms.ActivityStatus(activity_id, name, description, last_assigned, color_id) 
	VALUES (20, 'Jeff', 'User is Jeff', '0000-01-01 01:40:02', 8); -- minimum date
INSERT INTO teamsweetdreams_dms.ActivityStatus(activity_id, name, description, last_assigned, color_id) 
	VALUES (10, 'Poughkeepsie', 'User is in Poughkeepsie', '2023-05-08 23:01:0', 4);
INSERT INTO teamsweetdreams_dms.ActivityStatus(activity_id, name, description, last_assigned, color_id) 
	VALUES (255, 'Time-Out', 'This user is in timeout.', '2023-04-07 00:00:00', 10);

-- Populate the Location table
INSERT INTO teamsweetdreams_dms.Location(place_id, address_ln_1, address_ln2, city, state, zip) 
	VALUES (1, '3399 North Road', 'Marist College MSC 11111', 'Poughkeepsie','New York', '12601'); -- minimum ID
INSERT INTO teamsweetdreams_dms.Location(place_id, address_ln_1, address_ln2, city, state, zip) 
	VALUES (2, '47 Essex Ave', NULL, 'Westford', 'MA', '01886');
INSERT INTO teamsweetdreams_dms.Location(place_id, address_ln_1, address_ln2, city, state, zip) 
	VALUES (3, NULL, 'C. Library', 'Poughkeepsie', 'New York', '12601');
INSERT INTO teamsweetdreams_dms.Location(place_id, address_ln_1, address_ln2, city, state, zip) 
	VALUES (4, 'Greystone', NULL, NULL, NULL, '54701');
INSERT INTO teamsweetdreams_dms.Location(place_id, address_ln_1, address_ln2, city, state, zip) 
	VALUES (5, 'The weird room outside the new guys office name starts with a J', 'Someone please confirm', 'Glendale', '', NULL); -- Maximum varchar length
INSERT INTO teamsweetdreams_dms.Location(place_id, address_ln_1, address_ln2, city, state, zip) 
	VALUES (6, '8724 Grant St.', NULL, 'Woodstock', 'Georgia', '01886');
INSERT INTO teamsweetdreams_dms.Location(place_id, address_ln_1, address_ln2, city, state, zip) 
	VALUES (7, 'Dining Hall', '', '', '', '');
INSERT INTO teamsweetdreams_dms.Location(place_id, address_ln_1, address_ln2, city, state, zip) 
	VALUES (8, '1600 Pennsylvania Ave', NULL, 'N.W.', 'Washington DC', '20500');
INSERT INTO teamsweetdreams_dms.Location(place_id, address_ln_1, address_ln2, city, state, zip) 
	VALUES (10, 'Arlington Street', 'Red Building Blue Fence', 'Los Banos', NULL, NULL);
INSERT INTO teamsweetdreams_dms.Location(place_id, address_ln_1, address_ln2, city, state, zip) 
	VALUES (255, 'Large Conference Room', NULL, NULL, NULL, NULL); -- maximum ID, NULL values
 
 
 -- Insert into statements for the 'PERMISSIONS' table:
INSERT INTO teamsweetdreams_dms.permissions (perm_id, perm_name, perm_description, perm_notes, enabled) VALUES 
 ('1', 'All', 'All permissions', 'Granted to role: HEAD ADMIN', 0);
INSERT INTO teamsweetdreams_dms.permissions (perm_id, perm_name, perm_description, perm_notes, enabled) VALUES  ('2', 'Alter', 'Grants the ability to alter tables', 'Granted to role: ADMIN', 0);
INSERT INTO teamsweetdreams_dms.permissions (perm_id, perm_name, perm_description, perm_notes, enabled) VALUES ('3', 'Create', 'Grants the ability to create tables', 'Granted to role: ADMIN', 1);
INSERT INTO teamsweetdreams_dms.permissions (perm_id, perm_name, perm_description, perm_notes, enabled) VALUES ('4', 'Drop', 'Grants the ability to drop tables', 'Granted to role: ADMIN, DELETER', 1);
INSERT INTO teamsweetdreams_dms.permissions (perm_id, perm_name, perm_description, perm_notes, enabled) VALUES ('5', 'Grant', 'Grants the ability to grant other users perissions', 'Granted to role: SUPERVISOR', 1);
INSERT INTO teamsweetdreams_dms.permissions (perm_id, perm_name, perm_description, perm_notes, enabled) VALUES ('6', 'Insert', 'Grants the ability to insert data into tables', 'Granted to role: ADMIN, INSERTER', 0);
INSERT INTO teamsweetdreams_dms.permissions (perm_id, perm_name, perm_description, perm_notes, enabled) VALUES ('7', 'Spectate', 'Grants the ability to view only', 'Granted to role: VIEWER', 1);
INSERT INTO teamsweetdreams_dms.permissions (perm_id, perm_name, perm_description, perm_notes, enabled) VALUES ('8', 'Recrute', 'Grants the ability to recrute', 'Granted to role: RECRUTER', 0);
INSERT INTO teamsweetdreams_dms.permissions (perm_id, perm_name, perm_description, perm_notes, enabled) VALUES ('9', 'Godly', 'Grants the ability to delete the entire workspace', 'Granted to role: GOD', 0);
INSERT INTO teamsweetdreams_dms.permissions (perm_id, perm_name, perm_description, perm_notes, enabled) VALUES ('10', 'Visitor', 'Grants the ability to have acces to a workspace for a short time', 'Granted to role: TEMPORARY', 1);

-- Insert into statements for the 'ROLES' table:
INSERT INTO teamsweetdreams_dms.roles (role_id, name, description, color_id, notes) VALUES 
 ('1', 'Head Admin', 'Gives all permissions to the user', 1, 'Used for the president of the company');
INSERT INTO teamsweetdreams_dms.roles (role_id, name, description, color_id, notes) VALUES ('2', 'Admin', 'Gives the roles of creating, deleting, changing tables and can edit the roles of others', 2, 'Used for higher level personell ');
INSERT INTO teamsweetdreams_dms.roles (role_id, name, description, color_id, notes) VALUES ('3', 'Viewer', 'Only allows the user to view data in and the colums of tables', 3, 'Used for personell who should only be able to view data');
INSERT INTO teamsweetdreams_dms.roles (role_id, name, description, color_id, notes) VALUES ('4', 'Inserter', 'Only allows the user to insert data into tables', 4, 'Used for personell who should only be able to insert data');
INSERT INTO teamsweetdreams_dms.roles (role_id, name, description, color_id, notes) VALUES ('5', 'Deleter', 'Only allows the user to delete data in tables', 5, 'Used for personell who should only be able to delete data');
INSERT INTO teamsweetdreams_dms.roles (role_id, name, description, color_id, notes) VALUES ('6', 'Supervisor', 'Allows for the user to change the permissions of users', 6, 'Used for managerial employees');
INSERT INTO teamsweetdreams_dms.roles (role_id, name, description, color_id, notes) VALUES ('7', 'Recruiter', 'Gives the user the ability to add new users to the workspace', 7, 'Used for recruiters');
INSERT INTO teamsweetdreams_dms.roles (role_id, name, description, color_id, notes) VALUES ('8', 'Restricted', 'Does not allow ANY permissions', 8, 'Used to restrict users from the database');
INSERT INTO teamsweetdreams_dms.roles (role_id, name, description, color_id, notes) VALUES ('9', 'God', 'Grants the God-like power to create and destroy the enteirey of a workspace', 10, 'Used for God-like users');
INSERT INTO teamsweetdreams_dms.roles (role_id, name, description, color_id, notes) VALUES ('10', 'Temporary', 'Gives the user \'Viewer\' permissions for one day', 255, 'Used for users who should only see the data for a short time');

 
 
-- Insert into statements for the 'USERS' table:
INSERT INTO teamsweetdreams_dms.users (user_id, fname, lname, username, password, activity_id, role_id, date_joined) VALUES 
 ('1', 'Connor', 'Fleischman', 'waytofaded', 'Toothfairy', 5, 3, '2023-11-08 00:00:00');
INSERT INTO teamsweetdreams_dms.users (user_id, fname, lname, username, password, activity_id, role_id, date_joined) VALUES ('2', 'Evan', 'Spillane', 'EvanSpillane', 'Password', 2, 4, '2023-11-08 00:00:00');
INSERT INTO teamsweetdreams_dms.users (user_id, fname, lname, username, password, activity_id, role_id, date_joined) VALUES ('3', 'Lilli', 'Cartiera', 'LilliCartiera', 'Google123', 255, 7, '2023-11-08 00:00:00');
INSERT INTO teamsweetdreams_dms.users (user_id, fname, lname, username, password, activity_id, role_id, date_joined) VALUES ('4', 'Abel', 'Scholl', 'AbelScholl', 'BehindU', 10, 10, '2023-11-08 00:00:00');
INSERT INTO teamsweetdreams_dms.users (user_id, fname, lname, username, password, activity_id, role_id, date_joined) VALUES ('5', 'Neo', 'Pi', 'NeoPi', 'ABCDEFG123', 6, 1, '2023-11-08 00:00:00');
INSERT INTO teamsweetdreams_dms.users (user_id, fname, lname, username, password, activity_id, role_id, date_joined) VALUES ('6', 'Saul', 'Goodman', 'BetterCallSaul', 'LyrsAreUs', 1, 1, '2023-11-08 00:00:00');
INSERT INTO teamsweetdreams_dms.users (user_id, fname, lname, username, password, activity_id, role_id, date_joined) VALUES ('7', 'Anakin', 'Skywalker', 'theChosenOne', 'Jedi4Life', 1, 3, '2023-11-08 00:00:00');
INSERT INTO teamsweetdreams_dms.users (user_id, fname, lname, username, password, activity_id, role_id, date_joined) VALUES ('8', 'Neo', 'Anderson', 'MAtrixHakr', '123CantHakME', 20, 4, '2023-11-08 00:00:00');
INSERT INTO teamsweetdreams_dms.users (user_id, fname, lname, username, password, activity_id, role_id, date_joined) VALUES ('9', 'Jesus', 'Christ', 'SonofGod', 'Heaven', 2, 7, '2023-11-08 00:00:00');
INSERT INTO teamsweetdreams_dms.users (user_id, fname, lname, username, password, activity_id, role_id, date_joined) VALUES ('10', 'Finn', 'TheHuman', 'FinnTheHuman', 'ILoveJake', 1, 6, '2023-11-08 00:00:00');

-- SET FOREIGN_KEY_CHECKS=0;

INSERT INTO teamsweetdreams_dms.Organizations (org_id, org_name, maxDiaries, creator_id, date_created) 
	VALUES (1, 'Public Relations', 65535, 1, '2023-11-08 06:32:05');
INSERT INTO teamsweetdreams_dms.Organizations (org_id, org_name, maxDiaries, creator_id, date_created) 
	VALUES (2, 'Marketing', 65535, 2, '2023-11-08 10:30:59');
INSERT INTO teamsweetdreams_dms.Organizations (org_id, org_name, maxDiaries, creator_id, date_created) 
	VALUES (3, 'Advisors', 65533, 1, '0000-01-01 00:00:00'); -- minimum datetime
INSERT INTO teamsweetdreams_dms.Organizations (org_id, org_name, maxDiaries, creator_id, date_created) 
	VALUES (4, 'CEO', 65535, 1, '2023-11-08 10:30:59');
INSERT INTO teamsweetdreams_dms.Organizations (org_id, org_name, maxDiaries, creator_id, date_created) 
	VALUES (5, 'Administrators', 0, 1, '2022-11-25 10:30:59');
INSERT INTO teamsweetdreams_dms.Organizations (org_id, org_name, maxDiaries, creator_id, date_created) 
	VALUES (6, 'Human Resources', 15563, 1, '2014-03-08 10:30:59');
INSERT INTO teamsweetdreams_dms.Organizations (org_id, org_name, maxDiaries, creator_id, date_created) 
	VALUES (7, 'Information Technology', 65535, 1, '2023-11-08 10:30:59');
INSERT INTO teamsweetdreams_dms.Organizations (org_id, org_name, maxDiaries, creator_id, date_created) 
	VALUES (8, 'Finance', 65535, 1, '2023-11-08 10:30:59');
INSERT INTO teamsweetdreams_dms.Organizations (org_id, org_name, maxDiaries, creator_id, date_created) 
	VALUES (9, 'Sales', 65535, 1, '2023-11-08 10:30:59');
INSERT INTO teamsweetdreams_dms.Organizations (org_id, org_name, maxDiaries, creator_id, date_created) 
	VALUES (255, 'Operations Management Executive Special Team', 65535, 1, '9999-12-31 23:59:59') -- maximum datetime, varchar, maxDiaries
 ;

-- SET FOREIGN_KEY_CHECKS=1;

-- Insert into statements for the 'ENTRYTYPES' table:
INSERT INTO teamsweetdreams_dms.entrytypes (entryType_id, name, description, notes, color_id) VALUES 
 ('1', 'Required', 'Everyone is required to attend', NULL, 1);
INSERT INTO teamsweetdreams_dms.entrytypes (entryType_id, name, description, notes, color_id) VALUES ('2', 'High priority', 'Attendance is highly recommend but not required', NULL, 2);
INSERT INTO teamsweetdreams_dms.entrytypes (entryType_id, name, description, notes, color_id) VALUES ('3', 'Priority', 'Attendance is recommended but not required', 'Use high/low priority for more pressing/ less important events', 3);
INSERT INTO teamsweetdreams_dms.entrytypes (entryType_id, name, description, notes, color_id) VALUES ('4', 'Optional', 'Attendance is optional', NULL, 4);
INSERT INTO teamsweetdreams_dms.entrytypes (entryType_id, name, description, notes, color_id) VALUES ('5', 'Special Event', 'Used for the least important entires', NULL, 5);
INSERT INTO teamsweetdreams_dms.entrytypes (entryType_id, name, description, notes, color_id) VALUES ('6', 'Away', 'Denote predetermined times away from the office', 'This type will not notify the user', 3);
INSERT INTO teamsweetdreams_dms.entrytypes (entryType_id, name, description, notes, color_id) VALUES ('7', 'Note', NULL, 'Leave a note to your team', 4);
INSERT INTO teamsweetdreams_dms.entrytypes (entryType_id, name, description, notes, color_id) VALUES ('8', 'Put-off', 'Used for entries whose event will be put-off until later', NULL, 5);
INSERT INTO teamsweetdreams_dms.entrytypes (entryType_id, name, description, notes, color_id) VALUES ('9', 'Heads-up', 'Used for reminding users about the entry ', NULL, 8);
INSERT INTO teamsweetdreams_dms.entrytypes (entryType_id, name, description, notes, color_id) VALUES ('10', 'Delete later', 'Used for entries which will be deleted later', NULL, 6);


-- Insert into statements for the 'DIARIES' table:
INSERT INTO teamSweetDreams_DMS.Diaries (diary_id, title, date_created, last_updated, subject, org_id, owner_id) VALUES 
('32766', 'Meetings', '2022-01-22', '2022-07-15', 'Manages departmental meeting times', 255, 3); 
INSERT INTO teamSweetDreams_DMS.Diaries (diary_id, title, date_created, last_updated, subject, org_id, owner_id) VALUES 
('1', 'Partners', '2022-07-04', '2022-08-03', 'Keeps track of business partners events', 9, 5);
INSERT INTO teamSweetDreams_DMS.Diaries (diary_id, title, date_created, last_updated, subject, org_id, owner_id) VALUES 
('32767', 'Catalog', '2020-11-11', '2022-09-21', 'Deals with current products on the market', 3, 4);
INSERT INTO teamSweetDreams_DMS.Diaries (diary_id, title, date_created, last_updated, subject, org_id, owner_id) VALUES 
('34', 'Inventory', '2021-12-31', '2022-10-10', 'Tracks what items are currently in stock and/or need restocking', 8, 7);
INSERT INTO teamSweetDreams_DMS.Diaries (diary_id, title, date_created, last_updated, subject, org_id, owner_id) VALUES 
('2347', 'Employees', '2021-10-10', '2022-11-29', 'Manages current employees, contains personal info', 3, 8);
INSERT INTO teamSweetDreams_DMS.Diaries (diary_id, title, date_created, last_updated, subject, org_id, owner_id) VALUES 
('1237', 'Feedback', '2021-10-10', '2022-12-14', 'Contains customer and employee survey feedback', 1, 1);
INSERT INTO teamSweetDreams_DMS.Diaries (diary_id, title, date_created, last_updated, subject, org_id, owner_id) VALUES 
('3498', 'Trends', '2020-02-29', '2023-01-07', 'Tracks crucial trends in company dealings', 2, 3);
INSERT INTO teamSweetDreams_DMS.Diaries (diary_id, title, date_created, last_updated, subject, org_id, owner_id) VALUES 
('2348', 'Events', '2022-06-15', '2023-02-18', 'Calendar for event planning', 5, 10);
INSERT INTO teamSweetDreams_DMS.Diaries (diary_id, title, date_created, last_updated, subject, org_id, owner_id) VALUES 
('2312', 'Campaigns', '2021-08-08', '2023-03-22', 'Holds info about various company campaigns and descriptions', 7, 2);
INSERT INTO teamSweetDreams_DMS.Diaries (diary_id, title, date_created, last_updated, subject, org_id, owner_id) VALUES 
('65535', 'Team', '2020-11-11', '2023-04-05', 'For teams to communicate with one another', 1, 3);


-- Insert into statements for the 'ENTRIES' table:
INSERT INTO teamsweetdreams_dms.entries (entry_id, entry_title, start_time, end_time, priority, description, entryType_id, owner_id, org_id, diary_id, location_id) VALUES
 ('1', 'Meeting with boss', '2023-11-10 08:23:14', '2023-11-11 01:23:45', '1', 'Have statistics ready', 2, 2, 2, 34, 2);
INSERT INTO teamsweetdreams_dms.entries (entry_id, entry_title, start_time, end_time, priority, description, entryType_id, owner_id, org_id, diary_id, location_id) VALUES
('2', 'Presentation on Q1', '2023-11-10 12:34:56', '2023-11-11 05:45:23', '2', 'Black tie', 1, 2, 3,1237, 5);
INSERT INTO teamsweetdreams_dms.entries (entry_id, entry_title, start_time, end_time, priority, description, entryType_id, owner_id, org_id, diary_id, location_id) VALUES
('3', 'Meeting with board', '2023-11-11 09:12:34', '2023-11-12 02:34:56', '1', 'With Brian Gormanly', 2, 4, 1, 1, 1);
INSERT INTO teamsweetdreams_dms.entries (entry_id, entry_title, start_time, end_time, priority, description, entryType_id, owner_id, org_id, diary_id, location_id) VALUES
('4', 'New York show', '2023-11-12 06:45:23', '2023-11-13 03:12:34', '3', NULL, 6, 3, 6, 2312, NULL);
INSERT INTO teamsweetdreams_dms.entries (entry_id, entry_title, start_time, end_time, priority, description, entryType_id, owner_id, org_id, diary_id, location_id) VALUES
('5', 'Meeting with Greg', '2023-11-12 11:23:45', '2023-11-13 08:23:14', '1', 'About Forged Signature', 10, 8, 4, 32766, NULL);
INSERT INTO teamsweetdreams_dms.entries (entry_id, entry_title, start_time, end_time, priority, description, entryType_id, owner_id, org_id, diary_id, location_id) VALUES
('6', 'Call with Washington', '2023-11-12 12:34:56', '2023-11-13 09:12:34', '4', NULL, 5, 4, 3, 32766, NULL);
INSERT INTO teamsweetdreams_dms.entries (entry_id, entry_title, start_time, end_time, priority, description, entryType_id, owner_id, org_id, diary_id, location_id) VALUES
('7', 'Presentation on Q2', '2023-11-13 05:45:23', '2023-11-14 06:45:23', '2', 'Providing an overview of this quarter\'s progress.', 8, 10, 255, 65535, 4);
INSERT INTO teamsweetdreams_dms.entries (entry_id, entry_title, start_time, end_time, priority, description, entryType_id, owner_id, org_id, diary_id, location_id) VALUES
('8', 'Meeting with Connor', '2023-11-14 01:23:45', '2023-11-14 11:23:45', '1', 'Connor\'s office', 3, 1, 7, 2312, NULL);
INSERT INTO teamsweetdreams_dms.entries (entry_id, entry_title, start_time, end_time, priority, description, entryType_id, owner_id, org_id, diary_id, location_id) VALUES
('9', 'Hong Kong show', '2023-11-14 08:23:14', '2023-11-15 02:34:56', '3', NULL, 4, 8, 1, 2348, 1);
INSERT INTO teamsweetdreams_dms.entries (entry_id, entry_title, start_time, end_time, priority, description, entryType_id, owner_id, org_id, diary_id, location_id) VALUES
('10', 'Great Job, Guys!', '2023-11-11 02:34:56', '2023-11-12 11:23:45', '1', 'Im so proud of everyone\'s work on Thursday. We nailed it! Lunch on me tomorrow!', 7, 9, 2, 2347, NULL);


-- Insert values into table RolePermissions
INSERT INTO teamsweetdreams_dms.RolePermissions (role_id, perm_id) 
VALUES (10, 10);
INSERT INTO teamsweetdreams_dms.RolePermissions (role_id, perm_id) 
VALUES (1, 1);
INSERT INTO teamsweetdreams_dms.RolePermissions (role_id, perm_id) 
VALUES (2, 8);
INSERT INTO teamsweetdreams_dms.RolePermissions (role_id, perm_id) 
VALUES (3, 2);
INSERT INTO teamsweetdreams_dms.RolePermissions (role_id, perm_id) 
VALUES (4, 7);
INSERT INTO teamsweetdreams_dms.RolePermissions (role_id, perm_id) 
VALUES (5, 8);
INSERT INTO teamsweetdreams_dms.RolePermissions (role_id, perm_id) 
VALUES (6, 5);
INSERT INTO teamsweetdreams_dms.RolePermissions (role_id, perm_id) 
VALUES (7, 5);
INSERT INTO teamsweetdreams_dms.RolePermissions (role_id, perm_id) 
VALUES (8, 4);
INSERT INTO teamsweetdreams_dms.RolePermissions (role_id, perm_id) 
VALUES (9, 7)
;


-- insert values into the OrganizationMembers table
INSERT INTO teamsweetdreams_dms.organizationmembers (user_id, org_id) 
VALUES (1, 2);
INSERT INTO teamsweetdreams_dms.organizationmembers (user_id, org_id) 
VALUES(1, 3);
INSERT INTO teamsweetdreams_dms.organizationmembers (user_id, org_id) 
VALUES(3, 1);
INSERT INTO teamsweetdreams_dms.organizationmembers (user_id, org_id) 
VALUES(1, 4);
INSERT INTO teamsweetdreams_dms.organizationmembers (user_id, org_id) 
VALUES(2, 2);
INSERT INTO teamsweetdreams_dms.organizationmembers (user_id, org_id) 
VALUES(3, 2);
INSERT INTO teamsweetdreams_dms.organizationmembers (user_id, org_id) 
VALUES(4, 2);
INSERT INTO teamsweetdreams_dms.organizationmembers (user_id, org_id) 
VALUES(4, 6);
INSERT INTO teamsweetdreams_dms.organizationmembers (user_id, org_id) 
VALUES(3, 7);
INSERT INTO teamsweetdreams_dms.organizationmembers (user_id, org_id) 
VALUES(5, 7)
;


-- Insert values into UserDiaries Table
INSERT INTO teamsweetdreams_dms.UserDiaries (user_id, diary_id) 
VALUES (10, 34);
INSERT INTO teamsweetdreams_dms.UserDiaries (user_id, diary_id) 
VALUES (1, 1237);
INSERT INTO teamsweetdreams_dms.UserDiaries (user_id, diary_id) 
VALUES (2, 2312);
INSERT INTO teamsweetdreams_dms.UserDiaries (user_id, diary_id) 
VALUES (3, 2312);
INSERT INTO teamsweetdreams_dms.UserDiaries (user_id, diary_id) 
VALUES (4, 2347);
INSERT INTO teamsweetdreams_dms.UserDiaries (user_id, diary_id) 
VALUES (5, 2348);
INSERT INTO teamsweetdreams_dms.UserDiaries (user_id, diary_id) 
VALUES (6, 65535);
INSERT INTO teamsweetdreams_dms.UserDiaries (user_id, diary_id) 
VALUES (7, 65535);
INSERT INTO teamsweetdreams_dms.UserDiaries (user_id, diary_id) 
VALUES (8, 34);
INSERT INTO teamsweetdreams_dms.UserDiaries (user_id, diary_id) 
VALUES (9, 32767)
;

-- Insert values into table UserPermissions
INSERT INTO teamsweetdreams_dms.userPermissions (user_id, perm_id) 
VALUES (10, 10);
INSERT INTO teamsweetdreams_dms.userPermissions (user_id, perm_id) 
VALUES (1, 1);
INSERT INTO teamsweetdreams_dms.userPermissions (user_id, perm_id) 
VALUES (2, 8);
INSERT INTO teamsweetdreams_dms.userPermissions (user_id, perm_id) 
VALUES (3, 2);
INSERT INTO teamsweetdreams_dms.userPermissions (user_id, perm_id) 
VALUES (4, 7);
INSERT INTO teamsweetdreams_dms.userPermissions (user_id, perm_id) 
VALUES (5, 8);
INSERT INTO teamsweetdreams_dms.userPermissions (user_id, perm_id) 
VALUES (6, 5);
INSERT INTO teamsweetdreams_dms.userPermissions (user_id, perm_id) 
VALUES (7, 5);
INSERT INTO teamsweetdreams_dms.userPermissions (user_id, perm_id) 
VALUES (8, 4);
INSERT INTO teamsweetdreams_dms.userPermissions (user_id, perm_id) 
VALUES (9, 7)
;


