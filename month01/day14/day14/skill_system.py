"""
    技能系统
"""


class SkillImpactEffect:
    def impact(self):
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
