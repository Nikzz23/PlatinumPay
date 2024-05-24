# PlatinumPay 
###### Created by Nikolas Jon T. Peña | M001 - CP102

## Description
* PlatinumPay is your go-to user-friendly E-Wallet, offering seamless transactions with other users along with effortless deposits and withdrawals. With a sleek and modern user interface, navigating through PlatinumPay is a breeze, making your financial management experience a delight. Whether you're splitting bills with friends or managing your finances on the fly, PlatinumPay simplifies your digital transactions, empowering you to stay in control of your money with ease.

## Internal

### MySQL Tables
<div align="center">
	<img src="https://github.com/Nikzz23/PlatinumPay/assets/114866835/89261f2b-a223-4394-8212-c232b40ed2e2">
  <p>table1. User Login Data</p>
</div>

* tblUserLoginData(
id varchar(20) not null primary key,
username varchar(50) not null,
password varchar(60) null); 

<div align="center">
	<img src="https://github.com/Nikzz23/PlatinumPay/assets/114866835/632cb45c-8a1e-4689-a619-4417e1d8b1c5">
  <p>table2. User Balance</p>
</div>

* tblUserbalance(
id varchar(20) not null primary key,
balance float not null,
FOREIGN KEY (id) REFERENCES tbluserlogindata(id)
);

<div align="center">
	<img src="https://github.com/Nikzz23/PlatinumPay/assets/114866835/e084028d-d085-4ddc-bacd-c2e55601840e">
  <p>table3. User Personal Information</p>
</div>

* tbluserpersonalinformation(
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

<div align="center">
	<img src="https://github.com/Nikzz23/PlatinumPay/assets/114866835/c0e37057-fc3d-4915-a2cc-96cfdb5fa8d6">
  <p>table4. Users Transaction History</p>
</div>

* transaction_history (
transaction_id INT AUTO_INCREMENT PRIMARY KEY,
id varchar(20) not null,
transaction_type VARCHAR(20) NOT NULL,
amount DECIMAL(10, 2) NOT NULL,
timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
related_user_id varchar(20) not null
);

<div align="center">
	<img src="https://github.com/Nikzz23/PlatinumPay/assets/114866835/a0d2c465-2fe9-49ba-aa91-9f1357642d03">
  <p>table5. User number ID tracker</p>
</div>

* tblUserIDTracker (
    id INT PRIMARY KEY AUTO_INCREMENT,
    last_user_number INT NOT NULL
);

## MySQL
* Link: https://github.com/Nikzz23/PlatinumPay/blob/564f15df997e00941e8ced7f70b314f1cdbc715c/MySQL/userdatabase.sql
```
# CREATING DATABSE
Create Database userData;

# CREATING TABLES
Create Table tblUserLoginData(
id varchar(20) not null primary key,
username varchar(50) not null,
password varchar(60) null); 

Create Table tblUserbalance(
id varchar(20) not null primary key,
balance float not null,
FOREIGN KEY (id) REFERENCES tbluserlogindata(id)
);

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

CREATE TABLE transaction_history (
transaction_id INT AUTO_INCREMENT PRIMARY KEY,
id varchar(20) not null,
transaction_type VARCHAR(20) NOT NULL,
amount DECIMAL(10, 2) NOT NULL,
timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
related_user_id varchar(20) not null
);

CREATE TABLE tblUserIDTracker (
    id INT PRIMARY KEY AUTO_INCREMENT,
    last_user_number INT NOT NULL
);

# CHANGES/ MODIFICATION
-- select * from tbluserlogindata;
-- Delete from tbluserlogindata where id = 'U24-0005';

-- insert tblUserLoginData values
-- ('U24-0001', 'user1234', '12345678');

-- insert tblUserLoginData values
-- ('U24-0002', 'usersample2', '12345678');

-- SELECT username FROM tblUserLoginData WHERE id = 'U24-0001';

-- drop table tbluserbalance;

-- select * from tbluserbalance;
-- Delete from tbluserbalance where id = 'U24-0005';

-- insert tbluserbalance values
-- ('U24-0001', 120.00);

-- insert tbluserbalance values
-- ('U24-0002', 50.00);

-- insert tbluserpersonalinformation values
-- ('U24-0001', 'Nikolas Jon', 'Tolentino', 'Peña', '01/25/2005', 'Filipino', 'mypersonalemail@gmail.com', 'Executive Village, Mayao Kanluran, Quezon, Philippines');

-- Update tbluserpersonalinformation Set birthdate = '25/01/2005'  Where id = 'U24-0001';
-- Update tbluserpersonalinformation Set birthdate = '05/08/1999'  Where id = 'U24-0002';

-- insert tbluserpersonalinformation values
-- ('U24-0002', 'John', 'Mark', 'Doe', '05/8/1999', 'Filipino', 'mypersonalemail2@gmail.com', 'Calmar, Mayao Kanluran, Quezon, Philippines');

-- select * from tbluserpersonalinformation;

-- Delete from tbluserpersonalinformation where id = 'U24-0005';

-- SELECT firstname,middlename,lastname FROM tbluserpersonalinformation WHERE id = 'U24-0001';

-- SELECT CONCAT(firstname, ' ', COALESCE(lastname, '')) AS fullname
-- FROM tbluserpersonalinformation
-- WHERE id = 'U24-0001';

-- SELECT transaction_type, amount FROM transaction_history WHERE id = 'U24-0001' order by timestamp DESC limit 3;

-- select * from transaction_history;
-- DELETE FROM transaction_history WHERE transaction_id = 2;

-- UPDATE transaction_history SET related_user_id = 'null' WHERE related_user_id = 'International Banks';

-- select * from tblUserIDTracker;
-- insert tbluseridtracker values
-- (1, 2);

-- UPDATE tblUserIDTracker SET last_user_number = 2 WHERE id = 1;
```

## Python Source Code
* Link: https://github.com/Nikzz23/PlatinumPay/blob/564f15df997e00941e8ced7f70b314f1cdbc715c/Python/realmain.py 

## Executing the system





