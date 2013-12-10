#!/usr/bin/env python
#-*- coding: utf-8 -*-

def fib(n): #Выводит числа фибоначи на экран
    a,b = 0,1
    while b < n:
        print b,
        a,b = b, b+a

def fib2(n): #Возвращает числа фибоначи не превосходящие n
    result = []
    a,b = 0,1
    while b < n:
        result.append(b)
        a,b = b, b+a
    return result




