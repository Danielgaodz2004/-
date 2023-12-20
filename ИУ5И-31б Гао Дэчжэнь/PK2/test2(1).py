"""
coding: utf-8
@Software: PyCharm
@Time:  18:35
@Author: Fake77
@Module Name:
"""
import unittest

from datatest2 import a1, a2, a3


class TestDataClass(unittest.TestCase):
    a1 = [('tuzi', 90000, 'отдел economic'), ('lzc', 1800, 'отдел electric'), ('FJH', 300, 'отдел market'),
          ('gdz', 3000, 'отдел shop')]
    a2 = [('отдел economic', 90000), ('отдел shop', 3000), ('отдел electric', 1800), ('отдел market', 300)]
    a3 = {'отдел shop': ['tuzi'], 'отдел market': ['gdz'], 'отдел economic': ['lzc'], 'отдел electric': ['FJH']}

    def test_a1(self):
        print('run test a1')
        a1_lst = a1()
        self.assertListEqual(a1_lst, self.a1)

    def test_a2(self):
        print('run test a2')
        a2_lst = a2()
        self.assertListEqual(a2_lst, self.a2)

    def test_a3(self):
        print('run test a3')
        a3_lst = a3()
        self.assertDictEqual(a3_lst, self.a3)


if __name__ == '__main__':
    unittest.main()