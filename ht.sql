/*
Navicat MySQL Data Transfer

Source Server         : 5656
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : weibo

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2018-04-4 13:38:46
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for gjc
-- ----------------------------
DROP TABLE IF EXISTS `ht`;
CREATE TABLE `ht` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) DEFAULT NULL,
  `content` text,
  `post_time` varchar(255) DEFAULT NULL,
  `zf` int(10) DEFAULT NULL,
  `num_zan` int(10) DEFAULT NULL,
  `num_forw` int(10) DEFAULT NULL,
  `num_comm` int(10) DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
