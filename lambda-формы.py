#Ключевое слово lambda используется для создания функций и возврата их значения во время выполнения программы. lambda принимает параметр, за которым следует
#одно выражение, которое становится телом функции, а значение этого выражения возвращается новой функцией

points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
points.sort(key=lambda i : i['y'])
print(points)

input("\n\nНажмите Enter, чтобы выйти.")
