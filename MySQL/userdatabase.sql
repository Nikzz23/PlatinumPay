
Create Table tblAdmin(
id varchar(20) not null primary key,
username varchar(50) not null,
password varchar(60) null); 

insert tblAdmin values
('A24-0001', 'admin12345', '12345678');

select * from tblAdmin;

select * from tbluserlogindata;
Delete from tbluserlogindata where id = 'U24-0005';

Create Database userData;

Create Table tblUserLoginData(
id varchar(20) not null primary key,
username varchar(50) not null,
password varchar(60) null); 

insert tblUserLoginData values
('U24-0001', 'user1234', '12345678');

insert tblUserLoginData values
('U24-0002', 'usersample2', '12345678');

Create Table tblUserTransaction(
id varchar(20) not null primary key,
date varchar(50) not null,
password varchar(60) null); 

SELECT username FROM tblUserLoginData WHERE id = 'U24-0001';

Create Table tblUserbalance(
id varchar(20) not null primary key,
balance float not null,
FOREIGN KEY (id) REFERENCES tbluserlogindata(id)
);

-- drop table tbluserbalance;

select * from tbluserbalance;
Delete from tbluserbalance where id = 'U24-0005';

insert tbluserbalance values
('U24-0001', 120.00);

insert tbluserbalance values
('U24-0002', 50.00);

Create Table tbluserpersonalinformation(
id varchar(20) not null primary key,
firstname varchar(50) not null,
middlename varchar(50),
lastname varchar(50) not null,
birthdate varchar(50) not null,
nationality varchar(50) not null,
emailaddress varchar(100) not null,
homeaddress varchar(150) not null,
FOREIGN KEY (id) REFERENCES tbluserlogindata(id)
);

insert tbluserpersonalinformation values
('U24-0001', 'Nikolas Jon', 'Tolentino', 'Peña', '01/25/2005', 'Filipino', 'mypersonalemail@gmail.com', 'Executive Village, Mayao Kanluran, Quezon, Philippines');

Update tbluserpersonalinformation Set birthdate = '25/01/2005'  Where id = 'U24-0001';
Update tbluserpersonalinformation Set birthdate = '05/08/1999'  Where id = 'U24-0002';

insert tbluserpersonalinformation values
('U24-0002', 'John', 'Mark', 'Doe', '05/8/1999', 'Filipino', 'mypersonalemail2@gmail.com', 'Calmar, Mayao Kanluran, Quezon, Philippines');

select * from tbluserpersonalinformation;

Delete from tbluserpersonalinformation where id = 'U24-0005';

SELECT firstname,middlename,lastname FROM tbluserpersonalinformation WHERE id = 'U24-0001';

SELECT CONCAT(firstname, ' ', COALESCE(lastname, '')) AS fullname
FROM tbluserpersonalinformation
WHERE id = 'U24-0001';

CREATE TABLE transaction_history (
transaction_id INT AUTO_INCREMENT PRIMARY KEY,
id varchar(20) not null,
transaction_type VARCHAR(20) NOT NULL,
amount DECIMAL(10, 2) NOT NULL,
timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
related_user_id varchar(20) not null
);

SELECT transaction_type, amount FROM transaction_history WHERE id = 'U24-0001' order by timestamp DESC limit 3;

select * from transaction_history;
DELETE FROM transaction_history WHERE transaction_id = 2;

UPDATE transaction_history SET related_user_id = 'null' WHERE related_user_id = 'International Banks';

CREATE TABLE tblUserIDTracker (
    id INT PRIMARY KEY AUTO_INCREMENT,
    last_user_number INT NOT NULL
);

select * from tblUserIDTracker;
insert tbluseridtracker values
(1, 2);

UPDATE tblUserIDTracker SET last_user_number = 2 WHERE id = 1;