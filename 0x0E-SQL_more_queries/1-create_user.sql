-- Create user with all privileges and password setted
CREATE USER
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT PRIVILEGES
    ON *.*
    TO 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;
