CREATE DATABASE IF NOT EXISTS `websiteDB`;

USE `websiteDB`;

/*Table structure for table `Customers` */

DROP TABLE IF EXISTS `Customers`;

CREATE TABLE `Customers` (
  `customerId` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(20) DEFAULT NULL,
  `lastName` varchar(20) DEFAULT NULL,
  `phoneNumber` varchar(15) DEFAULT NULL,
  `emailAddress` varchar(50) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`customerId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `Customers` */

INSERT INTO Customers VALUES(0, 'Test', 'User', 3031231234, 'test@test.com', 'Boulder');

/*Table structure for table `Orders` */

DROP TABLE IF EXISTS `Orders`;

CREATE TABLE `Orders` (
  `orderId` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(50) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `orderDate` DATETIME DEFAULT NULL,
  `completion` tinyint(1) DEFAULT NULL,
  `customerId` int(11) DEFAULT NULL,
  PRIMARY KEY (`orderId`),
  KEY `customerId` (`customerId`),
  CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`customerId`) REFERENCES `Customers` (`customerId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `Orders` */

INSERT INTO Orders VALUES(0, 'Test Address', 'Boulder', NOW(), 0, 1);
