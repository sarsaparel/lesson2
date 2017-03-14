
a = 'зачем задавать сначала эту переменную?'

def ask_user(a):
	while True:
		a = input('Как дела? ')
		if a == 'Хорошо':
			break

ask_user(a)


