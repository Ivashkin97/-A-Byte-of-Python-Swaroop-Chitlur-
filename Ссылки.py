print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist #mylist - лишь ещё одно имя, указывающее на тот же объект!

del shoplist[0] #Я сделал первую покупку, поэтому удаляю её из списка

print('shoplist:', shoplist)
print('mylist:', mylist)
#Обратите внимание, что и shoplist, и mylist выводят один и тот же список
# без пункта "яблоко", подтверждая тем самым, что они указывают на один объект

print('копирование при помощи полной вырезки')
mylist = shoplist[:] #создаем копию путем полной вырезки
del mylist[0] #удаляем первый элемент

print('shoplist:', shoplist)
print('mylist:', mylist)
#обратите внимание, что теперь списки разные

input("\n\nНажмите Enter, чтобы выйти.")








#Когда мы создаем объект и присваиваем его переменной, переменная только ссылается на объект, а не представляет собой этот объект!

#Т.е. имя переменной указывает на ту часть памяти компьютера, где хранится объект. Это называется привязкой имени к объекту.