def	say(message, times = 1):
	print(message * times)

say('Привет')
say('Мир', 5)




input("\n\nНажмите Enter, чтобы выйти.")




#зачастую часть параметров функций могут необязательными, и для них будут использоваться некоторые заданные значения
#по умолчанию, если пользователь не укажет собственных. Этого можно достичь с помощью значений аргументов по умолчанию.
#Их можно указать, добавив к имени параметра в определении функции оператор присваивания (=) с последующим значением.

#Обратите внимание, что значение по умолчанию должно быть константой. Или точнее говоря, оно должно быть неизменным.
