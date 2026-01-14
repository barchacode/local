create table emp (
emp_id serial primary key,
first_name varchar(30) not null,
last_name varchar(30),
email varchar(40)not null unique,
dept varchar(40),
salary decimal(10,2) default 30000.00,
hire_date date not null default current_date

)
select * from emp;
INSERT INTO emp (first_name, last_name, email, dept)
VALUES ('nasir', 'abbas', 'barcha@gmail.com', 'IT');

INSERT INTO emp (first_name, last_name, email, dept)
VALUES ('asif', 'raza', 'asif@gmail.com', 'IT');

INSERT INTO emp (first_name, last_name, email, dept)
VALUES ('raza', 'ali', '@gmail.com', 'IT'),
('salah', 'din', 'salah@gmail.com', 'isa');

select count(*) from emp;

SELECT salary, COUNT(*) FROM emp GROUP BY salary;
 update emp set salary=50000 where emp_id=1;