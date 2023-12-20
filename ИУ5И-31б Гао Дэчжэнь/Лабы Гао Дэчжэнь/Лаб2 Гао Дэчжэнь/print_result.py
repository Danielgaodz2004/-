"""
coding: utf-8
@Software: PyCharm
@Time:  1:30
@Author: Fake77
@Module Name:
"""

# import functools


# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#
#         return wrapper
#
#     return decorator


# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % wrapper.__name__)
#         return func(*args, **kw)
#     return wrapper

def print_result(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result

    return inner


# @log("excute")
# def add(a, b):
#     return a + b
#
#
# add(1, 2)
