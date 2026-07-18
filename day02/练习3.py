#JSON读写数据
import json

# import json
# dict1={"username":"张三","age":18,"addr":"长沙","gender":"男"}
# with open("data.json","w",encoding="utf-8") as f:
#     json.dump(dict1,f,ensure_ascii=False)
#     print("数据加载完毕")


with open("data.json","r",encoding="utf-8") as f:
    information=json.load(f)
    print(information,type(information))