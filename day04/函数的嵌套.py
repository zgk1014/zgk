def func_A():
    print("------f start A------")
    print("我是A函数")
    print("------f end A------")


def func_B():
    print("------f start B------")
    func_A()
    print("------f end B------")
if __name__=='__main__':
    func_B()