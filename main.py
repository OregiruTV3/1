from math import tan,pi
import time
def decorator(func):
    print("Была вызвана функция{}".format(func))
    func()
    print(time.perf_counter())

def vi():
    print("введите переменные s,n")
    s = int(input("s: "))
    n = int(input("n: "))
    area = (n * s * s) / (4 * tan(pi / n))
    area = round(area)
    print("Ответ ",area)
def cait():
    print("введите переменную n")
    n=int(input("n: "))
    sum=((n)*(n+1))/2
    print("Ответ ",round(sum))
decorator(vi)
decorator(cait)