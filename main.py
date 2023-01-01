#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def vn():
    def fun(a, b):
        return "Для значений a, b функция f(a,b) = ", a*b/2
    return fun

if __name__=='__main__':
    A = float(input("Введите a: "))
    B = float(input("Введите b: "))
    f = vn()
    print(f(A,B))