create table teacher(
id int primary key auto_increment,
姓名 varchar(30),
年龄 tinyint,
性别 char,
籍贯 varchar(128)
);

create table stu(
id int primary key auto_increment,
)






create table course(
id int primary key auto_increment,
名称 varchar(30),
)



create table course_stu(
cid int,
sid int,
score float,
)