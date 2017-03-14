name = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person(name):
	while True:
		a = name.pop()
		print(a)
		if a == "Валера":
			print('Валера нашелся')
			break
			
find_person(name)
#почему если print(find_person(name)) выдает в конце None?

# в обратном порядке?