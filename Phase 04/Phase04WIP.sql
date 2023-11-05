SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema teamSweetDreams_DMS
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `teamSweetDreams_DMS` ;

-- -----------------------------------------------------
-- Schema teamSweetDreams_DMS
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `teamSweetDreams_DMS` DEFAULT CHARACTER SET utf8 ;
USE `teamSweetDreams_DMS` ;

-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`Colors`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`Colors` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`Colors` (
  `color_id` INT NOT NULL,
  `hexcode` VARCHAR(45) NOT NULL,
  `color_name` VARCHAR(45) NULL,
  `description` VARCHAR(45) NULL,
  `inUse` TINYINT NOT NULL,
  PRIMARY KEY (`color_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`ActivityStatus`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`ActivityStatus` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`ActivityStatus` (
  `activity_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(45) NULL,
  `last_active` DATETIME NOT NULL,
  `color_id` INT NOT NULL,
  PRIMARY KEY (`activity_id`, `color_id`),
  INDEX `fk_ActivityStatus_colors1_idx` (`color_id` ASC) VISIBLE,
  CONSTRAINT `fk_ActivityStatus_colors1`
    FOREIGN KEY (`color_id`)
    REFERENCES `teamSweetDreams_DMS`.`Colors` (`color_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`Roles`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`Roles` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`Roles` (
  `role_id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `description` VARCHAR(45) NULL,
  `notes` VARCHAR(45) NULL,
  `color_id` INT NOT NULL,
  PRIMARY KEY (`role_id`, `color_id`),
  INDEX `fk_Roles_colors1_idx` (`color_id` ASC) VISIBLE,
  CONSTRAINT `fk_Roles_colors1`
    FOREIGN KEY (`color_id`)
    REFERENCES `teamSweetDreams_DMS`.`Colors` (`color_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`Users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`Users` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`Users` (
  `user_id` INT NOT NULL,
  `fullName` VARCHAR(45) NULL,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `user_role` VARCHAR(45) NOT NULL,
  `date_joined` DATETIME NOT NULL,
  `active` TINYINT NOT NULL,
  `ActivityStatus_activity_id` INT NOT NULL,
  `role_id` INT NOT NULL,
  `role_color_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `ActivityStatus_activity_id`, `role_id`, `role_color_id`),
  INDEX `fk_Users_ActivityStatus1_idx` (`ActivityStatus_activity_id` ASC) VISIBLE,
  INDEX `fk_Users_Roles1_idx` (`role_id` ASC, `role_color_id` ASC) VISIBLE,
  CONSTRAINT `fk_Users_ActivityStatus1`
    FOREIGN KEY (`ActivityStatus_activity_id`)
    REFERENCES `teamSweetDreams_DMS`.`ActivityStatus` (`activity_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Users_Roles1`
    FOREIGN KEY (`role_id` , `role_color_id`)
    REFERENCES `teamSweetDreams_DMS`.`Roles` (`role_id` , `color_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`Location`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`Location` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`Location` (
  `place_id` INT NOT NULL,
  `address_ln_1` VARCHAR(45) NULL,
  `address_ln2` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `state` VARCHAR(45) NULL,
  `zip` INT NULL,
  PRIMARY KEY (`place_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`Organizations`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`Organizations` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`Organizations` (
  `org_id` INT NOT NULL,
  `org_name` VARCHAR(45) NULL,
  `maxDiaries` INT NOT NULL,
  `creator_id` INT NOT NULL,
  `date_created` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`org_id`, `creator_id`),
  INDEX `fk_Organizations_Users1_idx` (`creator_id` ASC) VISIBLE,
  CONSTRAINT `fk_Organizations_Users1`
    FOREIGN KEY (`creator_id`)
    REFERENCES `teamSweetDreams_DMS`.`Users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`EntryTypes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`EntryTypes` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`EntryTypes` (
  `entryType_id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `description` VARCHAR(45) NULL,
  `notes` VARCHAR(45) NULL,
  `color_id` INT NOT NULL,
  PRIMARY KEY (`entryType_id`, `color_id`),
  INDEX `fk_EntryType_colors1_idx` (`color_id` ASC) VISIBLE,
  CONSTRAINT `fk_EntryType_colors1`
    FOREIGN KEY (`color_id`)
    REFERENCES `teamSweetDreams_DMS`.`Colors` (`color_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`Diaries`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`Diaries` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`Diaries` (
  `diary_id` INT NOT NULL,
  `date_created` VARCHAR(45) NULL,
  `last_updated` VARCHAR(45) NULL,
  `created_by` VARCHAR(45) NULL,
  `description` VARCHAR(45) NULL,
  `Organizations_org_id` INT NOT NULL,
  PRIMARY KEY (`diary_id`, `Organizations_org_id`),
  INDEX `fk_Diaries_Organizations1_idx` (`Organizations_org_id` ASC) VISIBLE,
  CONSTRAINT `fk_Diaries_Organizations1`
    FOREIGN KEY (`Organizations_org_id`)
    REFERENCES `teamSweetDreams_DMS`.`Organizations` (`org_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`Entries`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`Entries` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`Entries` (
  `entry_id` INT NOT NULL,
  `entry_name` VARCHAR(45) NOT NULL,
  `start_time` DATETIME NOT NULL,
  `end_time` DATETIME NOT NULL,
  `duration` DATETIME NULL,
  `priority` INT NULL,
  `description` VARCHAR(45) NULL,
  `owner` INT NOT NULL,
  `org_id` INT NOT NULL,
  `location_id` INT NULL,
  `entryType_id` INT NOT NULL,
  `diary_id` INT NOT NULL,
  PRIMARY KEY (`entry_id`, `owner`, `org_id`),
  INDEX `fk_Entries_Users1_idx` (`owner` ASC) VISIBLE,
  INDEX `fk_Entries_Organizations1_idx` (`org_id` ASC) VISIBLE,
  INDEX `fk_Entries_Location1_idx` (`location_id` ASC) VISIBLE,
  INDEX `fk_Entries_EntryType1_idx` (`entryType_id` ASC) VISIBLE,
  INDEX `fk_Entries_Diaries1_idx` (`diary_id` ASC) VISIBLE,
  CONSTRAINT `fk_Entries_Users1`
    FOREIGN KEY (`owner`)
    REFERENCES `teamSweetDreams_DMS`.`Users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Entries_Organizations1`
    FOREIGN KEY (`org_id`)
    REFERENCES `teamSweetDreams_DMS`.`Organizations` (`org_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Entries_Location1`
    FOREIGN KEY (`location_id`)
    REFERENCES `teamSweetDreams_DMS`.`Location` (`place_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Entries_EntryType1`
    FOREIGN KEY (`entryType_id`)
    REFERENCES `teamSweetDreams_DMS`.`EntryTypes` (`entryType_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Entries_Diaries1`
    FOREIGN KEY (`diary_id`)
    REFERENCES `teamSweetDreams_DMS`.`Diaries` (`diary_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`Meetings`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`Meetings` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`Meetings` (
  `meeting_id` INT NOT NULL,
  PRIMARY KEY (`meeting_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`Users_Organizations`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`Users_Organizations` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`Users_Organizations` (
  `Users_user_id` INT NOT NULL,
  `Organizations_org_id` INT NULL,
  PRIMARY KEY (`Users_user_id`),
  INDEX `fk_Users_has_Organizations_Organizations1_idx` (`Organizations_org_id` ASC) VISIBLE,
  INDEX `fk_Users_has_Organizations_Users_idx` (`Users_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_Users_has_Organizations_Users`
    FOREIGN KEY (`Users_user_id`)
    REFERENCES `teamSweetDreams_DMS`.`Users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Users_has_Organizations_Organizations1`
    FOREIGN KEY (`Organizations_org_id`)
    REFERENCES `teamSweetDreams_DMS`.`Organizations` (`org_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`UserHasRoles`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`UserHasRoles` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`UserHasRoles` (
  `Roles_role_id` INT NOT NULL,
  PRIMARY KEY (`Roles_role_id`),
  INDEX `fk_Users_has_Roles_Roles1_idx` (`Roles_role_id` ASC) VISIBLE,
  CONSTRAINT `fk_Users_has_Roles_Roles1`
    FOREIGN KEY (`Roles_role_id`)
    REFERENCES `teamSweetDreams_DMS`.`Roles` (`role_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`Permissions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`Permissions` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`Permissions` (
  `perm_id` INT NOT NULL,
  `perm_name` VARCHAR(45) NOT NULL,
  `perm_description` VARCHAR(45) NULL,
  `perm_notes` VARCHAR(45) NULL,
  `enabled` CHAR NULL DEFAULT 'F',
  PRIMARY KEY (`perm_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`Roles_has_Permissions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`Roles_has_Permissions` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`Roles_has_Permissions` (
  `Roles_role_id` INT NOT NULL,
  `Permissions_perm_id` INT NOT NULL,
  PRIMARY KEY (`Roles_role_id`, `Permissions_perm_id`),
  INDEX `fk_Roles_has_Permissions_Permissions1_idx` (`Permissions_perm_id` ASC) VISIBLE,
  INDEX `fk_Roles_has_Permissions_Roles1_idx` (`Roles_role_id` ASC) VISIBLE,
  CONSTRAINT `fk_Roles_has_Permissions_Roles1`
    FOREIGN KEY (`Roles_role_id`)
    REFERENCES `teamSweetDreams_DMS`.`Roles` (`role_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Roles_has_Permissions_Permissions1`
    FOREIGN KEY (`Permissions_perm_id`)
    REFERENCES `teamSweetDreams_DMS`.`Permissions` (`perm_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`RolePermissions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`RolePermissions` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`RolePermissions` (
  `perm_id` INT NOT NULL,
  `role_id` INT NOT NULL,
  PRIMARY KEY (`perm_id`, `role_id`),
  INDEX `fk_Permissions_has_Roles_Roles1_idx` (`role_id` ASC) VISIBLE,
  INDEX `fk_Permissions_has_Roles_Permissions1_idx` (`perm_id` ASC) VISIBLE,
  CONSTRAINT `fk_Permissions_has_Roles_Permissions1`
    FOREIGN KEY (`perm_id`)
    REFERENCES `teamSweetDreams_DMS`.`Permissions` (`perm_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Permissions_has_Roles_Roles1`
    FOREIGN KEY (`role_id`)
    REFERENCES `teamSweetDreams_DMS`.`Roles` (`role_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`OrganizationMembers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`OrganizationMembers` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`OrganizationMembers` (
  `user_id` INT NOT NULL,
  `org_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `org_id`),
  INDEX `fk_Users_has_Organizations_Organizations2_idx` (`org_id` ASC) VISIBLE,
  INDEX `fk_Users_has_Organizations_Users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_Users_has_Organizations_Users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `teamSweetDreams_DMS`.`Users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Users_has_Organizations_Organizations2`
    FOREIGN KEY (`org_id`)
    REFERENCES `teamSweetDreams_DMS`.`Organizations` (`org_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`userDiaries`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`userDiaries` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`userDiaries` (
  `user_id` INT NOT NULL,
  `diary_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `diary_id`),
  INDEX `fk_Users_has_Diaries_Diaries2_idx` (`diary_id` ASC) VISIBLE,
  INDEX `fk_Users_has_Diaries_Users2_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_Users_has_Diaries_Users2`
    FOREIGN KEY (`user_id`)
    REFERENCES `teamSweetDreams_DMS`.`Users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Users_has_Diaries_Diaries2`
    FOREIGN KEY (`diary_id`)
    REFERENCES `teamSweetDreams_DMS`.`Diaries` (`diary_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `teamSweetDreams_DMS`.`userPermissions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `teamSweetDreams_DMS`.`userPermissions` ;

CREATE TABLE IF NOT EXISTS `teamSweetDreams_DMS`.`userPermissions` (
  `user_id` INT NOT NULL,
  `perm_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `perm_id`),
  INDEX `fk_Users_has_Permissions_Permissions1_idx` (`perm_id` ASC) VISIBLE,
  INDEX `fk_Users_has_Permissions_Users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_Users_has_Permissions_Users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `teamSweetDreams_DMS`.`Users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Users_has_Permissions_Permissions1`
    FOREIGN KEY (`perm_id`)
    REFERENCES `teamSweetDreams_DMS`.`Permissions` (`perm_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
