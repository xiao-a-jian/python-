CREATE TABLE `person` (
       `id` int PRIMARY KEY AUTO_INCREMENT,
       `name` varchar(32) NOT NULL,
       `age` tinyint DEFAULT 0,
       `sex` enum('m','w','o') DEFAULT 'o',
       `salary` decimal(8,2) DEFAULT 250.00,
       `hire_date` date NOT NULL,
       `dept_id` int) ;

insert into dept values(1,"技术部"),(2,"财务部"),(3,"销售部"),(4,"行政部"),(5,"市场部");
insert into person values(1,"Lily",29,'w',20000,'2017-4-3',2),(2,"Tom",27,'m',16000,'2019-10-3',1),(3,"Joy",30,'m',28000,'2016-4-3',1),(4,"Emma",24,'w',8000,'2019-5-8',4),(5,"Abby",28,'w',17000,'2018-11-3',3),(6,"Jame",32,'m',22000,'2017-4-7',3);


alter table person add constraint dept_fk foreign key(dept_id) references dept(id) on delete cascade on update cascade;

create view person_dept as (select p.id,p.name,p.age,p.sex,p.salary,d.dname from person as p left join dept as d on p.dept_id = d.id);












