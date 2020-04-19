-- 朋友圈设计练习

-- 用户
create table user(
id int primary key auto_increment,
name varchar(30),
passwd char(64)
);

-- 朋友圈内容
create table pyq(
id int primary key auto_increment,
content text,
image blob,
time datetime,
u_id int,
constraint u_fk foreign key (u_id) references user(id)
);

-- 点赞评论
create table user_pyq(
id int primary  key auto_increment,
uid int,
pid int,
lk bit default 0,
comment text,
constraint ufk foreign key (uid) references user(id),
constraint pfk foreign key (pid) references pyq(id)
);


-- 练习: 对应笔记中ER模型图,建立教师,学生,课程三个实体之间的表关系

create table teacher(
id int primary key  auto_increment,
姓名 varchar(30),
职称 varchar(50),
年龄 tinyint
);

create table stu(
id int primary key  auto_increment,
姓名 varchar(30),
年龄 tinyint,
性别 char,
籍贯 varchar(128)
);

create table course(
id int primary key  auto_increment,
名称 varchar(30),
学分 float,
tid int,
constraint t_fk
foreign key (tid)
references teacher(id)
);

create table course_stu(
cid int,
sid int,
score float,
constraint c_fk
foreign key (cid)
references course(id),
constraint s_fk
foreign key (sid)
references stu(id)
);


-- 多表查询
查询技术部工资高于20000的
select * from
(select d.dname,p.name,p.salary
from dept as d,person as p
where d.id = p.dept_id) as a
where dname='技术部' and salary > 20000;

select dept.dname,person.name,person.salary
from dept inner join person on dept.id=person.dept_id
where dname='技术部' and salary > 20000;

-- 部门ID大于1的所有部门及人员
select dept.dname,person.name
from dept left join person on dept.id = person.dept_id
where dept.id > 1;

-- 工资高于20000的人员和部门
select person.name,dept.dname
from dept right join person on dept.id = person.dept_id
where person.salary>=20000;




