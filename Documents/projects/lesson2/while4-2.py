
a = 'зачем задавать сначала эту переменную?'

def ask_user(a):
	while True:
		a = input('Как дела? ')
		answer = get_answer(a, dic)
		if answer != None:
			print (answer)
		if a == 'Хорошо':
			break
		elif a == 'Пока!':
			break
		

dic = {'Печаль' : 'это место, куда приходят корабли', 'Ураган' : 'это то, что мы кладем себе в чай', 'Курага' : 'отрывает машины от земли'}

def get_answer(a, dic):
	return dic.get(a)

if __name__ == "__main__"
ask_user(a)
