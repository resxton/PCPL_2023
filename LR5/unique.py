class Unique(object):
	def __init__(self, items, **kwargs):
		self.data = iter(items)
		self.unique_set = set()
		self.ignore_case = kwargs.get('ignore_case', False)

	def __next__(self):
		while True:
			item = next(self.data)
			key = item.lower() if self.ignore_case and isinstance(item, str) else item

			if key not in self.unique_set:
				self.unique_set.add(key)
				return item

	def __iter__(self):
		return self


def main():
	data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
	unique_iterator1 = Unique(data1)
	print(list(unique_iterator1))  # Вывод: [1, 2]

	from gen_random import gen_random

	data2 = gen_random(10, 1, 3)
	unique_iterator2 = Unique(data2)
	print(list(unique_iterator2))  # Вывод: комбинация из [0;1] цифр 1, 2, 3

	data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
	unique_iterator3 = Unique(data3)
	print(list(unique_iterator3))  # Вывод: ['a', 'A', 'b', 'B']

	unique_iterator4 = Unique(data3, ignore_case=True)
	print(list(unique_iterator4))  # Вывод: ['a', 'b']


if __name__ == "__main__":
	main()
