summ = 0
numb = 0
rating = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '5a', 'scores': [5,5,3,2,2]}, {'school_class': '6a', 'scores': [5,4,4,5,2]}]
for a in rating:
#	print(a)
	for b in a.get('scores'):
		print (b)
		summ += b
		numb += 1

middle = summ / numb
print (middle)

