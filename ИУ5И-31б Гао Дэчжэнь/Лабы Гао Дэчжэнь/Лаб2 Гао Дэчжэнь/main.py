import json
from print_result import print_result
from unique import Unique
from cm_timer import cm_time_1
from filed import field
import random

path = 'data/data_ligth.json'

with open(path, encoding='utf-8') as f:
    data = json.load(f)
# print(data)


@print_result
def f1(arg):
    job_lst = [job['job-name'] for job in field(arg, 'job-name')]
    job_lst_sorted = sorted([job for job in Unique(job_lst)])
    return job_lst_sorted


@print_result
def f2(arg: list):
    return list(filter(lambda x: x.startswith('программист'), arg)) + list(filter(lambda x: x.startswith('Программист'), arg))


@print_result
def f3(arg):
    return [job + 'с опытом Python' for job in arg]


@print_result
def f4(arg):
    return [job + f'зарплата {random.randint(100000, 200000)} руб.' for job in arg]


if __name__ == '__main__':
    with cm_time_1():
        f4(f3(f2(f1(data))))
