def fn():
    return "你好"
res=fn()
print(res)
fn=lambda:"我好"
res=fn()
print(res)



def fn1(a,b):
    return a+b
res1=fn1(1,2)
print(res1)
fn1=lambda a,b:a+b
res1=fn1(1,2)
print(res1)
fn2=lambda a,b,c="小文":a+b+c
res2=fn2("问问","小李子")
print(res2)
fn3=lambda *args:args
res3=fn3(1,2,3,4,5,6)
print(res3)
fn4=lambda **kwargs:kwargs
res4=fn4(name="张三",age=18,gender="男")
print(res4)






