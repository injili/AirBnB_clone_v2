-- a script that prepares a MySQL server for the project
-- create a database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grant SELECT permissions
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
