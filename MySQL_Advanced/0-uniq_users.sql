-- CREATE USERS TABLE
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL,
    name varchar(255),
    UNIQUE(email),
    PRIMARY KEY(id)
);
