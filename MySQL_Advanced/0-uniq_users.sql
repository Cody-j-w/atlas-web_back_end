-- CREATE USERS TABLE
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT,
    email string(255) NOT NULL,
    name string(255),
    UNIQUE(email),
    PRIMARY KEY(id)
)
