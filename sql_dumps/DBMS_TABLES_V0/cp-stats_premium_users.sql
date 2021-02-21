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
-- Table structure for table `premium_users`
--

DROP TABLE IF EXISTS `premium_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `premium_users` (
  `ID` varchar(20) NOT NULL,
  `Profile_Visits` int DEFAULT '0',
  `Subscription_Time_Start` varchar(50) NOT NULL,
  `Subscription_Time_End` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID_UNIQUE` (`ID`),
  CONSTRAINT `FK_Premium_User_Id` FOREIGN KEY (`ID`) REFERENCES `users` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `premium_users`
--

LOCK TABLES `premium_users` WRITE;
/*!40000 ALTER TABLE `premium_users` DISABLE KEYS */;
INSERT INTO `premium_users` VALUES ('U-1',285,'2019-10-13','2021-05-09'),('U-119',104,'2021-11-18','2022-01-07'),('U-126',83,'2020-10-20','2020-12-26'),('U-135',298,'2021-03-15','2021-07-31'),('U-139',98,'2013-08-02','2020-12-24'),('U-142',176,'2017-03-06','2017-11-24'),('U-154',153,'2000-10-29','2019-09-15'),('U-176',212,'2013-01-27','2013-11-21'),('U-181',219,'2020-03-13','2020-03-30'),('U-186',278,'2020-09-03','2021-08-27'),('U-191',264,'2018-07-01','2021-10-04'),('U-197',130,'2020-03-25','2020-10-29'),('U-199',178,'2018-04-12','2019-02-11'),('U-200',32,'2020-02-14','2020-09-15'),('U-206',240,'2019-09-10','2019-11-19'),('U-223',282,'2020-03-05','2020-08-30'),('U-224',10,'2021-06-24','2021-07-07'),('U-227',152,'2020-03-10','2020-08-16'),('U-236',238,'2021-04-21','2021-09-30'),('U-239',253,'2017-01-17','2018-05-21'),('U-241',81,'2021-06-16','2021-08-14'),('U-254',15,'2018-03-20','2021-08-03'),('U-255',274,'2020-11-14','2021-11-11'),('U-259',238,'2003-03-19','2007-08-29'),('U-261',212,'2011-03-01','2016-11-11'),('U-27',231,'2021-08-09','2021-12-03'),('U-270',220,'2010-08-14','2012-09-28'),('U-272',78,'2013-12-30','2014-08-13'),('U-279',152,'2009-08-08','2017-03-20'),('U-282',271,'2017-03-13','2017-06-11'),('U-29',156,'2006-07-12','2019-10-15'),('U-37',236,'2018-12-02','2020-07-06'),('U-4',15,'2019-10-10','2020-03-01'),('U-47',254,'2021-01-30','2021-06-09'),('U-48',16,'2014-01-28','2019-01-18'),('U-5',271,'2019-07-28','2020-03-08'),('U-6',110,'2021-12-10','2022-02-12'),('U-61',10,'2017-10-09','2017-11-27'),('U-62',33,'2009-08-20','2020-11-17'),('U-64',47,'2008-08-27','2009-02-27'),('U-68',43,'2016-06-26','2017-04-20'),('U-69',298,'2020-09-27','2021-10-15'),('U-77',143,'2021-07-11','2021-10-18'),('U-81',19,'2016-12-29','2021-01-22'),('U-85',137,'2020-12-28','2022-01-19'),('U-88',61,'2020-09-29','2021-11-08'),('U-9',105,'2020-11-24','2020-12-21'),('U-94',138,'2021-09-22','2022-01-23'),('U-96',55,'2008-06-23','2017-04-15'),('U-99',96,'2014-07-17','2020-04-28');
/*!40000 ALTER TABLE `premium_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-21 20:05:40
