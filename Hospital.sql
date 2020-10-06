-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: Hospital
-- ------------------------------------------------------
-- Server version	5.7.31-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Appointment`
--

DROP DATABASE IF EXISTS `Hospital`;
CREATE DATABASE Hospital;
USE Hospital;

DROP TABLE IF EXISTS `Appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Appointment` (
  `Time` time NOT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY (`Time`,`Date`),
  KEY `Date` (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Appointment`
--

LOCK TABLES `Appointment` WRITE;
/*!40000 ALTER TABLE `Appointment` DISABLE KEYS */;
INSERT INTO `Appointment` VALUES ('12:00:00','2020-09-09');
/*!40000 ALTER TABLE `Appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Batch_Details`
--

DROP TABLE IF EXISTS `Batch_Details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Batch_Details` (
  `Batch_No` int(11) NOT NULL,
  `Qty` int(11) NOT NULL,
  PRIMARY KEY (`Batch_No`),
  CONSTRAINT `Batch_Details_ibfk_1` FOREIGN KEY (`Batch_No`) REFERENCES `Medication` (`Batch_No`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Batch_Details`
--

LOCK TABLES `Batch_Details` WRITE;
/*!40000 ALTER TABLE `Batch_Details` DISABLE KEYS */;
INSERT INTO `Batch_Details` VALUES (12,590);
/*!40000 ALTER TABLE `Batch_Details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Bill`
--

DROP TABLE IF EXISTS `Bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Bill` (
  `Bill_No` int(11) NOT NULL,
  `Amount` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Time` time NOT NULL,
  `Payment_Status` char(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`Bill_No`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bill`
--

LOCK TABLES `Bill` WRITE;
/*!40000 ALTER TABLE `Bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `Bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Department`
--

DROP TABLE IF EXISTS `Department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Department` (
  `Dno` int(11) NOT NULL,
  `Dname` varchar(255) NOT NULL,
  `Location_Floor` int(11) NOT NULL,
  `Location_Block` varchar(255) NOT NULL,
  PRIMARY KEY (`Dno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Department`
--

LOCK TABLES `Department` WRITE;
/*!40000 ALTER TABLE `Department` DISABLE KEYS */;
INSERT INTO `Department` VALUES (12,'Emergency',2,'32');
INSERT INTO `Department` VALUES (1,'ENT',2,'A');
/*!40000 ALTER TABLE `Department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Doctor`
--

DROP TABLE IF EXISTS `Doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Doctor` (
  `Staff_Id` int(11) NOT NULL,
  `Consultation_Fee` int(11) NOT NULL,
  PRIMARY KEY (`Staff_Id`),
  CONSTRAINT `Doctor_ibfk_1` FOREIGN KEY (`Staff_Id`) REFERENCES `Staff` (`Staff_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Doctor`
--

LOCK TABLES `Doctor` WRITE;
/*!40000 ALTER TABLE `Doctor` DISABLE KEYS */;
INSERT INTO `Doctor` VALUES (374598,500);
INSERT INTO `Doctor` VALUES (554380,6000),(983313,10000);
/*!40000 ALTER TABLE `Doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Education`
--

DROP TABLE IF EXISTS `Education`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Education` (
  `Staff_Id` int(11) NOT NULL,
  `Degree` varchar(255) NOT NULL,
  PRIMARY KEY (`Staff_Id`,`Degree`),
  CONSTRAINT `Education_ibfk_1` FOREIGN KEY (`Staff_Id`) REFERENCES `Staff` (`Staff_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Education`
--

LOCK TABLES `Education` WRITE;
/*!40000 ALTER TABLE `Education` DISABLE KEYS */;
INSERT INTO `Education` VALUES (374598,'MBBS');
INSERT INTO `Education` VALUES (554380,'MBBS'),(983313,'MBBS'),(983313,'PHD');
/*!40000 ALTER TABLE `Education` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Entails`
--

DROP TABLE IF EXISTS `Entails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Entails` (
  `Pno` int(11) NOT NULL,
  `Date` date DEFAULT NULL,
  `Time` time DEFAULT NULL,
  `Bill_No` int(11) NOT NULL,
  PRIMARY KEY (`Pno`),
  KEY `Date` (`Date`),
  KEY `Bill_No` (`Bill_No`),
  KEY `Time` (`Time`),
  CONSTRAINT `Entails_ibfk_1` FOREIGN KEY (`Date`) REFERENCES `Test_or_Surgery` (`Date`),
  CONSTRAINT `Entails_ibfk_2` FOREIGN KEY (`Bill_No`) REFERENCES `Bill` (`Bill_No`),
  CONSTRAINT `Entails_ibfk_3` FOREIGN KEY (`Pno`) REFERENCES `Prescription` (`Pno`),
  CONSTRAINT `Entails_ibfk_4` FOREIGN KEY (`Time`) REFERENCES `Test_or_Surgery` (`Time`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Entails`
--

LOCK TABLES `Entails` WRITE;
/*!40000 ALTER TABLE `Entails` DISABLE KEYS */;
/*!40000 ALTER TABLE `Entails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Heads`
--

DROP TABLE IF EXISTS `Heads`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Heads` (
  `Dno` int(11) NOT NULL,
  `Staff_Id` int(11) NOT NULL,
  PRIMARY KEY (`Dno`),
  KEY `Staff_Id` (`Staff_Id`),
  CONSTRAINT `Heads_ibfk_1` FOREIGN KEY (`Dno`) REFERENCES `Department` (`Dno`),
  CONSTRAINT `Heads_ibfk_2` FOREIGN KEY (`Staff_Id`) REFERENCES `Doctor` (`Staff_Id`),
  CONSTRAINT `Heads_ibfk_3` FOREIGN KEY (`Dno`) REFERENCES `Works_In` (`Dno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Heads`
--

LOCK TABLES `Heads` WRITE;
/*!40000 ALTER TABLE `Heads` DISABLE KEYS */;
INSERT INTO `Heads` VALUES (12,374598);
INSERT INTO `Heads` VALUES (1,983313);
/*!40000 ALTER TABLE `Heads` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Insured_Details`
--

DROP TABLE IF EXISTS `Insured_Details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Insured_Details` (
  `Insurance_Id` int(11) NOT NULL,
  `Company` varchar(255) NOT NULL,
  `Latest_Renewal_Date` date NOT NULL,
  PRIMARY KEY (`Insurance_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Insured_Details`
--

LOCK TABLES `Insured_Details` WRITE;
/*!40000 ALTER TABLE `Insured_Details` DISABLE KEYS */;
INSERT INTO `Insured_Details` VALUES (85623,'LIC','2019-10-01');
/*!40000 ALTER TABLE `Insured_Details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Insured_Patients`
--

DROP TABLE IF EXISTS `Insured_Patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Insured_Patients` (
  `Patient_Id` int(11) NOT NULL,
  `Insurance_Id` int(11) NOT NULL,
  PRIMARY KEY (`Patient_Id`),
  KEY `Insurance_Id` (`Insurance_Id`),
  CONSTRAINT `Insured_Patients_ibfk_1` FOREIGN KEY (`Patient_Id`) REFERENCES `Patient` (`Patient_Id`),
  CONSTRAINT `Insured_Patients_ibfk_2` FOREIGN KEY (`Insurance_Id`) REFERENCES `Insured_Details` (`Insurance_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Insured_Patients`
--

LOCK TABLES `Insured_Patients` WRITE;
/*!40000 ALTER TABLE `Insured_Patients` DISABLE KEYS */;
INSERT INTO `Insured_Patients` VALUES (244472,85623);
/*!40000 ALTER TABLE `Insured_Patients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Med_Details`
--

DROP TABLE IF EXISTS `Med_Details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Med_Details` (
  `Med_Name` varchar(255) NOT NULL,
  `Manufacturer` varchar(255) NOT NULL,
  `Price` float NOT NULL,
  PRIMARY KEY (`Med_Name`),
  CONSTRAINT `Med_Details_ibfk_1` FOREIGN KEY (`Med_Name`) REFERENCES `Medication` (`Med_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Med_Details`
--

LOCK TABLES `Med_Details` WRITE;
/*!40000 ALTER TABLE `Med_Details` DISABLE KEYS */;
INSERT INTO `Med_Details` VALUES ('Paracetamol','Fanatol',20);
/*!40000 ALTER TABLE `Med_Details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Medication`
--

DROP TABLE IF EXISTS `Medication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Medication` (
  `Med_Name` varchar(255) NOT NULL,
  `Batch_No` int(11) NOT NULL,
  `Expiry_Date` date NOT NULL,
  `Supplier_Id` int(11) NOT NULL,
  PRIMARY KEY (`Med_Name`,`Batch_No`),
  KEY `Batch_No` (`Batch_No`),
  KEY `Supplier_Id` (`Supplier_Id`),
  CONSTRAINT `Medication_ibfk_1` FOREIGN KEY (`Supplier_Id`) REFERENCES `Supplier_Details` (`Supplier_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medication`
--

LOCK TABLES `Medication` WRITE;
/*!40000 ALTER TABLE `Medication` DISABLE KEYS */;
INSERT INTO `Medication` VALUES ('Paracetamol',12,'2025-09-13',14);
/*!40000 ALTER TABLE `Medication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Patient`
--

DROP TABLE IF EXISTS `Patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Patient` (
  `Patient_Id` int(11) NOT NULL,
  `First_Name` varchar(255) NOT NULL,
  `Last_Name` varchar(255) NOT NULL,
  `H_No` int(11) DEFAULT NULL,
  `Street` varchar(255) DEFAULT NULL,
  `City` varchar(255) DEFAULT NULL,
  `Zipcode` int(11) DEFAULT NULL,
  `Contact_No` bigint(20) DEFAULT NULL,
  `Date_Of_Birth` date NOT NULL,
  PRIMARY KEY (`Patient_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Patient`
--

LOCK TABLES `Patient` WRITE;
/*!40000 ALTER TABLE `Patient` DISABLE KEYS */;
INSERT INTO `Patient` VALUES (399815,'Chirag','Sahu',NULL,'','',NULL,1234567890,'2001-08-25');
INSERT INTO `Patient` VALUES (244472,'Debayan','Saha',NULL,'','',NULL,9234076187,'2001-07-28'),(787961,'Jayant','Panwar',NULL,'','',NULL,9120934785,'2001-06-15');
/*!40000 ALTER TABLE `Patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pays`
--

DROP TABLE IF EXISTS `Pays`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Pays` (
  `Bill_No` int(11) NOT NULL,
  `Patient_Id` int(11) NOT NULL,
  `Staff_Id` int(11) NOT NULL,
  PRIMARY KEY (`Bill_No`),
  KEY `Patient_Id` (`Patient_Id`),
  KEY `Staff_Id` (`Staff_Id`),
  CONSTRAINT `Pays_ibfk_1` FOREIGN KEY (`Bill_No`) REFERENCES `Bill` (`Bill_No`),
  CONSTRAINT `Pays_ibfk_2` FOREIGN KEY (`Patient_Id`) REFERENCES `Patient` (`Patient_Id`),
  CONSTRAINT `Pays_ibfk_3` FOREIGN KEY (`Staff_Id`) REFERENCES `Staff` (`Staff_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pays`
--

LOCK TABLES `Pays` WRITE;
/*!40000 ALTER TABLE `Pays` DISABLE KEYS */;
/*!40000 ALTER TABLE `Pays` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Performs`
--

DROP TABLE IF EXISTS `Performs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Performs` (
  `Date` date NOT NULL,
  `Time` time NOT NULL,
  `Staff_Id` int(11) NOT NULL,
  `Room_No` int(11) NOT NULL,
  PRIMARY KEY (`Date`,`Time`),
  KEY `Staff_Id` (`Staff_Id`),
  KEY `Room_No` (`Room_No`),
  KEY `Time` (`Time`),
  CONSTRAINT `Performs_ibfk_1` FOREIGN KEY (`Date`) REFERENCES `Test_or_Surgery` (`Date`),
  CONSTRAINT `Performs_ibfk_2` FOREIGN KEY (`Staff_Id`) REFERENCES `Staff` (`Staff_Id`),
  CONSTRAINT `Performs_ibfk_3` FOREIGN KEY (`Room_No`) REFERENCES `Room` (`Room_No`),
  CONSTRAINT `Performs_ibfk_4` FOREIGN KEY (`Time`) REFERENCES `Test_or_Surgery` (`Time`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Performs`
--

LOCK TABLES `Performs` WRITE;
/*!40000 ALTER TABLE `Performs` DISABLE KEYS */;
/*!40000 ALTER TABLE `Performs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Prescription`
--

DROP TABLE IF EXISTS `Prescription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Prescription` (
  `Pno` int(11) NOT NULL,
  `Complaint` varchar(255) NOT NULL,
  `Diagnosis` varchar(255) NOT NULL,
  PRIMARY KEY (`Pno`),
  CONSTRAINT `Prescription_ibfk_1` FOREIGN KEY (`Pno`) REFERENCES `Schedules` (`Pno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Prescription`
--

LOCK TABLES `Prescription` WRITE;
/*!40000 ALTER TABLE `Prescription` DISABLE KEYS */;
/*!40000 ALTER TABLE `Prescription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Recommends`
--

DROP TABLE IF EXISTS `Recommends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Recommends` (
  `Pno` int(11) NOT NULL,
  `Med_Name` varchar(255) DEFAULT NULL,
  `Batch_No` int(11) DEFAULT NULL,
  `Bill_No` int(11) NOT NULL,
  `Dosage` int(11) DEFAULT NULL,
  PRIMARY KEY (`Pno`),
  KEY `Med_Name` (`Med_Name`),
  KEY `Bill_No` (`Bill_No`),
  KEY `Batch_No` (`Batch_No`),
  CONSTRAINT `Recommends_ibfk_1` FOREIGN KEY (`Pno`) REFERENCES `Prescription` (`Pno`),
  CONSTRAINT `Recommends_ibfk_2` FOREIGN KEY (`Med_Name`) REFERENCES `Medication` (`Med_Name`),
  CONSTRAINT `Recommends_ibfk_3` FOREIGN KEY (`Bill_No`) REFERENCES `Bill` (`Bill_No`),
  CONSTRAINT `Recommends_ibfk_4` FOREIGN KEY (`Batch_No`) REFERENCES `Medication` (`Batch_No`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Recommends`
--

LOCK TABLES `Recommends` WRITE;
/*!40000 ALTER TABLE `Recommends` DISABLE KEYS */;
/*!40000 ALTER TABLE `Recommends` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Room`
--

DROP TABLE IF EXISTS `Room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Room` (
  `Room_No` int(11) NOT NULL,
  `Location_Floor` int(11) NOT NULL,
  `Location_Block` varchar(255) NOT NULL,
  `Room_Type` varchar(255) NOT NULL,
  `Available` tinyint(1) NOT NULL,
  PRIMARY KEY (`Room_No`),
  KEY `Room_Type` (`Room_Type`),
  CONSTRAINT `Room_ibfk_1` FOREIGN KEY (`Room_Type`) REFERENCES `Room_Pricing` (`Room_Type`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Room`
--

LOCK TABLES `Room` WRITE;
/*!40000 ALTER TABLE `Room` DISABLE KEYS */;
INSERT INTO `Room` VALUES (1,1,'A','General Ward',1);
/*!40000 ALTER TABLE `Room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Room_Pricing`
--

DROP TABLE IF EXISTS `Room_Pricing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Room_Pricing` (
  `Room_Type` varchar(255) NOT NULL,
  `Hourly_Tariff` int(11) DEFAULT NULL,
  PRIMARY KEY (`Room_Type`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Room_Pricing`
--

LOCK TABLES `Room_Pricing` WRITE;
/*!40000 ALTER TABLE `Room_Pricing` DISABLE KEYS */;
INSERT INTO `Room_Pricing` VALUES ('General Ward',2000);
/*!40000 ALTER TABLE `Room_Pricing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Schedules`
--

DROP TABLE IF EXISTS `Schedules`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Schedules` (
  `Staff_Id` int(11) NOT NULL,
  `Time` time NOT NULL,
  `Date` date NOT NULL,
  `Pno` int(11) NOT NULL,
  `Patient_Id` int(11) NOT NULL,
  `Duration` varchar(255) NOT NULL,
  PRIMARY KEY (`Pno`),
  KEY `Staff_Id` (`Staff_Id`),
  KEY `Time` (`Time`),
  KEY `Patient_Id` (`Patient_Id`),
  KEY `Date` (`Date`),
  CONSTRAINT `Schedules_ibfk_1` FOREIGN KEY (`Staff_Id`) REFERENCES `Doctor` (`Staff_Id`),
  CONSTRAINT `Schedules_ibfk_2` FOREIGN KEY (`Time`) REFERENCES `Appointment` (`Time`),
  CONSTRAINT `Schedules_ibfk_3` FOREIGN KEY (`Patient_Id`) REFERENCES `Patient` (`Patient_Id`),
  CONSTRAINT `Schedules_ibfk_4` FOREIGN KEY (`Date`) REFERENCES `Appointment` (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Schedules`
--

LOCK TABLES `Schedules` WRITE;
/*!40000 ALTER TABLE `Schedules` DISABLE KEYS */;
INSERT INTO `Schedules` VALUES (374598,'12:00:00','2020-09-09',97460,399815,'15');
/*!40000 ALTER TABLE `Schedules` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Shift`
--

DROP TABLE IF EXISTS `Shift`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Shift` (
  `Staff_Id` int(11) NOT NULL,
  `Shift_Start_Time` time NOT NULL,
  `Shift_End_Time` time NOT NULL,
  `Shift_Day` varchar(255) NOT NULL,
  PRIMARY KEY (`Staff_Id`,`Shift_Start_Time`,`Shift_End_Time`,`Shift_Day`),
  CONSTRAINT `Shift_ibfk_1` FOREIGN KEY (`Staff_Id`) REFERENCES `Staff` (`Staff_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Shift`
--

LOCK TABLES `Shift` WRITE;
/*!40000 ALTER TABLE `Shift` DISABLE KEYS */;
INSERT INTO `Shift` VALUES (374598,'11:00:00','17:00:00','Monday');
INSERT INTO `Shift` VALUES (554380,'08:00:00','16:00:00','Thursday'),(554380,'09:00:00','18:00:00','Saturday'),(554380,'14:00:00','22:00:00','Tuesday'),(983313,'08:00:00','16:00:00','Monday'),(983313,'08:00:00','16:00:00','Wednesday'),(983313,'13:00:00','21:00:00','Friday');
/*!40000 ALTER TABLE `Shift` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Specialisation`
--

DROP TABLE IF EXISTS `Specialisation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Specialisation` (
  `Staff_Id` int(11) NOT NULL,
  `Expertise_Area` varchar(255) NOT NULL,
  PRIMARY KEY (`Staff_Id`,`Expertise_Area`),
  CONSTRAINT `Specialisation_ibfk_1` FOREIGN KEY (`Staff_Id`) REFERENCES `Doctor` (`Staff_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Specialisation`
--

LOCK TABLES `Specialisation` WRITE;
/*!40000 ALTER TABLE `Specialisation` DISABLE KEYS */;
INSERT INTO `Specialisation` VALUES (374598,'ENT');
INSERT INTO `Specialisation` VALUES (554380,'ENT'),(983313,'Dermatology'),(983313,'ENT');
/*!40000 ALTER TABLE `Specialisation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Staff`
--

DROP TABLE IF EXISTS `Staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Staff` (
  `Staff_Id` int(11) NOT NULL,
  `First_Name` varchar(255) NOT NULL,
  `Last_Name` varchar(255) NOT NULL,
  `Sex` char(1) NOT NULL,
  `Salary` int(11) NOT NULL,
  `Contact_No` bigint(20) DEFAULT NULL,
  `Date_Of_Birth` date NOT NULL,
  `H_No` int(11) DEFAULT NULL,
  `Street` varchar(255) DEFAULT NULL,
  `Zipcode` int(11) DEFAULT NULL,
  `City` varchar(255) DEFAULT NULL,
  `Job` varchar(255) NOT NULL,
  `Supervisor_Id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Staff_Id`),
  KEY `Supervisor_Id` (`Supervisor_Id`),
  CONSTRAINT `Staff_ibfk_1` FOREIGN KEY (`Supervisor_Id`) REFERENCES `Doctor` (`Staff_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Staff`
--

LOCK TABLES `Staff` WRITE;
/*!40000 ALTER TABLE `Staff` DISABLE KEYS */;
INSERT INTO `Staff` VALUES (374598,'Joe','Mama','M',100000,1234567890,'1973-07-14',12,'3',201019,'','Doctor',NULL);
INSERT INTO `Staff` VALUES (554380,'Dayitva','Goel','M',15000,9267402764,'2001-01-01',NULL,'',NULL,'','Doctor',983313),(983313,'Shaurya','Dewan','M',25000,9652676483,'2001-09-18',NULL,'',NULL,'','Doctor',NULL);
/*!40000 ALTER TABLE `Staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Stays_In`
--

DROP TABLE IF EXISTS `Stays_In`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Stays_In` (
  `Bill_No` int(11) NOT NULL,
  `Patient_Id` int(11) NOT NULL,
  `Room_No` int(11) NOT NULL,
  `Duration` int(11) NOT NULL,
  PRIMARY KEY (`Bill_No`),
  KEY `Patient_Id` (`Patient_Id`),
  KEY `Room_No` (`Room_No`),
  CONSTRAINT `Stays_in_ibfk_1` FOREIGN KEY (`Bill_No`) REFERENCES `Bill` (`Bill_No`),
  CONSTRAINT `Stays_in_ibfk_2` FOREIGN KEY (`Patient_Id`) REFERENCES `Patient` (`Patient_Id`),
  CONSTRAINT `Stays_in_ibfk_3` FOREIGN KEY (`Room_No`) REFERENCES `Room` (`Room_No`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Stays_In`
--

LOCK TABLES `Stays_In` WRITE;
/*!40000 ALTER TABLE `Stays_In` DISABLE KEYS */;
/*!40000 ALTER TABLE `Stays_In` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Supplier_Details`
--

DROP TABLE IF EXISTS `Supplier_Details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Supplier_Details` (
  `Supplier_Id` int(11) NOT NULL,
  `Supplier_Name` varchar(255) NOT NULL,
  PRIMARY KEY (`Supplier_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Supplier_Details`
--

LOCK TABLES `Supplier_Details` WRITE;
/*!40000 ALTER TABLE `Supplier_Details` DISABLE KEYS */;
INSERT INTO `Supplier_Details` VALUES (14,'Vespers');
/*!40000 ALTER TABLE `Supplier_Details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Test_Pricing`
--

DROP TABLE IF EXISTS `Test_Pricing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Test_Pricing` (
  `Type` varchar(255) NOT NULL,
  `Cost` float NOT NULL,
  PRIMARY KEY (`Type`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Test_Pricing`
--

LOCK TABLES `Test_Pricing` WRITE;
/*!40000 ALTER TABLE `Test_Pricing` DISABLE KEYS */;
INSERT INTO `Test_Pricing` VALUES ('Blood Test',500);
/*!40000 ALTER TABLE `Test_Pricing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Test_or_Surgery`
--

DROP TABLE IF EXISTS `Test_or_Surgery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Test_or_Surgery` (
  `Date` date NOT NULL,
  `Time` time NOT NULL,
  `Duration` varchar(255) NOT NULL,
  `Type` varchar(255) NOT NULL,
  `Result` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`,`Time`),
  KEY `Type` (`Type`),
  KEY `Time` (`Time`),
  CONSTRAINT `Test_or_Surgery_ibfk_1` FOREIGN KEY (`Type`) REFERENCES `Test_Pricing` (`Type`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Test_or_Surgery`
--

LOCK TABLES `Test_or_Surgery` WRITE;
/*!40000 ALTER TABLE `Test_or_Surgery` DISABLE KEYS */;
/*!40000 ALTER TABLE `Test_or_Surgery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Works_In`
--

DROP TABLE IF EXISTS `Works_In`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Works_In` (
  `Staff_Id` int(11) NOT NULL,
  `Dno` int(11) NOT NULL,
  PRIMARY KEY (`Staff_Id`),
  KEY `Dno` (`Dno`),
  CONSTRAINT `Works_In_ibfk_1` FOREIGN KEY (`Staff_Id`) REFERENCES `Doctor` (`Staff_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Works_In`
--

LOCK TABLES `Works_In` WRITE;
/*!40000 ALTER TABLE `Works_In` DISABLE KEYS */;
INSERT INTO `Works_In` VALUES (374598,12);
INSERT INTO `Works_In` VALUES (554380,1),(983313,1);
/*!40000 ALTER TABLE `Works_In` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-06 12:39:12
