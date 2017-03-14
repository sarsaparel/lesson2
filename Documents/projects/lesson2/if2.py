str1 = input('Твое первое слово - ')
str2 = input('Твое второе слово - ')

if str1 == str2:
	print('1')
elif len(str1) > len(str2) and str2 != 'learn':
	print ('2')
elif len(str1) != len(str2) and str2 == 'learn':
	print('3')
