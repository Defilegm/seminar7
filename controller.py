from importdata import importdata
from exportdata import exportdata
from sort import sorting
from printmode import *
def dataaction():
    switch = input('Выберите действие(введите цифру): импорт(1)\экспорт(2)\сортировка(3)\вывод по имени и фамилии(4): ')
    if int(switch) == 1:
        return importdata()
    if int(switch) == 2:
        return exportdata()
    if int(switch) == 3:
        sorting()
        return sorting()
    if int(switch) == 4:
        output()
        return output()
    else:
        print('\nНе выбрано ни одно из доступных действий')
dataaction()


