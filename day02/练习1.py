#元祖
a=(1,2,5,8,10)
print(a)
for i in a:
    print(i)


b=(item for item in a if item%2==0)
for item in b:
  print(item)