name = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
while True:
	a = name.pop()
	print(a)
	if a == "Валера":
		print('Валера нашелся')
		break