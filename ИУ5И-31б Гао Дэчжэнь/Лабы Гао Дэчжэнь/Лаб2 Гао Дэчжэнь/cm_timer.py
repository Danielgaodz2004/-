"""
coding: utf-8
@Software: PyCharm
@Time:  1:49
@Author: Fake77
@Module Name:
"""
import time
from contextlib import contextmanager


class cm_time_1(object):

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print('time for run program: ', self.end - self.start)


def cm_time2(func):
    @contextmanager
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("time for run program: ", end - start)
        yield result
    return inner


def add(a, b):
    time.sleep(2)
    return a + b


@contextmanager
def cm_time_2():
    start = time.time()
    yield
    end = time.time()
    print("总耗时: ", end - start)
