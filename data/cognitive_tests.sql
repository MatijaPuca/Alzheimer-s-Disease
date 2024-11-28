CREATE TABLE `cognitive_tests` (
  `test_id` int NOT NULL AUTO_INCREMENT,
  `patient_id` bigint DEFAULT NULL,
  `test_answer` varchar(255) DEFAULT NULL,
  `date_taken` datetime DEFAULT NULL,
  PRIMARY KEY (`test_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
