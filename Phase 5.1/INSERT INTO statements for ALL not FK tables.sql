-- Insert into statements for the 'USERS' table:
INSERT INTO `teamsweetdreams_dms`.`users` (`user_id`, `fname`, `minit`, `lname`, `username`, `password`, `date_joined`) VALUES 
  ('1', 'Connor', 'M', 'Fleischman', 'waytofaded', 'Toothfairy', '2023-11-08 00:00:00')
, ('2', 'Evan', 'A', 'Spillane', 'EvanSpillane', 'Password', '2023-11-08 00:00:00')
, ('3', 'Lilli', 'A', 'Cartiera', 'LilliCartiera', 'Google123', '2023-11-08 00:00:00')
, ('4', 'Abel', 'A', 'Scholl', 'AbelScholl', 'BehindU', '2023-11-08 00:00:00')
, ('5', 'Neo', 'A', 'Pi', 'NeoPi', 'ABCDEFG123', '2023-11-08 00:00:00')
, ('6', 'Saul', 'P', 'Goodman', 'BetterCallSaul', 'LyrsAreUs', '2023-11-08 00:00:00')
, ('7', 'Anakin', 'A', 'Skywalker', 'theChosenOne', 'Jedi4Life', '2023-11-08 00:00:00')
, ('8', 'Neo', 'A', 'Anderson', 'MAtrixHakr', '123CantHakME', '2023-11-08 00:00:00')
, ('9', 'Jesus', 'H', 'Christ', 'SonofGod', 'Heaven', '2023-11-08 00:00:00')
, ('10', 'Finn', 'T', 'Human', 'FinnTheHuman', 'ILoveJake', '2023-11-08 00:00:00');

-- Insert into statements for the 'ROLES' table:
INSERT INTO `teamsweetdreams_dms`.`roles` (`role_id`, `name`, `description`, `notes`) VALUES 
  ('1', 'Head Admin', 'Gives all permissions to the user', 'Used for the president of the company')
, ('2', 'Admin', 'Gives the roles of creating, deleting, changing tables and can edit the roles of others', 'Used for higher level personell ')
, ('3', 'Viewer', 'Only allows the user to view data in and the colums of tables', 'Used for personell who should only be able to view data')
, ('4', 'Inserter', 'Only allows the user to insert data into tables', 'Used for personell who should only be able to insert data')
, ('5', 'Deleter', 'Only allows the user to delete data in tables', 'Used for personell who should only be able to delete data')
, ('6', 'Supervisor', 'Allows for the user to change the permissions of users', 'Used for managerial employees')
, ('7', 'Recruiter', 'Gives the user the ability to add new users to the workspace', 'Used for recruiters')
, ('8', 'Restricted', 'Does not allow ANY permissions', 'Used to restrict users from the database')
, ('9', 'God', 'Grants the God-like power to create and destroy the enteirey of a workspace', 'Used for God-like users')
, ('10', 'Temporary', 'Gives the user \'Viewer\' permissions for one day', 'Used for users who should only see the data for a short time');

-- Insert into statements for the 'PERMISSIONS' table:
INSERT INTO `teamsweetdreams_dms`.`permissions` (`perm_id`, `perm_name`, `perm_description`, `perm_notes`, `enabled`) VALUES 
  ('1', 'All', 'All permissions', 'Granted to role: HEAD ADMIN', 'Y')
, ('2', 'Alter', 'Grants the ability to alter tables', 'Granted to role: ADMIN', 'N')
, ('3', 'Create', 'Grants the ability to create tables', 'Granted to role: ADMIN', 'Y')
, ('4', 'Drop', 'Grants the ability to drop tables', 'Granted to role: ADMIN, DELETER', 'Y')
, ('5', 'Grant', 'Grants the ability to grant other users perissions', 'Granted to role: SUPERVISOR', 'Y')
, ('6', 'Insert', 'Grants the ability to insert data into tables', 'Granted to role: ADMIN, INSERTER', 'N')
, ('7', 'Spectate', 'Grants the ability to view only', 'Granted to role: VIEWER', 'Y')
, ('8', 'Recruite', 'Grants the ability to recruite', 'Granted to role: RECRUITER', 'N')
, ('9', 'Godly', 'Grants the ability to delete the entire workspace', 'Granted to role: GOD', 'N')
, ('10', 'Visitor', 'Grants the ability to have acces to a workspace for a short time', 'Granted to role: TEMPORARY', 'Y');

-- Insert into statements for the 'ENTRYTYPES' table:
INSERT INTO `teamsweetdreams_dms`.`entrytypes` (`entryType_id`, `name`, `description`, `notes`) VALUES 
  ('1', 'Highest priority', 'Used for the most important entries', null)
, ('2', 'High priority', 'Used for important but not urgent entries', null)
, ('3', 'Priority', 'Used for entries with medium importance', 'Use high/low priority for more pressing/ less important events')
, ('4', 'Low priority', 'Used for entries that are not as important', null)
, ('5', 'Lowest priority', 'Used for the least important entires', null)
, ('6', 'No priority', 'Used for entries with no importance ', 'This type will not notify the user')
, ('7', 'Immediate', 'Used for entries with immediate events', 'This type will notify the user')
, ('8', 'Put-off', 'Used for entries whose event will be put-off untill later', null)
, ('9', 'Heads-up', 'Used for reminding users about the entry ', null)
, ('10', 'Delete later', 'Used for entries which will be deleted later', null);

-- Insert into statements for the 'DIARIES' table:
INSERT INTO `teamSweetDreams_DMS`.`Diaries` (`diary_id`, `title`, `date_created`, `last_updated`, `subject`) VALUES 
('32766', 'Meetings', '2022-01-22', '2022-07-15', 'Manages meeting times'), 
('0', 'Partners', '2022-07-04', '2022-08-03', 'Keeps track of business partners'),
('32767', 'Catalog', '2020-11-11', '2022-09-21', 'Deals with current products on the market'),
('34', 'Inventory', '2021-12-31', '2022-10-10', 'Tracks what items are currently in stock and/or need restocking'),
('2347', 'Employees', '2021-10-10', '2022-11-29', 'Manages current employees, contains personal info'),
('1237', 'Feedback', '2021-10-10', '2022-12-14', 'Contains customer and employee survey feedback'),
('3498', 'Trends', '2020-02-29', '2023-01-07', 'Tracks crucial trends in company dealings'),
('2348', 'Events', '2022-06-15', '2023-02-18', 'Calendar for event planning'),
('2312', 'Campaigns', '2021-08-08', '2023-03-22', 'Holds info about various company campaigns and descriptions'),
('7469', 'Team', '2020-11-11', '2023-04-05',  'For teams to communicate with one another');

-- Insert into statements for the 'LOCATION' table:
INSERT INTO `teamSweetDreams_DMS`.`Location` (`place_id`, `address_ln_1`, `city`, `state`, `zip`) VALUES 
('01', '47 Essex Ave.', 'Westford', 'MA', '01886'),
('02', '69 Indian Spring St.', 'Fond Du Lac', 'WI', '54935'),
('03', '8724 Grant St.', 'Woodstock', 'GA', '54701'),
('04', '20 Greystone Lane', 'Eau Claire', 'WI', '54701'),
('05', '224 N. Queen St.', 'San Carlos', 'CA', '94070'),
('06', '9173 Clay Drive', 'Minneapolis', 'MN', '55406'),
('07', '4 Arlington St.', 'Los Banos', 'CA', '93635'),
('08', '33 Buttonwood Ave.', 'Southfield', 'MI', '48076'),
('09', '8635 East Glenlake St.', 'Des Plaines', 'IL', '60016'),
('10', '419 Glen Ridge Lane', 'Durham', 'NC', '27703');

-- Insert into statements for the 'COLORS' table:
INSERT INTO teamsweetdreams_dms.Colors(color_id, hexcode, color_name, description, inUse)
    VALUES (1, 'ed5050', 'Red1', 'Used for upper management.', 1)
	, (2, 'c18007', 'Orange1', 'Used for New Hires.', 1)
	, (3, 'ead748', 'Yellow1', 'Used to denote Meetings.', 0)
	, (4, 'c18007', 'Green1', Null, 1)
	, (5, '4285d1', 'Blueeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', 'Used for New Hires.', 1) -- a color name with 45 characters
	, (6, '6514b7', 'Purple1', 'Used for notes.', 1)
	, (7, 'b2b2b2', 'Marist Gray', 'Official Marist Gray.', 1)
	, (8, '2d9999', 'Jeff', 'Used for Jeff.', 1)
	, (9, '2d9943', 'Poughkeepsie', 'Used for events in Poughkeepsie. weeeeeeeeee!', 1) -- a description with 45 characters
	, (10, 'c8102e', 'Marist', 'Official Marist Red', 1);

-- Insert into statements for the 'ACTIVITYSTATUS' table:
INSERT INTO teamsweetdreams_dms.ActivityStatus(activity_id, name, description, last_active)
    VALUES (12, 'Online', 'User is Online', '2023-11-08 06:32:05')
	, (13, 'Offline', 'User is Offline', '9999-12-31 11:13:00') -- maximum date
	, (14, 'Idle', 'User is idle', '2010-02-28 21:04:00')
	, (4, 'Meeting', 'User is in a meeting', '2020-02-29 23:12:31') -- leap year date
	, (5, 'Away', 'User is away', '2023-11-08 23:59:59')  -- maximum time
	, (6, 'lunch', 'User is on lunch', '2022-12-30 00:00:00') -- minimum time
	, (7, 'user has 45 characters 1 1 1 1 1 1 1 1 ! ! !!', 'This user has 45 characters 1 1 1 1 1 1 1 1 !', '2023-11-08 00:00:00') -- maximum varchar length
	, (20, 'Jeff', 'User is Jeff', '0000-01-01 01:40:02') -- minimum date
	, (10, 'Poughkeepsie', 'User is in Poughkeepsie', '2023-05-08 23:01:0')
	, (1, 'Time-Out', 'This user is in timeout.', '2023-04-07 00:00:00');

-- Insert into statements for the 'ORGANIZATIONS' table:
INSERT INTO teamsweetdreams_dms.Organizations (org_id, org_name, maxDiaries, date_created)
    VALUES (1, 'Public Relations', 65535, '2023-11-08 06:32:05')
	, (2, 'Marketing', 65535, '2023-11-08 10:30:59')
	, (3, 'Advisors', 65533, '0000-01-01 00:00:00') -- minimum datetime
	, (4, 'CEO', 65535, '2023-11-08 10:30:59')
	, (5, 'Administrators', 0, '2022-11-25 10:30:59')
	, (6, 'Human Resources', 15563, '2014-03-08 10:30:59')
	, (7, 'Information Technology', 65535, '2023-11-08 10:30:59')
	, (8, 'Finance', 65535, '2023-11-08 10:30:59')
	, (9, 'Sales', 65535, '2023-11-08 10:30:59')
	, (10, 'Operations Management Executive Special Team', 65535, '9999-12-31 23:59:59') -- maximum datetime, varchar, maxDiaries
	;
    
-- Insert into statements for the 'ENTRIES' table:
INSERT INTO `teamsweetdreams_dms`.`entries` (`entry_id`, `entry_title`, `start_time`, `end_time`, `priority`, `description`) VALUES
  ('1', 'Meeting with boss', '2023-11-10 08:23:14', '2023-11-11 01:23:45', '1', 'Room 10302')
, ('2', 'Presentation on Q1', '2023-11-10 12:34:56', '2023-11-11 05:45:23', '2', 'Meeting room')
, ('3', 'Meeting with board', '2023-11-11 09:12:34', '2023-11-12 02:34:56', '1', 'Room 11002')
, ('4', 'New York show', '2023-11-12 06:45:23', '2023-11-13 03:12:34', '3', null)
, ('5', 'Meeting with supervisee', '2023-11-12 11:23:45', '2023-11-13 08:23:14', '1', 'Room 08006')
, ('6', 'Call with Washington', '2023-11-12 12:34:56', '2023-11-13 09:12:34', '4', null)
, ('7', 'Presentation on Q2', '2023-11-13 05:45:23', '2023-11-14 06:45:23', '2', 'Meeting room')
, ('8', 'Meeting with Connor', '2023-11-14 01:23:45', '2023-11-14 11:23:45', '1', 'Connor\'s office')
, ('9', 'Hong Kong show', '2023-11-14 08:23:14', '2023-11-15 02:34:56', '3', null)
, ('10', 'Meeting with trustees', '2023-11-11 02:34:56', '2023-11-12 11:23:45', '1', 'Board room');
