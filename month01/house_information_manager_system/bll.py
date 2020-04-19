"""
    业务逻辑层
"""
import collections
from typing import List, Dict

from dal import HouseDao
from model import HouseModel


class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()

    @property
    def list_houses(self) -> List[HouseModel]:
        return self.__list_houses

    def get_house_by_max_total_price(self) -> HouseModel:
        return max(self.__list_houses, key=lambda house: house.total_price)

    def get_house_by_min_area(self) -> HouseModel:
        return min(self.__list_houses, key=lambda house: house.area)

    def get_houses_type(self) -> Dict[str, int]:
        """
            获取户型种类
        :return:字典类型[户型种类,数量]
        """
        # dict_house_type = {}
        # for house in self.__list_houses:
        #     if house.house_type in dict_house_type:
        #         dict_house_type[house.house_type] += 1
        #     else:
        #         dict_house_type[house.house_type] = 1
        # return dict_house_type
        # return collections.Counter([house.house_type for house in self.__list_houses])
        return collections.Counter(map(lambda house: house.house_type, self.__list_houses))

    def ascending_by_id(self):
        return sorted(self.__list_houses, key=lambda house: house.id)

    def descending_by_unit_price(self):
        return sorted(self.__list_houses, key=lambda house: house.unit_price, reverse=True)

    def descending_by_attention(self):
        return sorted(self.__list_houses, key=self.__calculate_attention, reverse=True)

    def __calculate_attention(self, house: HouseModel):
        # 120人关注 / 共42次带看 / 一年前发布
        attention_info = house.follow_info.split("/")[0]
        # 120人关注　--> 120
        return float(attention_info.replace("人关注", ""))
