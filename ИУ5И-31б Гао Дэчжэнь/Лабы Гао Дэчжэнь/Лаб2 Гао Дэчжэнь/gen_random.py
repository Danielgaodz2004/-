"""
coding: utf-8
@Software: PyCharm
@Time:  22:47
@Author: Fake77
@Module Name:
"""
import random


def gen_random(num_count: int, begin: int, end: int):
    for _ in range(num_count):
        yield random.randint(begin, end)


# [print(i) for i in gen_random(5, 0, 100)]
