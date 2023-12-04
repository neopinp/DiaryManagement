-- -----------------------------------------------------
--  teamsweetdreams_dms
-- -----------------------------------------------------

DROP DATABASE IF EXISTS teamsweetdreams_dms;

-- -----------------------------------------------------
-- Create teamsweetdreams_dms Database
-- -----------------------------------------------------
CREATE DATABASE IF NOT EXISTS teamsweetdreams_dms;
USE teamsweetdreams_dms;

-- -----------------------------------------------------
-- Create the Colors Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS teamsweetdreams_dms.Colors;

CREATE TABLE IF NOT EXISTS teamsweetdreams_dms.Colors(
  color_id TINYINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
  hexcode VARCHAR(6) NOT NULL,
  color_name VARCHAR(45) NULL,
  description VARCHAR(45) NULL,
  inUse BOOLEAN NOT NULL
 );

-- -----------------------------------------------------
-- Create the ActivityStatus Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS teamsweetdreams_dms.ActivityStatus;

CREATE TABLE IF NOT EXISTS teamsweetdreams_dms.ActivityStatus(
  activity_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  description VARCHAR(45) NULL,
  last_assigned DATETIME NOT NULL,
  color_id TINYINT  UNSIGNED,
  PRIMARY KEY (activity_id),
  FOREIGN KEY (color_id) REFERENCES teamsweetdreams_dms.Colors (color_id)
 );

-- -----------------------------------------------------
-- Create Roles Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamsweetdreams_dms.Roles;

CREATE TABLE IF NOT EXISTS  teamsweetdreams_dms.Roles(
   role_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
   name VARCHAR(45) NULL,
   description VARCHAR(100) NULL,
   notes VARCHAR(100) NULL,
   color_id TINYINT UNSIGNED NOT NULL,
   PRIMARY KEY (role_id),
   FOREIGN KEY (color_id) REFERENCES teamsweetdreams_dms.Colors (color_id)
  );

-- -----------------------------------------------------
-- Create Users Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS teamsweetdreams_dms.Users;

CREATE TABLE IF NOT EXISTS teamsweetdreams_dms.Users ( 
   user_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
   fname VARCHAR(45) NOT NULL,
   lname VARCHAR(45) NOT NULL,
   fullName VARCHAR(135) GENERATED ALWAYS AS (concat(fname, ' ', lname)) STORED NOT NULL,
   username VARCHAR(45) NOT NULL,
   password VARCHAR(45) NOT NULL,
   date_joined DATETIME NOT NULL,
   activity_id TINYINT UNSIGNED NOT NULL,
   role_id TINYINT UNSIGNED NOT NULL,
   PRIMARY KEY (user_id),
   FOREIGN KEY (activity_id) REFERENCES teamsweetdreams_dms.ActivityStatus (activity_id),
   FOREIGN KEY (role_id) REFERENCES teamsweetdreams_dms.Roles (role_id)
   );

-- -----------------------------------------------------
-- Create Location Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS teamsweetdreams_dms.Location;

CREATE TABLE IF NOT EXISTS teamsweetdreams_dms.Location (
  place_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
  address_ln_1 VARCHAR(100) NULL,
  address_ln2 VARCHAR(100) NULL,
  city VARCHAR(45) NULL,
  state VARCHAR(45) NULL,
  zip VARCHAR(5) NULL,
  PRIMARY KEY (place_id)
  );

-- -----------------------------------------------------
-- Table  teamsweetdreams_dms.Organizations 
-- -----------------------------------------------------
DROP TABLE IF EXISTS teamsweetdreams_dms.Organizations;

CREATE TABLE IF NOT EXISTS  teamsweetdreams_dms.Organizations (
   org_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
   org_name VARCHAR(45) NULL,
   maxDiaries INT NOT NULL,
   creator_id TINYINT UNSIGNED NOT NULL,
   date_created DATETIME NOT NULL,
   PRIMARY KEY (org_id),
   FOREIGN KEY (creator_id) REFERENCES teamsweetdreams_dms.Users (user_id)
   );

-- -----------------------------------------------------
-- Create EntryTypes Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS teamsweetdreams_dms.EntryTypes;

CREATE TABLE IF NOT EXISTS  teamsweetdreams_dms.EntryTypes (
   entryType_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
   name VARCHAR(45) NULL,
   description VARCHAR(100) NULL,
   notes VARCHAR(100) NULL, -- -------------------
   color_id TINYINT UNSIGNED NOT NULL,
   PRIMARY KEY (entryType_id),
   FOREIGN KEY (color_id) REFERENCES teamsweetdreams_dms.Colors (color_id)
   );

-- -----------------------------------------------------
-- Create Diaries Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamsweetdreams_dms.Diaries;

CREATE TABLE IF NOT EXISTS  teamsweetdreams_dms.Diaries (
   diary_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
   title VARCHAR(45),
   date_created DATETIME NOT NULL,
   last_updated DATETIME NOT NULL,
   owner_id TINYINT UNSIGNED NOT NULL,
   subject VARCHAR(100) NULL,
   diaryOrg_id TINYINT UNSIGNED NOT NULL,
   PRIMARY KEY (diary_id),
   FOREIGN KEY (diaryOrg_id) REFERENCES teamsweetdreams_dms.Organizations (org_id),
   FOREIGN KEY (owner_id) REFERENCES teamsweetdreams_dms.Users (user_id)
   );

-- -----------------------------------------------------
-- Create Entries Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamsweetdreams_dms.Entries;

CREATE TABLE IF NOT EXISTS  teamsweetdreams_dms.Entries (
   entry_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
   entry_title VARCHAR(45) NOT NULL,
   start_time DATETIME NOT NULL,
   end_time DATETIME NOT NULL,
   duration DATETIME,
   priority TINYINT NULL,
   description VARCHAR(100) NULL,
   entryOwner_id TINYINT UNSIGNED NOT NULL,
   entryOrg_id TINYINT UNSIGNED NOT NULL,
   location_id TINYINT UNSIGNED NULL,
   entryType_id INT UNSIGNED NOT NULL,
   entryDiary_id SMALLINT UNSIGNED NOT NULL,
   PRIMARY KEY (entry_id),
   FOREIGN KEY (entryOwner_id) REFERENCES teamsweetdreams_dms.Users (user_id),
   FOREIGN KEY (entryOrg_id) REFERENCES teamsweetdreams_dms.Organizations (org_id),
   FOREIGN KEY (location_id) REFERENCES teamsweetdreams_dms.Location (place_id),
   FOREIGN KEY (entryType_id) REFERENCES teamsweetdreams_dms.EntryTypes (entryType_id),
   FOREIGN KEY (entryDiary_id) REFERENCES teamsweetdreams_dms.Diaries (diary_id)
   );

-- -----------------------------------------------------
-- Create Permissions Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamsweetdreams_dms.Permissions;

CREATE TABLE IF NOT EXISTS  teamsweetdreams_dms.Permissions (
   perm_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
   perm_name VARCHAR(45) NOT NULL,
   perm_description VARCHAR(100) NULL,
   perm_notes VARCHAR(100) NULL,
   enabled BOOLEAN NULL DEFAULT 0,
   PRIMARY KEY (perm_id)
  );

-- -----------------------------------------------------
-- Create RolePermissions Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamsweetdreams_dms.RolePermissions;

CREATE TABLE IF NOT EXISTS  teamsweetdreams_dms.RolePermissions (
   perm_id TINYINT UNSIGNED NOT NULL ,
   role_id TINYINT UNSIGNED NOT NULL,
   PRIMARY KEY (perm_id, role_id),
   FOREIGN KEY (perm_id) REFERENCES teamsweetdreams_dms.Permissions (perm_id) ON DELETE CASCADE, -- if id is deleted, will apply to related tables as well
   FOREIGN KEY (role_id) REFERENCES teamsweetdreams_dms.Roles (role_id) ON DELETE CASCADE
   );

-- -----------------------------------------------------
-- Create OrganizationMembers Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamsweetdreams_dms.OrganizationMembers;

CREATE TABLE IF NOT EXISTS  teamsweetdreams_dms.OrganizationMembers (
   user_id TINYINT UNSIGNED NOT NULL,
   org_id TINYINT UNSIGNED NOT NULL,
   PRIMARY KEY (user_id, org_id),
   FOREIGN KEY (user_id) REFERENCES teamsweetdreams_dms.Users (user_id) ON DELETE CASCADE,
   FOREIGN KEY (org_id) REFERENCES teamsweetdreams_dms.Organizations (org_id) ON DELETE CASCADE
   );

-- -----------------------------------------------------
-- Create UserDiaries Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamsweetdreams_dms.UserDiaries;

CREATE TABLE IF NOT EXISTS  teamsweetdreams_dms.UserDiaries (
   user_id TINYINT UNSIGNED NOT NULL,
   diary_id SMALLINT UNSIGNED NOT NULL,
   PRIMARY KEY (user_id, diary_id),
   FOREIGN KEY (user_id) REFERENCES teamsweetdreams_dms.Users (user_id) ON DELETE CASCADE,
   FOREIGN KEY (diary_id) REFERENCES teamsweetdreams_dms.Diaries (diary_id) ON DELETE CASCADE
   );

-- -----------------------------------------------------
-- Create UserPermissions Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamsweetdreams_dms.userPermissions;

CREATE TABLE IF NOT EXISTS  teamsweetdreams_dms.userPermissions (
   user_id TINYINT UNSIGNED NOT NULL,
   perm_id TINYINT UNSIGNED NOT NULL,
   PRIMARY KEY (user_id, perm_id),
   FOREIGN KEY (user_id) REFERENCES teamsweetdreams_dms.Users (user_id) ON DELETE CASCADE,
   FOREIGN KEY (perm_id) REFERENCES teamsweetdreams_dms.Permissions (perm_id) ON DELETE CASCADE
   );

