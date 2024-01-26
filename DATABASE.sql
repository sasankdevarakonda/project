/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.1.13-MariaDB : Database - healthcare_sector
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`healthcare_sector` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `healthcare_sector`;

/*Table structure for table `book_slot` */

DROP TABLE IF EXISTS `book_slot`;

CREATE TABLE `book_slot` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `dname` varchar(100) DEFAULT NULL,
  `demail` varchar(100) DEFAULT NULL,
  `pname` varchar(100) DEFAULT NULL,
  `pemail` varchar(100) DEFAULT NULL,
  `sym` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'Incomplete',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `book_slot` */

insert  into `book_slot`(`id`,`dname`,`demail`,`pname`,`pemail`,`sym`,`date`,`status`) values (3,'LAKSHMI','lakshmi@gmail.com','RUPESH','cse.takeoff@gmail.com','fever','2021-04-22','Completed');

/*Table structure for table `doctor` */

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `area` varchar(100) DEFAULT NULL,
  `addr` varchar(100) DEFAULT NULL,
  `pno` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `doctor` */

insert  into `doctor`(`id`,`fname`,`lname`,`email`,`pwd`,`area`,`addr`,`pno`) values (2,'LAKSHMI','N','lakshmi@gmail.com','1','cardiologist','tirupati','7896541230');

/*Table structure for table `features` */

DROP TABLE IF EXISTS `features`;

CREATE TABLE `features` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `disp` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `features` */

insert  into `features`(`id`,`email`,`fname`,`disp`) values (2,'lakshmi@gmail.com','feature1','book1');

/*Table structure for table `patient` */

DROP TABLE IF EXISTS `patient`;

CREATE TABLE `patient` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `addr` varchar(100) DEFAULT NULL,
  `pno` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `patient` */

insert  into `patient`(`id`,`fname`,`lname`,`email`,`pwd`,`addr`,`pno`) values (2,'RUPESH','R','cse.takeoff@gmail.com','1','tirupati','6985231470');

/*Table structure for table `report` */

DROP TABLE IF EXISTS `report`;

CREATE TABLE `report` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `rid` int(10) DEFAULT NULL,
  `pname` varchar(100) DEFAULT NULL,
  `pemail` varchar(100) DEFAULT NULL,
  `dname` varchar(100) DEFAULT NULL,
  `demail` varchar(100) DEFAULT NULL,
  `sym` varchar(100) DEFAULT NULL,
  `disp` varchar(100) DEFAULT NULL,
  `report` longblob,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'Incomplete',
  `action` varchar(100) DEFAULT 'pending',
  `pkey` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `report` */

insert  into `report`(`id`,`rid`,`pname`,`pemail`,`dname`,`demail`,`sym`,`disp`,`report`,`date`,`status`,`action`,`pkey`) values (8,3,'RUPESH','cse.takeoff@gmail.com','LAKSHMI','lakshmi@gmail.com','fever','NORMAL','∫&5;Ú‰r3◊Å\r˜z;©˝','2021-04-22','Completed','Close','70b64a85');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
