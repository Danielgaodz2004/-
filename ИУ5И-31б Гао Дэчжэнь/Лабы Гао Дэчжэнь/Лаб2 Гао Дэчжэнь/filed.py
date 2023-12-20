"""
coding: utf-8
@Software: PyCharm
@Time:  22:33
@Author: Fake77
@Module Name:
"""


def field(contain: list, *args):
    assert len(args) > 0
    for element in contain:
        result = dict()
        for arg in args:
            if arg in element.keys():
                result[arg] = element[arg]
            else:
                continue
        if result:
            yield result
        continue


def field2(contain: list, *args):
    assert len(args) > 0
    for element in contain:
        result = dict()
        for arg in args:
            try:
                if element[arg]:
                    result[arg] = element[arg]
            except KeyError:
                continue

        if result:
            yield result
        continue


# goods = [
#     {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#     {'title': 'Диван для отдыха', 'color': 'black'},
#     {},
#     {'title': 'Диван для отдыха', 'color': 'black'},
# ]
#
# for i in field(goods, 'title', 'price'):
#     print(i)
#
# # for i in field2(goods, 'title', 'price', 'color'):
# #     print(i)
