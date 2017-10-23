# make db available through the network
vi /etc/mysql/mysql.conf.d/mysqld.cnf
# comment out the line that has bind = 127.0.0.1
systemctl restart mysql

# installing phpmyadmin
apt-get update
apt-get install phpmyadmin
vi /etc/apach2/apach2.conf
# add this line
Include /etc/phpmyadmin/apache.conf
:wq
systemctl restart apache2 
Now go to ip/phpmyadmin
username and password for database 

# create a new user
CREATE USER 'monty'@'%' IDENTIFIED BY 'some_pass';
GRANT ALL PRIVILEGES ON *.* TO 'monty'@'%'WITH GRANT OPTION;
FLUSH PRIVILEGES;


# also comment out this line
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf #bind-address           = 127.0.0.1

# change password
SET PASSWORD FOR 'hamed'@'%' = PASSWORD('test');


# mysql> show tables;
+----------------------+
| Tables_in_BucketList |
+----------------------+
| tbl_user             |
+uuu----------------------+
1 row in set (0.01 sec)

# mysql> describe tbl_user;
+---------------+-------------+------+-----+---------+----------------+
| Field         | Type        | Null | Key | Default | Extra          |
+---------------+-------------+------+-----+---------+----------------+
| user_id       | bigint(20)  | NO   | PRI | NULL    | auto_increment |
| user_name     | varchar(45) | YES  |     | NULL    |                |
| user_username | varchar(45) | YES  |     | NULL    |                |
| user_password | varchar(45) | YES  |     | NULL    |                |
+---------------+-------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)



# create Stored procedure
```
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUseri`(
    IN p_name VARCHAR(20),
    IN p_username VARCHAR(20),
    IN p_password VARCHAR(20)
)
BEGIN
    if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into tbl_user
        (
            user_name,
            user_username,
            user_password
        )
        values
        (
            p_name,
            p_username,
            p_password
        );
     
    END IF;
END$$
DELIMITER ;
```

# testing
INSERT INTO tbl_user (user_name, User_username,user_password) VALUES ('hamed','hamedh','pass');

# SELECT * from tbl_user;
+---------+-----------+---------------+---------------+
| user_id | user_name | user_username | user_password |
+---------+-----------+---------------+---------------+
|       1 | hamed     | hamedh        | pass          |
+---------+-----------+---------------+---------------+



DELIMITER //
 CREATE PROCEDURE GetAllProducts()
   BEGIN
   SELECT *  FROM tbl_user;
   END //
 DELIMITER ;


# to call a store procedure for mysql
CALL GetAllProducts();
CALL hamed1('test','test','test');


DELIMITER $$
CREATE PROCEDURE pro1(
    IN p_name VARCHAR(20),
    IN p_username VARCHAR(20),
    IN p_password VARCHAR(20)
)
BEGIN
    if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into tbl_user
        (
            user_name,
            user_username,
            user_password
        )
        values
        (
            p_name,
            p_username,
            p_password
        );
     
    END IF;
END$$
DELIMITER ;


