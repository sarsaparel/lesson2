# При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

a = 'зачем задавать сначала эту переменную?'

def ask_user(a):
	while True:
		a = input('Как дела? ')
		if a == 'Хорошо':
			break
		elif a == 'Пока!':
			break
		elif a[-1] == '?':
			get_answer(a)
			


def get_answer(a):
	print ('Ответ на этот вопрос лежит в твоем подсознании, загляни туда')

ask_user(a)
