# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/18 14:38
@Auth ： chenxu
@File ：Animal.py
"""
class Animal:

    def __init__(self,name,color,age,sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
        print("初始化")

    def wow(self):
        print(f"{self.name}会叫，嗷呜")

    def run(self):
        print("我会跑")


if __name__ == '__main__':
    a_Animal = Animal("dahuang","yellow","5","female")
    print(a_Animal.age)
    a_Animal.wow()