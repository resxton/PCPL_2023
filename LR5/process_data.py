import json
from cm_timer import cm_timer_1
from print_result import print_result
from gen_random import gen_random

path = "data_light.json"

with open(path) as f:
	data = json.load(f)


@print_result
def f1(arg):
	return sorted(set(job['job-name'].lower() for job in arg))


@print_result
def f2(arg):
	return list(filter(lambda x: x.lower().startswith("программист"), arg))


@print_result
def f3(arg):
	return list(map(lambda x: f"{x}, с опытом Python", arg))


@print_result
def f4(arg):
	return [f"{job}, зарплата {salary} руб." for job, salary in zip(arg, gen_random(len(arg), 100000, 200000))]


if __name__ == '__main__':
	with cm_timer_1():
		f4(f3(f2(f1(data))))
