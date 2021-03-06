DROP DATABASE IF EXISTS websiteDB;

CREATE DATABASE websiteDB;

USE websiteDB;

/*Table structure for table customers */

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
  customerId int(11) NOT NULL AUTO_INCREMENT,
  firstName varchar(20) DEFAULT NULL,
  lastName varchar(20) DEFAULT NULL,
  emailAddress varchar(50) DEFAULT NULL,
  phoneNumber varchar(12) DEFAULT NULL,
  address varchar(50) DEFAULT NULL,
  city varchar(20) DEFAULT NULL,
  PRIMARY KEY (customerId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table customers */

INSERT INTO customers VALUES
(72391,'Alex','Delgado','alexdel413@gmail.com','720-242-7210','11355 livingston dr','Northglenn'),
(72324,'Hector','Marin','HectorMar425@gmail.com','303-808-3003','1203 love st','Littleton'),
(72384,'Allen','Reyes','Allen424@gmail.com','720-242-6126','820 28th st','Boulder'),
(0,'Test','User','Test@gmail.com','555-555-5555','test address','Boulder'),
(0,'Hell','Boy','Test@gmail.com','666-666-6666','Schlecht Strasse','Hell');

/*Table structure for table orders */

DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
  orderId int(11) NOT NULL AUTO_INCREMENT,
  orderDate DATE DEFAULT NULL,
  description varchar(500) DEFAULT NULL,
  status varchar(10) DEFAULT NULL,
  customerId int(11) DEFAULT NULL,
  PRIMARY KEY (orderId),
  KEY customerId (customerId),
  CONSTRAINT orders_ibfk_1 FOREIGN KEY (customerId) REFERENCES customers (customerId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table orders */

INSERT INTO orders VALUES
(1151423,'2017-04-13','Sidewalk Replacement','Complete',72391),
(1234123,'2017-08-20','Cement Patio','Initial',72324),
(5657475,'2017-10-20','Driveway Replacement','Ongoing',72384),
(0,CURDATE(),'Test Description','Initial',72392),
(1111111,CURDATE(),'Concrete Stuff','Ongoing',72393);

/*Table structure for table users */

DROP TABLE IF EXISTS users;

CREATE TABLE users (
  userId int(11) NOT NULL AUTO_INCREMENT,
  userType varchar(50) DEFAULT NULL,
  username varchar(100) NOT NULL,
  password varchar(100) NOT NULL,
  PRIMARY KEY (userId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table users */

INSERT INTO users VALUES
(0,'Admin','Admin','123');

/*Table structure for table reviews */

DROP TABLE IF EXISTS reviews;

CREATE TABLE reviews (
  reviewId int(11) NOT NULL AUTO_INCREMENT,
  orderId int(11) DEFAULT NULL,
  description varchar(140) DEFAULT NULL,
  starCount int(1) DEFAULT NULL,
  PRIMARY KEY (reviewId),
  KEY orderId (orderId),
  CONSTRAINT reviews_ibfk_1 FOREIGN KEY (orderId) REFERENCES orders (orderId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table orders */

INSERT INTO reviews VALUES
(0,1151423,'Nice website, keep up the good work!',5),
(0,1234123,'A+ service, would recommend!',5),
(0,5657475,'PHAT Patio!',5),
(0,5657476,'Good Work',4);