-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: projectphase03
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `date & time datatypes`
--

DROP TABLE IF EXISTS `date & time datatypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `date & time datatypes` (
  `idDate & Time Datatypes` int NOT NULL,
  PRIMARY KEY (`idDate & Time Datatypes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `date & time datatypes`
--

LOCK TABLES `date & time datatypes` WRITE;
/*!40000 ALTER TABLE `date & time datatypes` DISABLE KEYS */;
/*!40000 ALTER TABLE `date & time datatypes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-05 18:26:40
=======
-- Date and Time types 
-- -- Comprehensive Example using all DATE and TIME data types
-- -- Also uses Fractional Seconds and Auto-initialization and Auto-updating

use project_phase_03;
create table DATEandTIME (
	CurrentDATE DATE,
    CurrentTIME TIME,
    CurrentTIME6 TIME(6),
    CurrentTIME5 TIME(5),
    CurrentTIME4 TIME(4),
    CurrentTIME3 TIME(3),
    CurrentTIME2 TIME(2),
    CurrentTIME1 TIME(1),
    CurrentTIME0 TIME(0),
    CurrentYEAR YEAR,
    CurrentDATETIME DATETIME NOT NULL ON UPDATE CURRENT_TIMESTAMP,
    CurrentTIMESTAMP TIMESTAMP NULL ON UPDATE CURRENT_TIMESTAMP
);    

-- Signed DATE example
insert into DATEandTIME (CurrentDate, CurrentTIME, CurrentTIME6, CurrentTIME5, CurrentTIME4, CurrentTIME3, CurrentTIME2, CurrentTIME1, CurrentTIME0, CurrentYEAR, CurrentDATETIME, CurrentTIMESTAMP)
	values ('2023-10-09', '16:39.143665', '16:39.143665', '16:39.143665', '16:39.143665', '16:39.143665', '16:39.143665', '16:39.143665', '16:39.143665', '2023', NOW(),NOW());
    
-- drop table DATEandTIME;