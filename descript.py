#!/usr/bin/env python
# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------------------------------
##### IF ветвление
#
x = int(raw_input('Введите число: '))
if x < 0:
    x = 0
    print u'Число отрицательное'
elif x == 0:
    print u'Число является 0'
elif x == 1:
    print u'Число 1'
else:
    print u'Число больше 1'

#--------------------------------------------------------------------------------------------------------
##### Логические выражения
# Логические значения True, False
# Логические операции and, or, not
# 0, [], "" - ложь, иначе - истина

### While
# Ряд Фибоначчи
#
a, b = 0, 1
while b < 10:
    print b
    a, b = b, a+b

### Цикл не хрена не делает
#
while 1:
    pass

### Распаковка кортежа
#
t = 12345, 54321 , 'hello!'
#распаковка a, b, c = t
#Множественное присваивание, обязательно слева сколько эл-ов в кортеже
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
#-------------------------------------------------------------------------------------------------------_

# for. Range
#
a = ['it','is','lectorium','interresant']
for i in a:
    print i

#Возвращает список значений
#
N=range(1,10)
M = N #Создает указатель на объект указателя N (т.е объект не копируется)
T = N[:] #Создает объект в памяти аналогичный N

range(10)
range(5,10)
range(1,10,3) 

#!!!!!!!!!!!--------------------------------------------------------------------------------------------
#
args = [3,6]
range(*args)

#xrange                                                                                                 #xrange
# Псевдосписок - объект, для которого мы можем получить значения элементов, но не можем изменить их или порядок их следования
#xrange не создает список, а создает псевдосписок. Всегда использовать xrange, а не range() чтоб не переполнить память
#
a = ['Что-то','новенькое']
for i in xrange(len(a)):
    print a[i]

#Break.Continue. Else
#element_to_find

for element in list:
    if element_to_find == element:
        print element,'Элемент найден' break
    else:
        print element1, 'Элемент не найден'
#Блок else выполняется есл вышед не через break
#--------------------------------------------------------------------------------------------------------

### Генератор списков
#
li = [1,9,8,4]
[elem*2 for elem in li]

#--------------------------------------------------------------------------------------------------------
### Импорты 3 вида
# urllib2 - библиотека работы с веб

from urllib2 import urlopen
from urllib2 import *
import urllib2.urlopen

if __name__ == "__main__"
# Запись говорит что если файл выполняется. 

#-------------------------------------------------------------------------------------------------------
###################################### Функции #########################################################
#Лямбда функции - неименованые функции
#
(lambda x: x*x)(5) # (5) - параметр переданный в лямбда функцию
foo = lambda x: x*x
print foo(7)


# -----------------------------------
#
def empty_func():
    pass

Функция без return возвращает None
print empty_func()
None
#------------------------------------
# Документация
#
def gcd(a,b):
    '''Greatest Common Divisor'''#docstring
    while a != 0:
        a,b = b%a, a
    return b
print gcd.__doc__

#------------------------------------
#
new_function = gcd
print new_function(14, 7)

#------------------------------------ 
#
def magic(v):
    v.append('Blue')
my_list = ['Red'.'Green']
magic(my_list)
print my_list

#------------------------------------ 
#
# Можем вернуть из функции кортеж
def multiout():
    return 1,2,3
print multiout()

#------------------------------------ 
#
# Переменные деляться на локальные, средние, глобальные
# Внутри функции локальные переменные, глобальные не меняют

#------------ Передача параметров в функцию
# Параметры могут передаваться в функцию по ссылке
a = 1
def(a):

# Могут быть параметры по умолчанию
def greet(adr='mr',name='X'):
    print "Hello %s %s" % (adr,name)
greet(name = 'Gates')
greet('Mr','Anderson')

#Значения по умолчанию вычисляются в точке определения функции
#
i = 5
def dooble_print(arg1, arg2 = i):
        print arg2
dooble_print(1,2)
1 2

dooble_print(arg2=1,5)
SyntaxError

# Значения по умолчанию вычисляются единожды
#
def list_function(a,my_lst=[]):
    my_lst.append(a)
    return my_lst
print list_finction(1)

# Передача неограниченного количества параметров(параметры передаются в виде списка)
#
def avg(*args):
    sum = 0.0
    for arg in args:
        sum += arg
    return sum/len(args)

# Передача параметров в виде словарей
#
def foo_kwargs(farg, **kwargs):
    print 'formal_arg:', farg
    for key in kwargs:
        print "keyword arg: %s: %s" % (key,kwargs[key])

foo_kwargs(farg=1,myarg2='two',myarg3=3)

# Замыкание
# Функция которая ссылается на свободные переменные в своем лексическом контексте.
# Замыкание — это особый вид функции. Она определена в теле другой функции и создаётся каждый раз во время её выполнения.
def make_adder(x):
   def adder(n):
     return x+n #Замыкание внешнего контекста
   return adder

adder = make_adder(10)
print adder(5)
# Вернет 15

#-----------------------------------
# filter(функция, последовательность)-- возвращает последовательность, состоящую из тех элементов для которых функция является истинной
list = [10, 4, 2, 5, 6 ]
filter(lambda x: x<5, list)

# map(функция, последовательность)--совершает вызов с каждым элементом последовательности и возвращает список фозвращенных функцией значений
list1=[7,2,3,1,12]
list2=[-1,1,-5,6,4]
map(lambda x,y: x*y,list1,list2)
