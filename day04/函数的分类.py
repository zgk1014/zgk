def fn1():
    print("你好")
    fn1()
def fn2():
    print("你好")
    return "天气",2
res=fn2()
print(res)
def fn3(a,b):
    print(a+b)
fn3(1,2)
def fn4(a,b,c="张三"):
    print(a,b,c)
    return a+b+c
res=fn4(1,2)
print(res)
