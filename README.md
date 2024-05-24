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

### Sign In and User Dashboard
https://github.com/Nikzz23/PlatinumPay/assets/114866835/9cf75b60-5dc6-40fd-bbf5-d5ae3cdd9508

### Sign Up and User Dashboard
https://github.com/Nikzz23/PlatinumPay/assets/114866835/b45bfb7f-bf5a-41df-bcb1-58da5c45790f

### Deposit
https://github.com/Nikzz23/PlatinumPay/assets/114866835/1c1f308b-4c18-4ea5-a4a2-778d4f47e06b

### Transfer
https://github.com/Nikzz23/PlatinumPay/assets/114866835/9b9b4fec-1f6e-458a-ab35-50e37a8371f8

### Withdraw
https://github.com/Nikzz23/PlatinumPay/assets/114866835/508b2c24-4c7a-4c48-ac8d-5e99604f5c42

### History
https://github.com/Nikzz23/PlatinumPay/assets/114866835/80747107-07d8-421f-8aaf-e0cb063f7d3a

### Account Settings
https://github.com/Nikzz23/PlatinumPay/assets/114866835/d0297cf6-bea0-40e8-9678-e93b5701dbf8

### Account Settings / Edit Personal Information
https://github.com/Nikzz23/PlatinumPay/assets/114866835/4b8f8710-3361-43c6-8596-d83208b8f431

### Account Settings / Delete Account
https://github.com/Nikzz23/PlatinumPay/assets/114866835/72ce5494-4bcf-4073-a5ff-45d0448990d3

### Log Out
https://github.com/Nikzz23/PlatinumPay/assets/114866835/53a50124-5187-4226-89fd-3494c46baae1

## System Photos

### Sign In and User Dashboard
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/3d00f949-5561-4749-9b60-0ccd2d3b5c6b)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/9d3b616d-6198-47d8-8d62-04a466794ad2)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/5dd4a0d6-aec2-49ac-8d39-2f81db3dcaf9)


### Sign Up and User Dashboard
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/f6034ec1-130e-4643-be7d-7f1bf10170f3)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/9cff5d4b-e472-42ca-b091-f7ba5ebe3f79)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/e22ac888-3770-4b66-a7bd-bacb85d887bb)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/9572e7e1-90a4-46c7-8122-c914a8a3e82d)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/75380013-73af-44a6-807c-66ed2add5808)


### Deposit
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/8f924ed6-57de-49dc-9a68-64ff4dfaac29)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/0228cf80-c749-4dfc-8055-d5b707c1635c)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/35c43337-6fd2-4942-8156-07d8e8e400b4)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/063cf475-0e3c-48ac-97b4-e141c8ba711e)


### Transfer
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/7dc7cee4-1185-474d-b616-5a293931b9f6)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/0b1e030b-e770-4a64-8105-53ca29fd15c4)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/f5760cdf-2f55-4b0a-bf0e-196aad62a184)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/8d0cfa3e-39cf-4081-9bc1-69f5dbd8f873)


### Withdraw
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/6b472e54-d235-4acf-b37f-97bc0c58f01a)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/b9048139-6e0c-4fec-9586-3035c2a569de)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/4e8c42a3-a46f-4930-8186-e1e11d714d68)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/829adbd5-aa20-4a66-bc96-a7383043bab8)


### History
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/97763f3f-25df-4ae3-80f4-1135b9d33e5d)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/0505f779-5284-47fa-a782-1a0ae8d7871a)


### Account Settings
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/97763f3f-25df-4ae3-80f4-1135b9d33e5d)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/40fb016e-aeb8-4ec7-8446-ecd9fc988371)


### Account Settings / Edit Personal Information
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/bb642670-4cf6-4788-94ab-84939cb07b57)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/e63e03e0-9260-468f-a77c-cfdd6009e296)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/1827cdac-ee5e-4a97-aab9-cd4151d2759e)


### Account Settings / Delete Account
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/bb642670-4cf6-4788-94ab-84939cb07b57)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/64db6bcd-9fa8-45be-bc6b-a3d6388aa1cf)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/101fb10b-2ff2-432a-8eb0-cde1398b4201)


### Log Out
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/a8bf27f1-f146-4dcb-91e1-48056b5881dd)
![image](https://github.com/Nikzz23/PlatinumPay/assets/114866835/2f12b79c-b438-475f-af9a-63cad8880a6a)



