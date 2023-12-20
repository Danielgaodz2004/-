"""
coding: utf-8
@Software: PyCharm
@Time:  22:50
@Author: Fake77
@Module Name:
"""
import collections.abc
import random


class Unique(object):
    def __init__(self, items, **kwargs):
        if 'ignore_case' in kwargs.keys():
            ignore_case = kwargs['ignore_case']
        else:
            ignore_case = False
        self.itr = isinstance(items, collections.abc.Iterable)

        if ignore_case:
            self.items = list(set([str(ele).lower() for ele in items]))
        else:
            self.items = list(set(items))

    def __next__(self):
        if self.idx == len(self.items):
            raise StopIteration
        idx = self.idx
        self.idx += 1
        return self.items[idx]

    def __iter__(self):
        self.idx = 0
        return self


data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
data2 = [1, 2, 3, 4, 5, 5, 5, 5, 2, 3, 1]


# def gen_random(num_count: int, begin: int, end: int):
#     for _ in range(num_count):
#         yield random.randint(begin, end)
#
#
# for i in Unique(gen_random(5, 0, 100), ignore_case=True):
#     print(i, end=' ')
#
# for i in Unique(data2, ignore_case=True):
#     print(i, end=' ')
