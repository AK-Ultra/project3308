/*
SQLyog Community v12.4.3 (64 bit)
MySQL - 5.7.19-log : Database - websitedb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`delconcretedb` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `delconcretedb`;

/*Table structure for table `customerinfo` */

DROP TABLE IF EXISTS `customerinfo`;

CREATE TABLE `customerinfo` (
  `customerID` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(20) DEFAULT NULL,
  `lastName` varchar(20) DEFAULT NULL,
  `emailAddress` varchar(50) DEFAULT NULL,
  `phoneNumber` varchar(12) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  
  PRIMARY KEY (`customerId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into customerinfo (customerID, firstName, lastName, emailAddress, phoneNumber,city) values
(72391,'Alex','Delgado','alexdel413@gmail.com','720-242-7210','Northglenn'),
(72324,'Hector','Marin','HectorMar425@gmail.com','303-808-3003','Littleton'),
(72384,'Allen','Reyes','Allen424@gmail.com','720-242-6126','Boulder');

/*Data for the table `customerinfo` */

/*Table structure for table `orderinfo` */

DROP TABLE IF EXISTS `orderinfo`;

CREATE TABLE `orderinfo` (
  `orderID` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(50) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `orderDate` varchar(11) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `completion` varchar(7) DEFAULT NULL,
  `customerID` int(11) DEFAULT NULL,
  PRIMARY KEY (`orderId`),
  KEY `customerId` (`customerId`),
  CONSTRAINT `orderinfo_ibfk_1` FOREIGN KEY (`customerId`) REFERENCES `customerinfo` (`customerId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into orderinfo (orderID,address,city,orderDate, description,completion,customerID) values
(1151423,'10431 Livingston Dr','Northglenn','4/13/2017','Side Walk replacement','Yes',72391),
(1234123,'11355 Highline Dr','Littleton','8/20/2017','cement patio','No',72324),
(5657475,'820 28th st','Boulder','10/20/2017','driveway replacement','Ongoing',72384);

/*Data for the table `orderinfo` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
