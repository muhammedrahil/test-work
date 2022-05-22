/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - dgold
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`dgold` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `dgold`;

/*Table structure for table `employee` */

DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
  `emp_id` int(10) NOT NULL AUTO_INCREMENT,
  `emp_name` varchar(50) DEFAULT NULL,
  `e-code` varchar(20) DEFAULT NULL,
  `branch` varchar(50) DEFAULT NULL,
  `loginid` int(10) DEFAULT NULL,
  PRIMARY KEY (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=120 DEFAULT CHARSET=latin1;

/*Data for the table `employee` */

insert  into `employee`(`emp_id`,`emp_name`,`e-code`,`branch`,`loginid`) values 
(1,'ALI AKBAR MV','1072','Valanchery',3),
(2,'MUHAMMED JAFAR','1085','Valanchery',4),
(3,'MUHAMMED ADIL','1113','Valanchery',5),
(4,'JAYARAJ','1123','Valanchery',6),
(5,'GOUTHAMI','1174','Valanchery',7),
(6,'VIGIN','1179','Valanchery',8),
(7,'SAMEER','1186','Valanchery',9),
(8,'NIZAMUDHEEN P','1189','Valanchery',10),
(9,'VALSALA','1206','Valanchery',11),
(10,'VIJEESH T    ','1212','Valanchery',12),
(11,'MOIDEEN KUTTY','1220','Valanchery',13),
(12,'RAMSHAD KT','1243','Valanchery',14),
(13,'ABOOBACKER','1149','Valanchery',15),
(14,'MUHAMMED SHAKKEER P','1249','Valanchery',16),
(15,'ABDUL BASITH PP','1251','Valanchery',17),
(16,'SREELAKSHMI K','1253','Valanchery',18),
(17,'MUHAMMED JABIR ','1258','Valanchery',19),
(18,'AJMAL PV','1260','Valanchery',20),
(19,'RASHID','1261','Valanchery',21),
(20,'FAROOK','1262','Valanchery',22),
(21,'NADEER ABDUL HAZEEB K','1263','Valanchery',23),
(22,'SISHANT','1248','Valanchery',24),
(23,'IMBICHU','1241','Valanchery',25),
(24,'SUHAIL','1265','Valanchery',26),
(25,'SHABEER MGR','1269','Valanchery',27),
(26,'VANAJA P','1268','Valanchery',28),
(27,'ABDUL ASEEZ','D001','Ramanatukara',29),
(28,'BIBINRAJ','1012','Ramanatukara',30),
(29,'NOUFAL','1023','Ramanatukara',31),
(30,'PRAJITHA MANOJ','1024','Ramanatukara',32),
(31,'REENA','1027','Ramanatukara',33),
(32,'MUNEER','1044','Ramanatukara',34),
(33,'CHANDRASHEKARAN','1051','Ramanatukara',35),
(34,'SHIJIN','1101','Ramanatukara',36),
(35,'HIMESH','1111','Ramanatukara',37),
(36,'UDAYAKUMAR','1116','Ramanatukara',38),
(37,'ROBIN','1117','Ramanatukara',39),
(38,'ABUDUJANATHULLA','1122','Ramanatukara',40),
(39,'SHARATH','1127','Ramanatukara',41),
(40,'JISHA','1136','Ramanatukara',42),
(41,'NIDHEESH','1148','Ramanatukara',43),
(42,'MUSTAK','1150','Ramanatukara',44),
(43,'BINSHAD AHAMMED ALI','1151','Ramanatukara',45),
(44,'ARSHAD KV','1155','Ramanatukara',46),
(45,'MUHAMMED SWADIK A','1158','Ramanatukara',47),
(46,'SHAHINA PA','1159','Ramanatukara',48),
(47,'AMITH','1160','Ramanatukara',49),
(48,'ANSAL THOMAS','1162','Ramanatukara',50),
(49,'JABIR','1170','Ramanatukara',51),
(50,'ASHURAHANA','1172','Ramanatukara',52),
(51,'NIKHIL M','1174','Ramanatukara',53),
(52,'MUHAMMED SHAREEF','1176','Ramanatukara',54),
(53,'RAHUL KN','1178','Ramanatukara',55),
(54,'FAHAD K','1179','Ramanatukara',56),
(55,'MUHAMMED RASHID P','1003','Perinthalmanna',57),
(56,'JUFAIL THAYYIL','1006','Perinthalmanna',58),
(57,'MOHAMMED AJMAL','1048','Perinthalmanna',59),
(58,'VIJEESH KP','1049','Perinthalmanna',60),
(59,'RASHEED','1058','Perinthalmanna',61),
(60,'SHAFEEQ','1063','Perinthalmanna',62),
(61,'RAJAN VT','1064','Perinthalmanna',63),
(62,'NIZAMUDEEN','1072','Perinthalmanna',64),
(63,'ANSARI','1075','Perinthalmanna',65),
(64,'FASAL','1077','Perinthalmanna',66),
(65,'RASHMI K','1090','Perinthalmanna',67),
(66,'SUHAIL','1105','Perinthalmanna',68),
(67,'SHEEBA','1109','Perinthalmanna',69),
(68,'SAI KUMAR','1122','Perinthalmanna',70),
(69,'GIREESH','1126','Perinthalmanna',71),
(70,'JOHNSON','1129','Perinthalmanna',72),
(71,'AKBAR','1131','Perinthalmanna',73),
(72,'SHINIL','1132','Perinthalmanna',74),
(73,'ANAS','1137','Perinthalmanna',75),
(74,'MUHAMMED JALAL','1149','Perinthalmanna',76),
(75,'NOUFAL','1152','Perinthalmanna',77),
(76,'JIJI','1153','Perinthalmanna',78),
(77,'ANWAR SADATH','1155','Perinthalmanna',79),
(78,'MOHAMMED ARSHAD','1158','Perinthalmanna',80),
(79,'VISHNURAJ','1159','Perinthalmanna',81),
(80,'ANSULA','1160','Perinthalmanna',82),
(81,'NAJEEB','1164','Perinthalmanna',83),
(82,'MOHD RASHAD','1165','Perinthalmanna',84),
(83,'MUBEENA','1166','Perinthalmanna',85),
(84,'JIJIN','1167','Perinthalmanna',86),
(85,'ANEESUDHEEN','1170','Perinthalmanna',87),
(86,'RAJANI ','1171','Perinthalmanna',88),
(87,'MOHAMMED FAYIZ EK','D001','Pattambi',89),
(88,'NOUFAL','1022','Pattambi',90),
(89,'JAMSHEER A','1013','Pattambi',91),
(90,'NABEEL AP','1019','Pattambi',92),
(91,'ABDUL RASHEED K','1031','Pattambi',93),
(92,'RANJITH PK','1030','Pattambi',94),
(93,'SAILAJA C','1036','Pattambi',95),
(94,'VINOD U','1047','Pattambi',96),
(95,'ASIYA PK','1048','Pattambi',97),
(96,'SUBRAMANIAN P','1054','Pattambi',98),
(97,'SHAMEER P','1094','Pattambi',99),
(98,'SHARFUDHEEN V','1073','Pattambi',100),
(99,'NOUFAL S','1128','Pattambi',101),
(100,'AMEER MALIK M','1102','Pattambi',102),
(101,'SHARAFUDHEEN','1141','Pattambi',103),
(102,'SHAMEER K','1105','Pattambi',104),
(103,'MUHAMMED ANSHAF','1157','Pattambi',105),
(104,'MANOJ ','1162','Pattambi',106),
(105,'ABDUL SALAM','1126','Pattambi',107),
(106,'MUHAMMED SHEREEF T','1134','Pattambi',108),
(107,'MUHAMMED NUSHAD KP','1112','Pattambi',109),
(108,'ANEES MOIDU','1147','Pattambi',110),
(109,'ARSHAD VP','1132','Pattambi',111),
(110,'MUHAMMED SHIHAB P','1169','Pattambi',112),
(111,'MUSTHAQ TT','1110','Pattambi',113),
(112,'MOHAMMED SHIBILI','1167','Pattambi',114),
(113,'VINOD KUMAR V','1164','Pattambi',115),
(114,'MUHAMMED MANSOOR','1131','Pattambi',116),
(115,'SMITHA','1158','Pattambi',117),
(116,'PRAVEEN MS ','1168','Pattambi',118),
(117,'KUNJU MUHAMMED ','1144','Pattambi',119),
(118,'ANJALI P','1170','Pattambi',120),
(119,'NISHAD K','1129','Pattambi',121);

/*Table structure for table `leaverequest` */

DROP TABLE IF EXISTS `leaverequest`;

CREATE TABLE `leaverequest` (
  `LRid` int(10) NOT NULL AUTO_INCREMENT,
  `reason` varchar(100) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `lg_id` int(10) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `expDate` date DEFAULT NULL,
  `applyDate` date DEFAULT NULL,
  PRIMARY KEY (`LRid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `leaverequest` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `loginid` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `ecode` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`loginid`,`username`,`ecode`,`usertype`) values 
(1,'director','dgold@2022','director'),
(2,'manager','dgold@M','manager'),
(3,'ALI AKBAR MV','1072','employee'),
(4,'MUHAMMED JAFAR','1085','employee'),
(5,'MUHAMMED ADIL','1113','employee'),
(6,'JAYARAJ','1123','employee'),
(7,'GOUTHAMI','1174','employee'),
(8,'VIGIN','1179','employee'),
(9,'SAMEER','1186','employee'),
(10,'NIZAMUDHEEN P','1189','employee'),
(11,'VALSALA','1206','employee'),
(12,'VIJEESH T    ','1212','employee'),
(13,'MOIDEEN KUTTY','1220','employee'),
(14,'RAMSHAD KT','1243','employee'),
(15,'ABOOBACKER','1149','employee'),
(16,'MUHAMMED SHAKKEER P','1249','employee'),
(17,'ABDUL BASITH PP','1251','employee'),
(18,'SREELAKSHMI K','1253','employee'),
(19,'MUHAMMED JABIR ','1258','employee'),
(20,'AJMAL PV','1260','employee'),
(21,'RASHID','1261','employee'),
(22,'FAROOK','1262','employee'),
(23,'NADEER ABDUL HAZEEB K','1263','employee'),
(24,'SISHANT','1248','employee'),
(25,'IMBICHU','1241','employee'),
(26,'SUHAIL','1265','employee'),
(27,'SHABEER MGR','1269','employee'),
(28,'VANAJA P','1268','employee'),
(29,'ABDUL ASEEZ','D001','employee'),
(30,'BIBINRAJ','1012','employee'),
(31,'NOUFAL','1023','employee'),
(32,'PRAJITHA MANOJ','1024','employee'),
(33,'REENA','1027','employee'),
(34,'MUNEER','1044','employee'),
(35,'CHANDRASHEKARAN','1051','employee'),
(36,'SHIJIN','1101','employee'),
(37,'HIMESH','1111','employee'),
(38,'UDAYAKUMAR','1116','employee'),
(39,'ROBIN','1117','employee'),
(40,'ABUDUJANATHULLA','1122','employee'),
(41,'SHARATH','1127','employee'),
(42,'JISHA','1136','employee'),
(43,'NIDHEESH','1148','employee'),
(44,'MUSTAK','1150','employee'),
(45,'BINSHAD AHAMMED ALI','1151','employee'),
(46,'ARSHAD KV','1155','employee'),
(47,'MUHAMMED SWADIK A','1158','employee'),
(48,'SHAHINA PA','1159','employee'),
(49,'AMITH','1160','employee'),
(50,'ANSAL THOMAS','1162','employee'),
(51,'JABIR','1170','employee'),
(52,'ASHURAHANA','1172','employee'),
(53,'NIKHIL M','1174','employee'),
(54,'MUHAMMED SHAREEF','1176','employee'),
(55,'RAHUL KN','1178','employee'),
(56,'FAHAD K','1179','employee'),
(57,'MUHAMMED RASHID P','1003','employee'),
(58,'JUFAIL THAYYIL','1006','employee'),
(59,'MOHAMMED AJMAL','1048','employee'),
(60,'VIJEESH KP','1049','employee'),
(61,'RASHEED','1058','employee'),
(62,'SHAFEEQ','1063','employee'),
(63,'RAJAN VT','1064','employee'),
(64,'NIZAMUDEEN','1072','employee'),
(65,'ANSARI','1075','employee'),
(66,'FASAL','1077','employee'),
(67,'RASHMI K','1090','employee'),
(68,'SUHAIL','1105','employee'),
(69,'SHEEBA','1109','employee'),
(70,'SAI KUMAR','1122','employee'),
(71,'GIREESH','1126','employee'),
(72,'JOHNSON','1129','employee'),
(73,'AKBAR','1131','employee'),
(74,'SHINIL','1132','employee'),
(75,'ANAS','1137','employee'),
(76,'MUHAMMED JALAL','1149','employee'),
(77,'NOUFAL','1152','employee'),
(78,'JIJI','1153','employee'),
(79,'ANWAR SADATH','1155','employee'),
(80,'MOHAMMED ARSHAD','1158','employee'),
(81,'VISHNURAJ','1159','employee'),
(82,'ANSULA','1160','employee'),
(83,'NAJEEB','1164','employee'),
(84,'MOHD RASHAD','1165','employee'),
(85,'MUBEENA','1166','employee'),
(86,'JIJIN','1167','employee'),
(87,'ANEESUDHEEN','1170','employee'),
(88,'RAJANI ','1171','employee'),
(89,'MOHAMMED FAYIZ EK','D001','employee'),
(90,'NOUFAL','1022','employee'),
(91,'JAMSHEER A','1013','employee'),
(92,'NABEEL AP','1019','employee'),
(93,'ABDUL RASHEED K','1031','employee'),
(94,'RANJITH PK','1030','employee'),
(95,'SAILAJA C','1036','employee'),
(96,'VINOD U','1047','employee'),
(97,'ASIYA PK','1048','employee'),
(98,'SUBRAMANIAN P','1054','employee'),
(99,'SHAMEER P','1094','employee'),
(100,'SHARFUDHEEN V','1073','employee'),
(101,'NOUFAL S','1128','employee'),
(102,'AMEER MALIK M','1102','employee'),
(103,'SHARAFUDHEEN','1141','employee'),
(104,'SHAMEER K','1105','employee'),
(105,'MUHAMMED ANSHAF','1157','employee'),
(106,'MANOJ ','1162','employee'),
(107,'ABDUL SALAM','1126','employee'),
(108,'MUHAMMED SHEREEF T','1134','employee'),
(109,'MUHAMMED NUSHAD KP','1112','employee'),
(110,'ANEES MOIDU','1147','employee'),
(111,'ARSHAD VP','1132','employee'),
(112,'MUHAMMED SHIHAB P','1169','employee'),
(113,'MUSTHAQ TT','1110','employee'),
(114,'MOHAMMED SHIBILI','1167','employee'),
(115,'VINOD KUMAR V','1164','employee'),
(116,'MUHAMMED MANSOOR','1131','employee'),
(117,'SMITHA','1158','employee'),
(118,'PRAVEEN MS ','1168','employee'),
(119,'KUNJU MUHAMMED ','1144','employee'),
(120,'ANJALI P','1170','employee'),
(121,'NISHAD K','1129','employee'),
(125,'coo','dgold@coo','coo');

/*Table structure for table `memo` */

DROP TABLE IF EXISTS `memo`;

CREATE TABLE `memo` (
  `memoid` int(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `memo` longblob,
  `file_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`memoid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `memo` */

/*Table structure for table `pyment` */

DROP TABLE IF EXISTS `pyment`;

CREATE TABLE `pyment` (
  `pid` int(50) NOT NULL AUTO_INCREMENT,
  `catogary` varchar(100) DEFAULT NULL,
  `moneny` varchar(100) DEFAULT NULL,
  `lg_id` int(10) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `pyment` */

/*Table structure for table `target` */

DROP TABLE IF EXISTS `target`;

CREATE TABLE `target` (
  `trid` int(10) NOT NULL AUTO_INCREMENT,
  `gold` varchar(50) DEFAULT NULL,
  `lg_id` int(10) DEFAULT NULL,
  `achive_gold` varchar(100) DEFAULT NULL,
  `Diamond` varchar(100) DEFAULT NULL,
  `achive_diamond` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`trid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `target` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
