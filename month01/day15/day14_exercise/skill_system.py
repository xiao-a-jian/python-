"""
    技能系统
        三大特征：
            封装(分)：创建了技能释放器SkillDeployer和具体影响效果(DamageEffect、DizzinessEffect、LowerDeffenseEffect)
            继承(隔)：创建了技能影响效果SkillImpactEffect,抽象(统一)具体影响效果
            多态(做)：技能释放器SkillDeployer调用技能影响效果SkillImpactEffect,具体影响效果进行重写,
                 根据配置文件,动态(运行时)创建具体影响效果对象.
        设计原则：
            开闭原则：当增加新影响效果算法,技能释放器SkillDeployer不变
            单一职责：
                DamageEffect：负责处理伤害生命算法
                DizzinessEffect：负责眩晕算法
                SkillDeployer：负责技能释放(创建和执行影响效果对象)
            依赖倒置(用谁?)：技能释放器SkillDeployer调用技能影响效果SkillImpactEffect,没有调用具体影响效果.
            组合复用(用法?)：技能释放器SkillDeployer与影响效果算法是组合关系
            里氏替换：重写时通过super()调用了父类方法
            迪米特：技能释放器SkillDeployer与各种影响效果低耦合。
        优势：
            增加新技能,代码无需改变.  -->  体现正确分析了需求中行为的变化
            某个技能所需要的影响算法改变,代码无需改变. --> 体现了依赖注入(修改配置文件)
            某个影响算法改变,不影响其他代码 --> 体现迪米特
            增加影响算法,增加新类型,不影响其他代码 --> 体现开闭原则
"""

print(__name__)

# Python类型标注
class SkillImpactEffect:
    def impact(self) -> None:
        pass


class DamageEffect(SkillImpactEffect):
    def __init__(self, value=0):
        self.value = value

    # 2. 重写
    def impact(self):
        super().impact()
        print("扣你", self.value, "血量")

class DizzinessEffect(SkillImpactEffect):
    def __init__(self, duration=0):
        self.duration = duration

    def impact(self):
        super().impact()
        print("眩晕你", self.duration, "秒")


class LowerDeffenseEffect(SkillImpactEffect):
    def __init__(self, value=0, duration=0):
        self.value = value
        self.duration = duration

    def impact(self):
        super().impact()
        print("降低", self.duration, "防御力,持续", self.duration, "秒")


class SkillDeployer:
    def __init__(self, name=""):
        self.name = name
        self.__config_file = {
            "降龙十八掌": ["DizzinessEffect(15)", "DamageEffect(500)"],
            "六脉神剑": ["LowerDeffenseEffect(100,10)", "DamageEffect(500)"],
        }
        effect_names = self.__config_file[self.name]
        # "DizzinessEffect(15)"  --> DizzinessEffect(15)
        # self.__effect_objects = []
        # for item in effect_names:
        #     self.__effect_objects.append(eval(item))
        self.__effect_objects = [eval(item) for item in effect_names]

    def deploy(self):
        print(self.name, "打死你")
        for item in self.__effect_objects:
            # 1. 调用父类(影响效果SkillImpactEffect)
            item.impact()

# 测试
xlsbz = SkillDeployer("降龙十八掌")
xlsbz.deploy()

lmsj = SkillDeployer("六脉神剑")
lmsj.deploy()
