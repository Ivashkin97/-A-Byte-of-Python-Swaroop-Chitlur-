#Функция repr используется для получения канонического строкового представления объекта. Любопытно, что в большинстве случаев eval(repr(object)) == object
#>>>i = []
#>>>i.append('item')
#repr(i)
#['item']
#>>>eval(repr(i)) == i
#True