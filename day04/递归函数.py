def fn():
    flag = input("请输入小陀螺是否还在转动")
    if flag=="转":
        print("在梦见当中")
        fn()
    else:
        print("回到了现实当中")
        return
    fn()