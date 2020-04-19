"""
    创建敌人类（姓名、血量、攻击力）
                  0-100  1 - 30
    创建敌人对象,设置不同数据,体会拦截作用.
"""


class Enemy:
    def __init__(self, name="", hp=0, atk=0):
        self.name = name
        self.hp = hp
        self.atk = atk

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            raise Exception("血量超过范围")

    hp = property(get_hp, set_hp)

    def get_atk(self):
        return self.__atk

    def set_atk(self, value):
        if 1 <= value <= 30:
            self.__atk = value
        else:
            raise Exception("攻击力超过范围")

    atk = property(get_atk, set_atk)


e01 = Enemy("灭霸", 50, 10)
print(e01.hp)
print(e01.atk)
