s={1,2,3,4,5,6,7,8,9}
s.add("曾兵")
print(s)
s.remove("曾兵")
print(s)
for index,item in enumerate(s):
    print(index,item)
    s.clear()
    print(s)
    del s
    print(s)