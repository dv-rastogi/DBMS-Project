CREATE DATABASE  IF NOT EXISTS `cp-stats` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cp-stats`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: cp-stats
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `groups`
--

DROP TABLE IF EXISTS `groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `groups` (
  `ID` varchar(20) NOT NULL,
  `Group_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `DateOfFormation` varchar(50) NOT NULL,
  `Size` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`Group_ID`),
  UNIQUE KEY `Group_ID_UNIQUE` (`Group_ID`),
  KEY `FK_Groups_idx` (`ID`),
  CONSTRAINT `FK_Groups` FOREIGN KEY (`ID`) REFERENCES `users` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups`
--

LOCK TABLES `groups` WRITE;
/*!40000 ALTER TABLE `groups` DISABLE KEYS */;
INSERT INTO `groups` VALUES ('U-297',1,'uncredit','2020-03-12',14),('U-75',2,'tenacle','2019-11-20',5),('U-127',3,'inoculable','2019-11-06',16),('U-135',4,'socialism','2020-12-21',14),('U-139',5,'briquets','2009-07-05',18),('U-157',6,'barbwire','2010-01-03',5),('U-9',7,'indene','2020-12-13',4),('U-119',8,'trout-hole','2005-01-26',9),('U-54',9,'fry-up','2017-03-16',7),('U-236',10,'faith-healing','2016-11-04',2),('U-86',11,'insignificantly','2019-07-04',20),('U-14',12,'combustible','2020-09-11',2),('U-279',13,'blasphemous','2020-10-25',16),('U-202',14,'uncreate','2017-06-18',4),('U-215',15,'cast-by','2014-09-12',16),('U-72',16,'sallowness','2018-05-27',18),('U-140',17,'caped','2020-10-03',2),('U-161',18,'vocabulary','2019-12-24',15),('U-57',19,'insulating','2014-03-03',12),('U-154',20,'travelators','2008-09-10',3),('U-184',21,'glittered','2018-09-27',10),('U-15',22,'Gatling gun','2018-10-01',6),('U-22',23,'inseparable','2020-12-09',20),('U-254',24,'alveole','2013-12-08',7),('U-267',25,'armstand','2018-03-15',19),('U-255',26,'arbitrational','2020-06-18',1),('U-179',27,'macropoma','2012-04-18',7),('U-178',28,'medevacked','2018-12-14',13),('U-4',29,'lethally','2019-08-13',8),('U-193',30,'exaltations','2018-01-19',16),('U-80',31,'Qiana','2020-02-09',9),('U-277',32,'mailings','2017-11-12',5),('U-296',33,'straughte','2018-06-26',13),('U-125',34,'verapamil','2020-06-11',11),('U-259',35,'thrist','2008-07-16',6),('U-74',36,'thunder-crack','2020-10-29',19),('U-270',37,'stern-wheeler','2008-04-08',4),('U-26',38,'unbright','2019-08-05',8),('U-66',39,'intussuscepted','2020-07-26',16),('U-156',40,'ill-humoredly','2009-10-25',9),('U-282',41,'cacodaemoniacal','2014-01-23',12),('U-37',42,'hamartia','2020-11-15',7),('U-46',43,'Tsaritsyn','2018-04-04',20),('U-53',44,'unfrightful','2019-04-05',15),('U-261',45,'pernicious','2010-10-08',15),('U-168',46,'endonucleolytic','2019-07-09',8),('U-101',47,'fleered','2019-04-21',11),('U-90',48,'coevally','2020-12-07',16),('U-82',49,'chromography','2020-06-25',18),('U-242',50,'figurated','2009-03-19',2);
/*!40000 ALTER TABLE `groups` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-21 20:05:37
