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
-- Table structure for table `contest_tags`
--

DROP TABLE IF EXISTS `contest_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contest_tags` (
  `ID` varchar(20) NOT NULL,
  `Name` varchar(200) NOT NULL,
  `Tag` varchar(20) NOT NULL,
  `Date` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`,`Name`,`Tag`,`Date`),
  KEY `FK_Contest_Tags_idx` (`ID`,`Name`,`Date`),
  CONSTRAINT `FK_Contest_Tags` FOREIGN KEY (`ID`, `Name`, `Date`) REFERENCES `contests` (`ID`, `Name`, `Date`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contest_tags`
--

LOCK TABLES `contest_tags` WRITE;
/*!40000 ALTER TABLE `contest_tags` DISABLE KEYS */;
INSERT INTO `contest_tags` VALUES ('P-1','Codeforces Round 438','brute force','2019-01-13'),('P-1','Codeforces Round 455','binary search','2018-09-13'),('P-1','Codeforces Round 455','strings','2018-09-13'),('P-1','Codeforces Round 509','binary search','2017-03-08'),('P-1','Codeforces Round 509','graphs','2017-03-08'),('P-1','Codeforces Round 509','greedy','2017-03-08'),('P-1','Codeforces Round 509','math','2017-03-08'),('P-1','Codeforces Round 521','brute force','2016-12-25'),('P-1','Codeforces Round 521','data structures','2016-12-25'),('P-1','Codeforces Round 521','implementation','2016-12-25'),('P-1','Codeforces Round 521','number theory','2016-12-25'),('P-1','Codeforces Round 632','brute force','2019-07-13'),('P-1','Codeforces Round 632','data structures','2019-07-13'),('P-1','Codeforces Round 652','dp','2017-04-22'),('P-1','Codeforces Round 652','graphs','2017-04-22'),('P-1','Codeforces Round 652','greedy','2017-04-22'),('P-1','Codeforces Round 652','strings','2017-04-22'),('P-2','Leetcode Biweekly Contest 428','math','2020-07-25'),('P-2','Leetcode Biweekly Contest 428','strings','2020-07-25'),('P-2','Leetcode Biweekly Contest 475','data structures','2017-08-07'),('P-2','Leetcode Biweekly Contest 475','dp','2017-08-07'),('P-2','Leetcode Biweekly Contest 475','implementation','2017-08-07'),('P-2','Leetcode Biweekly Contest 475','strings','2017-08-07'),('P-2','Leetcode Biweekly Contest 508','binary search','2020-06-20'),('P-2','Leetcode Biweekly Contest 590','binary search','2018-12-09'),('P-2','Leetcode Biweekly Contest 590','data structures','2018-12-09'),('P-2','Leetcode Biweekly Contest 590','dp','2018-12-09'),('P-2','Leetcode Biweekly Contest 590','graphs','2018-12-09'),('P-2','Leetcode Biweekly Contest 590','number theory','2018-12-09'),('P-2','Leetcode Biweekly Contest 671','data structures','2019-08-25'),('P-2','Leetcode Biweekly Contest 671','math','2019-08-25'),('P-2','Leetcode Weekly Contest 508','graphs','2018-10-08'),('P-2','Leetcode Weekly Contest 508','math','2018-10-08'),('P-2','Leetcode Weekly Contest 508','strings','2018-10-08'),('P-2','Leetcode Weekly Contest 533','data structures','2018-11-17'),('P-2','Leetcode Weekly Contest 533','math','2018-11-17'),('P-2','Leetcode Weekly Contest 570','binary search','2019-03-17'),('P-2','Leetcode Weekly Contest 570','brute force','2019-03-17'),('P-2','Leetcode Weekly Contest 570','greedy','2019-03-17'),('P-2','Leetcode Weekly Contest 570','math','2019-03-17'),('P-2','Leetcode Weekly Contest 570','strings','2019-03-17'),('P-2','Leetcode Weekly Contest 656','binary search','2020-04-24'),('P-2','Leetcode Weekly Contest 656','data structures','2020-04-24'),('P-2','Leetcode Weekly Contest 656','math','2020-04-24'),('P-2','Leetcode Weekly Contest 656','number theory','2020-04-24'),('P-2','Leetcode Weekly Contest 696','binary search','2020-02-02');
/*!40000 ALTER TABLE `contest_tags` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-21 20:05:39
