"""
coding: utf-8
@Software: PyCharm
@Time:  17:40
@Author: Fake77
@Module Name:
"""
from operator import itemgetter


class Emp:
    def __init__(self, emp_id, fio, sal, dep_id):
        self.emp_id = emp_id
        self.fio = fio
        self.sal = sal
        self.dep_id = dep_id


class Dep:
    def __init__(self, dep_id, name):
        self.dep_id = dep_id
        self.name = name


class DepEmp:
    def __init__(self, dep_id, emp_id):
        self.dep_id = dep_id
        self.emp_id = emp_id


deps = [
    Dep(1, 'отдел shop'),
    Dep(2, 'отдел market'),
    Dep(3, 'отдел economic'),
    Dep(4, 'отдел electric'),
]

emps = [
    Emp(1, 'tuzi', 90000, 3),
    Emp(2, 'gdz', 3000, 1),
    Emp(3, 'lzc', 1800, 4),
    Emp(4, 'FJH', 300, 2),
]

emps_deps = [
    DepEmp(1, 3),
    DepEmp(2, 1),
    DepEmp(3, 4),
    DepEmp(4, 2),
]

one_to_many = [
    (e.fio, e.sal, d.name)
    for d in deps
    for e in emps
    if e.dep_id == d.dep_id
]


def main():
    many_to_many_temp = [(d.name, ed.dep_id, ed.emp_id)
                         for d in deps
                         for ed in emps_deps
                         if d.dep_id == ed.dep_id]

    many_to_many = [(e.fio, e.sal, dep_name)
                    for dep_name, dep_id, emp_id in many_to_many_temp
                    for e in emps if e.dep_id == emp_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []

    for d in deps:
        # Список сотрудников отдела
        d_emps = list(filter(lambda i: i[2] == d.name, one_to_many))
        # Если отдел не пустой
        if len(d_emps) > 0:
            # Зарплаты сотрудников отдела
            d_sals = [sal for _, sal, _ in d_emps]
            # Суммарная зарплата сотрудников отдела
            d_sals_sum = sum(d_sals)
            res_12_unsorted.append((d.name, d_sals_sum))

    # Сортировка по суммарной зарплате
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    for d in deps:
        if 'отдел' in d.name:

            d_emps = list(filter(lambda i: i[2] == d.name, many_to_many))

            d_emps_names = [x for x, _, _ in d_emps]

            res_13[d.name] = d_emps_names

    print(res_13)


if __name__ == '__main__':
    main()
