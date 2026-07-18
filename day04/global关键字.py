a=66
def fun1():
    print(f"fun1函数~~~{a}")
def fun2():
    global a
    a=200
    print(f"fun2函数~~~{a}")
fun1()
fun2()
fun1()