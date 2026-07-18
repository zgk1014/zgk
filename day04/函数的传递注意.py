def fun1():
    return 100

def fun2(num):
    print(num)

a=fun1()

fun2(a)

fun2(fun1())