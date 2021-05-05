# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/18 14:38
@Auth ： chenxu
@File ：Cat.py
"""
from Animal import Animal


class Cat(Animal):

    def __init__(self,hair,name,color,age,sex):
        super().__init__(name,color,age,sex)
        self.hair = hair
        print("子类初始化")

    def action(self):
        print(f"{self.name}会抓老鼠")

    def wow(self):
        print(f"{self.name}会叫，喵喵叫")

if __name__ == '__main__':
    a_cat = Cat("short","huahua","gray","3","girl")
    print(a_cat.age)
    print(a_cat.hair)
    a_cat.wow()
    a_cat.action()

