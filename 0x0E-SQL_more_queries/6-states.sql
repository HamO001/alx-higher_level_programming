-- creates the database hbtn_0d_usa and the table states in db hbtn_0d_usa
-- id INT unique auto generated, can't be null and is a primary key
-- name VARCHAR(256) can't be null
-- if db or table already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states`(
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY(`id`)
);
