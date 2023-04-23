def total(initial=5, *numbers, extra_number):
	count = initial
	for number in numbers:
		count += number
	count += extra_number
	print(count)

total(10, 1, 2, 3, extra_number = 50)
total(10, 1, 2, 3)

#Вызовет ошибку, поскольку мы не указали значение 
#аргумента по умолчанию для 'extra_number'

input("\n\nНажмите Enter, чтобы выйти.")







#Если некоторые ключевые параметры должны быть доступны только по ключу, а не как позиционные аргументы, их можно объявить
#после параметра со звёздочкой 