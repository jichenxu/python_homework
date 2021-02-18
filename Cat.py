# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/18 14:38
@Auth ： chenxu
@File ：Cat.py
"""
from Animal import Animal


class Cat(Animal):

    hair = "short hair"

    def __init__(self):
        super().__init__()
        print("我是一只猫")

    def action(self):
        print("我会抓老鼠")

    def wow(self):
        print("我会叫，喵喵叫")

if __name__ == '__main__':
    a_cat = Cat()
    print(a_cat.age)
    print(a_cat.wow())
    print(a_cat.action())

