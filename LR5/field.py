def field(items, *args):
	assert len(args) > 0

	if len(args) == 1:
		# Если передано только одно поле, выдаем значения этого поля последовательно
		for item in items:
			field_value = item.get(args[0])
			if field_value is not None:
				yield field_value
	else:
		# Если передано несколько полей, выдаем словари, содержащие эти поля
		for item in items:
			# comprehesion
			filtered_item = {field: item.get(field) for field in args if item.get(field) is not None}
			if filtered_item:
				yield filtered_item


def main():
	goods = [
		{'title': 'Ковер', 'price': 2000, 'color': 'green'},
		{'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
		{'title': 'Стол', 'price': 500, 'color': 'brown'},
		{'title': 'Лампа', 'price': 120, 'color': 'white'},
		{'title': 'Шкаф', 'color': 'red'},
		{'title': 'Кресло', 'price': 2500, 'color': 'blue'}
	]

	for value in field(goods, 'title'):
		print(value)

	for dictionary in field(goods, 'title', 'price'):
		print(dictionary)


if __name__ == '__main__':
	main()
