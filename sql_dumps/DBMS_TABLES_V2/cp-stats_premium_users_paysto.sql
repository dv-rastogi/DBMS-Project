-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: cp-stats
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `premium_users_paysto`
--

DROP TABLE IF EXISTS `premium_users_paysto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `premium_users_paysto` (
  `Premium_User_ID` varchar(20) NOT NULL,
  `Admin_Role` varchar(50) NOT NULL DEFAULT 'Premium',
  `DateOfPayment` datetime NOT NULL,
  `AmountPaid` int NOT NULL,
  PRIMARY KEY (`Premium_User_ID`,`Admin_Role`,`DateOfPayment`),
  KEY `FK_Admin_Role_idx` (`Admin_Role`),
  CONSTRAINT `FK_Premium_User_PaysTo` FOREIGN KEY (`Premium_User_ID`) REFERENCES `premium_users` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_Premium_Users_PaysTo_Admin` FOREIGN KEY (`Admin_Role`) REFERENCES `admin` (`Role`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `premium_users_paysto`
--

LOCK TABLES `premium_users_paysto` WRITE;
/*!40000 ALTER TABLE `premium_users_paysto` DISABLE KEYS */;
INSERT INTO `premium_users_paysto` VALUES ('U-1','User','2020-08-09 00:00:00',1769),('U-119','Financial','2020-05-05 00:00:00',1204),('U-126','Support','2020-02-16 00:00:00',2006),('U-135','Organisation','2020-10-16 00:00:00',1872),('U-139','Financial','2020-06-26 00:00:00',1863),('U-142','Domain','2020-09-06 00:00:00',2138),('U-154','Financial','2020-07-07 00:00:00',2274),('U-176','Advertisement','2020-06-12 00:00:00',1997),('U-181','Global','2020-07-17 00:00:00',1724),('U-186','Domain','2020-09-14 00:00:00',1908),('U-191','Domain','2020-08-15 00:00:00',2024),('U-197','Advertisement','2020-04-05 00:00:00',1249),('U-199','General','2020-06-03 00:00:00',1468),('U-200','Organisation','2020-02-03 00:00:00',1519),('U-206','Support','2020-11-04 00:00:00',1879),('U-223','Support','2020-09-28 00:00:00',2429),('U-224','HR','2020-12-08 00:00:00',1223),('U-227','Domain','2020-05-15 00:00:00',2339),('U-236','Senior','2020-04-04 00:00:00',1403),('U-239','Global','2020-10-06 00:00:00',2365),('U-241','General','2020-06-17 00:00:00',1869),('U-254','General','2020-07-26 00:00:00',2400),('U-255','Financial','2020-09-20 00:00:00',2060),('U-259','General','2020-08-07 00:00:00',1253),('U-261','General','2020-12-28 00:00:00',2158),('U-27','Premium','2020-05-28 00:00:00',1789),('U-270','Senior','2020-05-29 00:00:00',1296),('U-272','Support','2020-07-12 00:00:00',1323),('U-279','Organisation','2020-09-08 00:00:00',2320),('U-282','General','2020-04-09 00:00:00',1564),('U-29','User','2020-07-23 00:00:00',1408),('U-37','Global','2020-12-19 00:00:00',1881),('U-4','Senior','2020-02-27 00:00:00',1728),('U-47','Domain','2020-04-23 00:00:00',1087),('U-48','Advertisement','2020-06-12 00:00:00',1496),('U-5','Technical','2020-04-27 00:00:00',1551),('U-6','Financial','2020-08-20 00:00:00',2451),('U-61','Global','2020-11-02 00:00:00',1962),('U-62','User','2020-05-18 00:00:00',1479),('U-64','General','2020-04-18 00:00:00',1466),('U-68','Global','2020-12-02 00:00:00',1926),('U-69','Advertisement','2020-04-24 00:00:00',2415),('U-77','Premium','2020-06-09 00:00:00',1260),('U-81','Domain','2020-11-07 00:00:00',1366),('U-85','Global','2020-09-06 00:00:00',2458),('U-88','Global','2020-11-20 00:00:00',1323),('U-9','User','2020-05-05 00:00:00',1495),('U-94','Support','2020-09-11 00:00:00',2286),('U-96','Advertisement','2020-08-16 00:00:00',1483),('U-99','Premium','2020-11-13 00:00:00',1788);
/*!40000 ALTER TABLE `premium_users_paysto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-16 20:07:04
