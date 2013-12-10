#!/usr/bin/env python
#-*- coding: utf-8 *-

#----------------------------------------------------------
class MyClass:
    """Простой класс"""
    i = 12345
    def f(self):
        return 'Привет мир'


x = MyClass() #Экземпляр класса (instance)
#Обращение к объектам класса
MyClass.attr
MyClass.foo

#----------------------------------------------------------
 class Complex:
      def __init__(self, realpart, imagpart):
          self.r = realpart
          self.i = imagpart
         
x = Complex(3.0, -4.5)
x.r, x.i
(3.0,-4.5)

#-----------------------------------------------------------
class Student:
    city = "St.Peterburg"
    def __init__(self,name,year):
        self.name = name
        self.year = year
    def print_info(self):
        print self.name, self.year,

# Создаём instance класса Student
vasya = Student("Vasya",20)
vasya.name
vasya.year
vasya.gerlfriend="Anna"
vasya.city='Moscow'

# Методы private определяются 2 подчеркиваниями
def __print(self):
    print self.name, self.year
