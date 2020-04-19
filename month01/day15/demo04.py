class Wife:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 16 < value <= 30:
            self.__age = value
        else:
            # raise 抛出
            raise Exception("我不要")

# try 接收
try:
    w01 = Wife(20)
    print(w01.age)
except:
    print("那你再等等吧")
