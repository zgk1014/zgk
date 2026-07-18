def login(username,password):
    if username=='admin' and password=='123456':
        return "登陆成功"
    else:
        return "登录失败"
zhangsan=login("zhangsan","123456")
print(zhangsan)
lisi=login("lisi","123456")
print(lisi)