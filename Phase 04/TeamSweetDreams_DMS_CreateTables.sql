-- -----------------------------------------------------
--  teamSweetDreams_DMS
-- -----------------------------------------------------

DROP DATABASE IF EXISTS teamSweetDreams_DMS;

-- -----------------------------------------------------
-- Create teamSweetDreams_DMS Database
-- -----------------------------------------------------
CREATE DATABASE IF NOT EXISTS teamSweetDreams_DMS;
USE teamSweetDreams_DMS;

-- -----------------------------------------------------
-- Create the Colors Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS teamSweetDreams_DMS.Colors;

CREATE TABLE IF NOT EXISTS teamSweetDreams_DMS.Colors(
  color_id TINYINT NOT NULL PRIMARY KEY,
  hexcode VARCHAR(6) NOT NULL,
  color_name VARCHAR(45) NULL,
  description VARCHAR(45) NULL,
  inUse TINYINT NOT NULL
 );

-- -----------------------------------------------------
-- Create the ActivityStatus Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS teamSweetDreams_DMS.ActivityStatus;

CREATE TABLE IF NOT EXISTS teamSweetDreams_DMS.ActivityStatus(
  activity_id TINYINT NOT NULL,
  name VARCHAR(45) NOT NULL,
  description VARCHAR(45) NULL,
  last_active DATETIME NOT NULL,
  color_id TINYINT,
  PRIMARY KEY (activity_id),
  FOREIGN KEY (color_id) REFERENCES teamSweetDreams_DMS.Colors (color_id)
 );

-- -----------------------------------------------------
-- Create Roles Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamSweetDreams_DMS.Roles;

CREATE TABLE IF NOT EXISTS  teamSweetDreams_DMS.Roles(
   role_id TINYINT NOT NULL,
   name VARCHAR(45) NULL,
   description VARCHAR(100) NULL,
   notes VARCHAR(100) NULL,
   color_id TINYINT NOT NULL,
   PRIMARY KEY (role_id),
   FOREIGN KEY (color_id) REFERENCES teamSweetDreams_DMS.Colors (color_id)
  );

-- -----------------------------------------------------
-- Create Users Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS teamSweetDreams_DMS.Users;

CREATE TABLE IF NOT EXISTS teamSweetDreams_DMS.Users ( 
   user_id TINYINT NOT NULL,
   fname VARCHAR(45) NOT NULL,
   mname VARCHAR(45) NULL,
   lname VARCHAR(45) NOT NULL,
   fullName VARCHAR(135) NOT NULL,
   username VARCHAR(45) NOT NULL,
   password VARCHAR(45) NOT NULL,
   date_joined DATETIME NOT NULL,
   activity_id TINYINT NOT NULL,
   role_id TINYINT NOT NULL,
   PRIMARY KEY (user_id),
   FOREIGN KEY (activity_id) REFERENCES teamSweetDreams_DMS.ActivityStatus (activity_id),
   FOREIGN KEY (role_id) REFERENCES teamSweetDreams_DMS.Roles (role_id)
   );

-- -----------------------------------------------------
-- Create Location Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS teamSweetDreams_DMS.Location;

CREATE TABLE IF NOT EXISTS teamSweetDreams_DMS.Location (
  place_id TINYINT NOT NULL,
  address_ln_1 VARCHAR(100) NULL,
  address_ln2 VARCHAR(100) NULL,
  city VARCHAR(45) NULL,
  state VARCHAR(45) NULL,
  zip SMALLINT NULL,
  PRIMARY KEY (place_id)
  );

-- -----------------------------------------------------
-- Table  teamSweetDreams_DMS.Organizations 
-- -----------------------------------------------------
DROP TABLE IF EXISTS teamSweetDreams_DMS.Organizations;

CREATE TABLE IF NOT EXISTS  teamSweetDreams_DMS.Organizations (
   org_id TINYINT NOT NULL,
   org_name VARCHAR(45) NULL,
   maxDiaries INT NOT NULL,
   creator_id TINYINT NOT NULL,
   date_created VARCHAR(45) NOT NULL,
   PRIMARY KEY (org_id),
   FOREIGN KEY (creator_id) REFERENCES teamSweetDreams_DMS.Users (user_id)
   );

-- -----------------------------------------------------
-- Create EntryTypes Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS teamSweetDreams_DMS.EntryTypes;

CREATE TABLE IF NOT EXISTS  teamSweetDreams_DMS.EntryTypes (
   entryType_id INT NOT NULL,
   name VARCHAR(45) NULL,
   description VARCHAR(100) NULL,
   notes VARCHAR(100) NULL, -- -------------------
   color_id TINYINT NOT NULL,
   PRIMARY KEY (entryType_id),
   FOREIGN KEY (color_id) REFERENCES teamSweetDreams_DMS.Colors (color_id)
   );

-- -----------------------------------------------------
-- Create Diaries Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamSweetDreams_DMS.Diaries;

CREATE TABLE IF NOT EXISTS  teamSweetDreams_DMS.Diaries (
   diary_id SMALLINT NOT NULL,
   title VARCHAR(45),
   date_created DATETIME NOT NULL,
   last_updated DATETIME NOT NULL,
   owner_id TINYINT NOT NULL,
   subject VARCHAR(100) NULL,
   org_id TINYINT NOT NULL,
   PRIMARY KEY (diary_id),
   FOREIGN KEY (org_id) REFERENCES teamSweetDreams_DMS.Organizations (org_id),
   FOREIGN KEY (owner_id) REFERENCES teamSweetDreams_DMS.Users (user_id)
   );

-- -----------------------------------------------------
-- Create Entries Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamSweetDreams_DMS.Entries;

CREATE TABLE IF NOT EXISTS  teamSweetDreams_DMS.Entries (
   entry_id INT NOT NULL,
   entry_title VARCHAR(45) NOT NULL,
   start_time DATETIME NOT NULL,
   end_time DATETIME NOT NULL,
   duration DATETIME NULL,
   priority TINYINT NULL,
   description VARCHAR(100) NULL,
   owner_id TINYINT NOT NULL,
   org_id TINYINT NOT NULL,
   location_id TINYINT NULL,
   entryType_id INT NOT NULL,
   diary_id SMALLINT NOT NULL,
   PRIMARY KEY (entry_id),
   FOREIGN KEY (owner_id) REFERENCES teamSweetDreams_DMS.Users (user_id),
   FOREIGN KEY (org_id) REFERENCES teamSweetDreams_DMS.Organizations (org_id),
   FOREIGN KEY (location_id) REFERENCES teamSweetDreams_DMS.Location (place_id),
   FOREIGN KEY (entryType_id) REFERENCES teamSweetDreams_DMS.EntryTypes (entryType_id),
   FOREIGN KEY (diary_id) REFERENCES teamSweetDreams_DMS.Diaries (diary_id)
   );

-- -----------------------------------------------------
-- Create Permissions Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamSweetDreams_DMS.Permissions;

CREATE TABLE IF NOT EXISTS  teamSweetDreams_DMS.Permissions (
   perm_id TINYINT NOT NULL,
   perm_name VARCHAR(45) NOT NULL,
   perm_description VARCHAR(100) NULL,
   perm_notes VARCHAR(100) NULL,
   enabled CHAR NULL DEFAULT 'F',
   PRIMARY KEY (perm_id)
  );

-- -----------------------------------------------------
-- Create RolePermissions Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamSweetDreams_DMS.RolePermissions;

CREATE TABLE IF NOT EXISTS  teamSweetDreams_DMS.RolePermissions (
   perm_id TINYINT NOT NULL,
   role_id TINYINT NOT NULL,
   FOREIGN KEY (perm_id) REFERENCES teamSweetDreams_DMS.Permissions (perm_id),
   FOREIGN KEY (role_id) REFERENCES teamSweetDreams_DMS.Roles (role_id)
   );

-- -----------------------------------------------------
-- Create OrganizationMembers Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamSweetDreams_DMS.OrganizationMembers;

CREATE TABLE IF NOT EXISTS  teamSweetDreams_DMS.OrganizationMembers (
   user_id TINYINT NOT NULL,
   org_id TINYINT NOT NULL,
   FOREIGN KEY (user_id) REFERENCES teamSweetDreams_DMS.Users (user_id),
   FOREIGN KEY (org_id) REFERENCES teamSweetDreams_DMS.Organizations (org_id)
   );

-- -----------------------------------------------------
-- Create UserDiaries Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamSweetDreams_DMS.UserDiaries;

CREATE TABLE IF NOT EXISTS  teamSweetDreams_DMS.UserDiaries (
   user_id TINYINT NOT NULL,
   diary_id SMALLINT NOT NULL,
   FOREIGN KEY (user_id) REFERENCES teamSweetDreams_DMS.Users (user_id),
   FOREIGN KEY (diary_id) REFERENCES teamSweetDreams_DMS.Diaries (diary_id)
   );

-- -----------------------------------------------------
-- Create UserPermissions Table
-- -----------------------------------------------------
DROP TABLE IF EXISTS  teamSweetDreams_DMS.userPermissions;

CREATE TABLE IF NOT EXISTS  teamSweetDreams_DMS.userPermissions (
   user_id TINYINT NOT NULL,
   perm_id TINYINT NOT NULL,
   FOREIGN KEY (user_id) REFERENCES teamSweetDreams_DMS.Users (user_id),
   FOREIGN KEY (perm_id) REFERENCES teamSweetDreams_DMS.Permissions (perm_id)
   );
