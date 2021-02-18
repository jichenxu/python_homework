# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/18 14:38
@Auth ： chenxu
@File ：Animal.py
"""
class Animal:
    name = "huahua"
    color = "yellow"
    age = "3"
    sex = "female"

    def __init__(self):
        print("初始化")

    def wow(self):
        print("我会叫，嗷呜")

    def run(self):
        print("我会跑")


if __name__ == '__main__':
    a_Animal = Animal()
    print(a_Animal.age)
    print(a_Animal.wow())
