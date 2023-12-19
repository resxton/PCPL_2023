import random


def gen_random(num_count, begin, end):
	for _ in range(num_count):
		yield random.randint(begin, end)


def main():
	random_numbers = gen_random(5, 1, 10)

	for number in random_numbers:
		print(number)


if __name__ == "__main__":
	main()
