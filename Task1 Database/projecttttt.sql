show databases;
create database Task;
use Task;

create table Department(DeptID int primary key Not null, DeptName varchar(50) Not null, DeptCode varchar(50), 
ManagerID int, ManagerName varchar(50), Descriptionn text, Activee boolean);

desc Department;

insert into Department value(101, 'Sales', 'S01', 1, 'John', 'Deals with sales and other stuffs', true );
insert into Department value(102, 'Marketing', 'M01', 1, 'Ned', 'Deals with marketing and other stuffs', false );
insert into Department value(103, 'It', 'I01', 1, 'Sansa', 'They are cool guys', true );
insert into Department value(104, 'Account', 'A01', 1, 'Bran', 'Deals with accounts and other stuffs', true );
insert into Department value(105, 'Reception', 'R01', 1, 'Arya', 'Dealing with client and customers', true );

select * from Department;

create table Employee(employeeID int primary key not null, FirstName varchar(50) not null,
 MiddleName varchar(50) not null, LastName varchar(50) not null, joinDate datetime, MonthlySalary decimal(6,2),
 DeptID int not null, foreign key (DeptID) references Department(DeptID));
 
alter table Employee modify MiddleName varchar(50);
alter table Employee modify MonthlySalary decimal(7,2);


 
 desc Employee;
 
insert into Employee values(501, 'Ram', 'Bahadur', 'Karki', '2019-02-15 10:30:00', 30000.00, 101);
insert into Employee values(502, 'Hari', 'Bahadur', 'Khadka', '2022-04-15 10:30:00', 25000.00, 101);
insert into Employee values(503, 'Shyam', '', 'Chhetri', '2020-04-15 10:30:00', 27000.00, 101);
insert into Employee values(517, 'Suraj', 'Raj', 'Pandey', '2022-03-15 9:30:00', 27000.00, 101);
insert into Employee values(504, 'Rajesh', 'Null', 'Hamal', '2019-04-15 10:30:00', 3200.00, 101);

insert into Employee values(505, 'Harka', 'Raj', 'Shrestha', '2022-04-15 10:30:00', 28000.00, 102);
insert into Employee values(506, 'Rabin', 'Null', 'Rai', '2020-04-15 10:30:00', 29000.00, 102);
insert into Employee values(507, 'Lakpa', 'Null', 'Sherpa', '2020-09-15 10:30:00', 25000.00, 102);


insert into Employee values(508, 'Rohit', 'Null', 'Lama', '2021-12-24 9:30:00', 25000.00, 103);
insert into Employee values(509, 'Sonam', 'Wangdi', 'Sherpa', '2022-01-11 12:30:00', 25000.00, 103);
insert into Employee values(510, 'Tsering', 'Wangdi', 'Sherpa', '2021-04-15 12:42:00', 35000.00, 103);

insert into Employee values(511, 'Saroj', 'Null', 'Neupane', '2022-04-15 10:50:00', 30000.00, 104);
insert into Employee values(512, 'Nirav', 'Null', 'Timalsena', '2020-08-24 11:42:00', 29000.00, 104);
insert into Employee values(513, 'Sagun', 'Null', 'Joshi', '2020-09-15 2:15:00', 25000.00, 104);

insert into Employee values(514, 'Supriya', 'Null', 'Shakya', '2022-04-15 12:50:00', 30000.00, 105);
insert into Employee values(515, 'Swastika', 'Null', 'Shrestha', '2020-08-24 11:42:00', 29000.00, 105);


select * from Employee;

create table Employee(employeeID int primary key not null, FirstName varchar(50) not null,
 MiddleName varchar(50) not null, LastName varchar(50) not null, joinDate datetime, MonthlySalary decimal(6,2),
 DeptID int not null, foreign key (DeptID) references Department(DeptID));
 
 /* --------------------------------------First Question-------------------------------------------- */

SELECT 
    dept.DeptName,    
	sum(TIMESTAMPDIFF(Month, joinDate, current_timestamp()) * MonthlySalary) AS TotalEarnings
FROM
    Employee emp, Department dept where emp.DeptID = dept.DeptID group by dept.DeptName;
    
    
 /* --------------------------------------Second Question-------------------------------------------- */
    
SELECT 
    emp.FirstName
FROM
    Employee emp, Department dept where emp.DeptID = dept.DeptID and dept.DeptName='Sales' and 
    TIMESTAMPDIFF(Month, joinDate, current_timestamp()) > 6 ;
    
    
 /* --------------------------------------Third Questions-------------------------------------------- */
 
 SELECT 
    emp.FirstName,
    emp.LastName,
    dept.DeptName,
    dept.ManagerName
FROM
    Employee emp, Department dept where emp.DeptID = dept.DeptID;












