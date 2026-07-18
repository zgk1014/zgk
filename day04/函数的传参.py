def fn2(name,age,gender):
    print(name,age,gender)
fn2(age=18,gender="男",name="曾兵")
def fn3(name,age=18,gender="男"):
    print(name,age,gender)
fn3("张三2号")
def fn4(*args):
    print(args)
fn4(1,2,3,'张三')
def fn5(**Kwords):
    print(Kwords)
fn5(name="张三",age=18,gender="男")