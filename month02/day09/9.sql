create table class(cid int primary key auto_increment,
                  caption char(4) not null);

create table teacher(tid int primary key auto_increment,
                    tname varchar(32) not null);

create table student(sid int primary key auto_increment,
                    sname varchar(32) not null,
                    gender enum('male','female','others') not null default 'male',
                    class_id int,
                    foreign key(class_id) references class(cid)
                    on update cascade
                    on delete cascade);

create table course(cid int primary key auto_increment,
                   cname varchar(16) not null,
                   teacher_id int,
                   foreign key(teacher_id) references teacher(tid)
                   on update cascade
                   on delete cascade);

create table score(sid int primary key auto_increment,
                  student_id int,
                  course_id int,
                  number int(3) not null,
                  foreign key(student_id) references student(sid)
                   on update cascade
                   on delete cascade,
                   foreign key(course_id) references course(cid)
                   on update cascade
                   on delete cascade);

insert into class(caption) values('三年二班'),('三年三班'),('三年一班');
insert into teacher(tname) values('波多老师'),('苍老师'),('小泽老师');
insert into student(sname,gender,class_id) values('钢蛋','female',1),('铁锤','female',1),('山炮','male',2),('彪哥','male',3);
insert into course(cname,teacher_id) values('生物',1),('体育',1),('物理',2);
insert into score(student_id,course_id,number) values(1,1,60),(1,2,59),(2,2,100),(3,2,78),(4,3,66);

1. 查询每位老师教授的课程数量
select t.tname,count(c.cname)
from teacher as t left join course as c on t.tid=c.teacher_id
group by t.tname;

2. 查询学生的信息及学生所在班级信息
select sid,sname,gender,caption
from student left join class on student.class_id=class.cid;

3. 查询各科成绩最高和最低的分数,形式 : 课程ID  最高分  最低分
select course.cid,max(number),min(number) from course left join score on course.cid=score.course_id
group by course.cid;

4. 查询平均成绩大于85分的所有学生学号,姓名和平均成绩
select student.sid,student.sname,avg(number)
from student left join score on student.sid=score.student_id
group by student.sid having avg(number)>85;

5. 查询课程编号为2且课程成绩在80以上的学生学号和姓名
select student.sid,student.sname
from student left join score on score.student_id=student.sid
where score.course_id=2 and number>80;

6. 查询各个课程及相应的选修人数
select course.cname,count(score.student_id)
from course left join score on course.cid=score.course_id
group by course.cname;

作业: 1. 将book数据表拆分  图书表   作家表   出版社表
         字段自拟  关系自拟
create table 作家 (id int primary key auto_increment,name varchar(30),sex char,remark text);
create table 出版社 (id int primary key auto_increment,pname varchar(30),address varchar(128),tel char(16));
create table 图书 (id int primary key auto_increment,bname varchar(30),
price float,
press_date date,
aid int,pid int,
constraint afk foreign key (aid) references 作家(id),
constraint pfk foreign key (pid) references 出版社(id));
create table author_press(
id int primary key auto_increment,
a_id int,
p_id int,
签约时间 date,
constraint a_fk foreign key (a_id) references 作家(id),
constraint p_fk foreign key (p_id) references 出版社(id));
)
         画出E-R图然后建立表模型

      2. 函数 传入两个学生的ID 得到这两个学生的成绩之和
delimiter $$
create function  get_sum(uid1 int,uid2 int)
returns float
begin
declare a float;
declare b float;
select score from cls where id=uid1 into a;
select score from cls where id=uid2 into b;
return a+b;
end $$

delimiter ;

存储过程  传入一个学生的姓名 通过外部的用户变量得到这个学生的成绩
delimiter $$
create procedure get_score(in uname varchar(30),out s float)
begin
set s=(select score from cls where name=uname);
end $$

delimiter ;

set @s=0;

call get_score('Lily',@s)


