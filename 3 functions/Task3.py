"""
Напишите программу определяющую допуск ученика к зачету.
Программа должна запрашивать число учеников, затем у каждого ученика запрашивать балл за финальный тест
и в ответ печатать, допущен ли он (True или False) к зачету (необходимо набрать больше 50 баллов).

Ученикам без допуска должно печататься "Вы отчислены".

Выдачу допуска реализуй как функцию.
"""


def dopusk(points):
    if points > 50:
        return True
    else:
        return False


a = int(input("Сколько студентов в группе? ", ))#количество студентов
for i in range (a):
    name = input('Введите имя: ', )
    points = int(input('Сколько у вас баллов? ', ))
    dop = dopusk(points)

    if dop == False:
        print(name, ", вы отчислены!")
    else:
        print(name, ", вы допущены!")


