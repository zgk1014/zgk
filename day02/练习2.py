#字典
dict1={"username":"张三","age":18,"addr":"长沙","gender":"男"}
print(dict1,type(dict1))
dict1["height"]=180
print(dict1)
dict1["username"]="张无忌"
print(dict1)
del dict1["username"]
print(dict1)
print(dict1["addr"])



keys=dict1.keys()
print(keys)

for key in keys:
    print(f"键名:{key},值:{dict1[key]}")

values=dict1.values()
print(values)

