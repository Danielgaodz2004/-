"""
coding: utf-8
@Software: PyCharm
@Time:  23:06
@Author: Fake77
@Module Name:
"""
data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]


if "__main__" == __name__:
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)

    result = sorted(data, key=abs, reverse=True)
    print(result)

