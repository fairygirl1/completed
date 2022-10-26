"""
Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси.
"""



def taxi(s):
    cost = 4.00 + s // 140 * 0.25
    if s % 140 != 0:
        cost = cost + 0.25
        return cost
    else:
        return cost

s = int(input())
print(taxi(s))

