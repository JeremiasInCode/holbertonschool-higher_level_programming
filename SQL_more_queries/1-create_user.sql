-- script that creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' identified by 'user_0d_1_pwd';
GRANT ALL ON hbtn_0c_0.* TO user_0d_1@localhost;