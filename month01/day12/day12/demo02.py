"""
    继承
        财产：钱  不用孩子挣,但是可以花.
        皇位：江山不用太子打,但是可以坐.
        代码：子类不用写,但是可以用.
"""


# 封装有了多个类
# 多个类有相同代码,且都属于一个概念.
class Person:
    def say(self):
        print("说话")


class Student(Person):
    def study(self):
        print("学习")

        # def say(self):
    #     print("说话")


class Teacher:
    def teach(self):
        print("教学")

    # def say(self):
    #     print("说话")


# 测试
p1 = Person()
# 父类对象只能访问父类成员
p1.say()

s1 = Student()
# 子类对象可以访问父类成员，也可以访问子类成员
s1.study()
s1.say()

# 内置函数
# 人对象是一种人类型
print(isinstance(p1, Person))  # True
# 学生对象是一种人类型
print(isinstance(s1, Person))  # True
# 人对象是一种学生类型
print(isinstance(p1, Student))  # False
# 学生对象是一种老师类型
print(isinstance(s1, Teacher))  # False

# 人类型是一种人类型
print(issubclass(Person, Person))  # True
# 学生类型是一种人类型
print(issubclass(Student, Person))  # True
# 人类型是一种学生类型
print(issubclass(Person, Student))  # False
# 学生类型是一种老师类型
print(issubclass(Student, Teacher))  # False

# 人对象是人类型
print(type(p1) == Person)  # True
# 学生对象是人类型(学生对象是学生类型,不是人类型)
print(type(s1) == Person)  # False
# 人对象是学生类型
print(type(p1) == Student)  # False
# 学生对象是老师类型
print(type(s1) == Teacher)  # False
